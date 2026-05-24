import pandas as pd
import requests
import config
import pandas_ta as ta

def fetch_ohlc(pair, timeframe):
    # Fetch candles using Alpha Vantage (works for forex pairs)
    symbol = pair.replace('USD', '/USD')
    params = {
        'function': 'FX_INTRADAY',
        'from_symbol': pair[:3],
        'to_symbol': pair[3:],
        'interval': f'{timeframe}min',
        'outputsize': 'compact',
        'apikey': config.ALPHA_VANTAGE_API_KEY,
    }
    url = 'https://www.alphavantage.co/query'
    r = requests.get(url, params=params)
    data = r.json()
    try:
        key = list(data.keys())[1] # e.g., 'Time Series FX (5min)'
        df = pd.DataFrame.from_dict(data[key], orient='index').astype(float)
        df.columns = ['open','high','low','close'][:len(df.columns)]
        df = df.iloc[::-1] # Oldest first
        return df
    except Exception as e:
        return None

def analyze_market(df):
    if df is None or len(df) < 20:
        return None
    # Example simple signal: EMA cross with RSI filter
    df['ema_fast'] = ta.ema(df['close'], length=5)
    df['ema_slow'] = ta.ema(df['close'], length=10)
    df['rsi'] = ta.rsi(df['close'], length=14)
    if df['ema_fast'].iloc[-1] > df['ema_slow'].iloc[-1] and df['rsi'].iloc[-1] > 55:
        # Buy
        confidence = min(99, round(df['rsi'].iloc[-1]))
        return ('BUY', confidence)
    if df['ema_fast'].iloc[-1] < df['ema_slow'].iloc[-1] and df['rsi'].iloc[-1] < 45:
        # Sell
        confidence = 100 - round(df['rsi'].iloc[-1])
        return ('SELL', confidence)
    return None

def generate_signals(pairs, timeframes):
    signals = []
    for pair in pairs:
        for tf in timeframes:
            df = fetch_ohlc(pair, tf)
            result = analyze_market(df)
            if result:
                direction, confidence = result
                if confidence >= config.MIN_SIGNAL_CONFIDENCE:
                    signals.append({'pair': pair, 'timeframe': tf, 'signal': direction, 'confidence': confidence})
    return signals
