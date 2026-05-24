# Pocket Option Signal Bot

A powerful, momentum-based trading bot for Pocket Option that sends high-accuracy signals (and can auto-trade) on all Forex pairs direct to Telegram. Supports both demo and real-money modes!

## Features
- Telegram bot signals & management
- Demo/Real money trading switch
- Trades all major Forex pairs
- Automated momentum-based technical analysis
- Auto-trade or manual signal modes
- Secure and customizable
- Stores trading and signal history locally (SQLite)

## Project Structure
```
pocket-option-signal-bot/
  ├── main.py                   # Bot entry point
  ├── telegram_bot.py           # Telegram features
  ├── trading_engine.py         # Signal generation & trade manager
  ├── pocket_option_api.py      # Pocket Option API integration
  ├── database.py               # Local database setup
  ├── config.py                 # App settings
  ├── requirements.txt          # Python deps
  └── README.md
```

## Quickstart
1. Clone the repo and run:
   ```sh
   pip install -r requirements.txt
   ```

2. Create your Telegram bot via [BotFather](https://t.me/BotFather) and note the token.

3. Add your config to `config.py`:
   ```python
   TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
   PO_EMAIL = 'your@email.com'          # Pocket Option login
   PO_PASSWORD = 'your_password'        # Pocket Option password
   DEFAULT_TRADE_AMOUNT = 1             # USD
   USE_DEMO_ACCOUNT = True              # Switch to False for real trades
   ALLOWED_USERS = ['your_telegram_id'] # Only these users can trade
   ```

4. Run the bot:
   ```sh
   python main.py
   ```

---
## ⚠️ Disclaimer
Automated trading is risky! Start with demo mode. Never risk funds you can't afford to lose.

## Next Steps
- I’ll generate the first Python files now.
- You’ll add your secret info only in your local code (keep tokens private).

---
