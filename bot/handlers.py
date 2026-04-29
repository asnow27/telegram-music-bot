"""
Bot command and message handlers
"""

import logging
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters
from bot.music import MusicPlayer

logger = logging.getLogger(__name__)
music_player = MusicPlayer()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Start command handler
    """
    await update.message.reply_text(
        'Welcome to Telegram Music Bot! 🎵\n\n'
        'Use /help to see available commands.'
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Help command handler
    """
    help_text = (
        '/start - Start the bot\n'
        '/help - Show this help message\n'
        '/play <song> - Play a song\n'
        '/stop - Stop playback\n'
        '/status - Show current status'
    )
    await update.message.reply_text(help_text)


async def play(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Play command handler
    """
    if not context.args:
        await update.message.reply_text('Usage: /play <song name>')
        return

    song_name = ' '.join(context.args)
    await update.message.reply_text(f'🎵 Playing: {song_name}')


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Stop command handler
    """
    await update.message.reply_text('⏹️ Playback stopped')


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Status command handler
    """
    await update.message.reply_text('🎵 Music Bot is running and ready!')


def setup_handlers(application) -> None:
    """
    Setup all handlers for the application
    """
    # Command handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('play', play))
    application.add_handler(CommandHandler('stop', stop))
    application.add_handler(CommandHandler('status', status))
