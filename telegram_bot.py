import logging
import config
from telegram.ext import Updater, CommandHandler
from signal_engine import generate_signals

logging.basicConfig(level=logging.INFO)

user_settings = {
    'pairs': config.DEFAULT_PAIRS[:],
    'timeframes': config.DEFAULT_TIMEFRAMES[:],
}

def start(update, context):
    update.message.reply_text('Welcome to Pocket Option Signal Bot!\nUse /set_pairs and /set_timeframes to configure your signals.')

def set_pairs(update, context):
    pairs = context.args
    user_settings['pairs'] = pairs
    update.message.reply_text(f'✅ Signal pairs updated: {", ".join(pairs)}')

def set_timeframes(update, context):
    try:
        timeframes = [int(t) for t in context.args]
        user_settings['timeframes'] = timeframes
        update.message.reply_text(f'✅ Signal timeframes updated: {", ".join(map(str, timeframes))} minutes')
    except ValueError:
        update.message.reply_text('Usage: /set_timeframes 5 10 15 30')

def signal(update, context):
    update.message.reply_text('Analyzing market...')
    signals = generate_signals(user_settings['pairs'], user_settings['timeframes'])
    if not signals:
        update.message.reply_text('No strong signals found at this time.')
    else:
        for s in signals:
            msg = f"\n📊 New Signal!\nPair: {s['pair']}\nTimeframe: {s['timeframe']}m\nDirection: {s['signal']}\nConfidence: {s['confidence']}%\n"
            update.message.reply_text(msg)

def run_bot():
    updater = Updater(token=config.TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('set_pairs', set_pairs))
    dp.add_handler(CommandHandler('set_timeframes', set_timeframes))
    dp.add_handler(CommandHandler('signal', signal))
    updater.start_polling()
    updater.idle()
