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
    Help command handler - Shows available commands
    """
    help_text = (
        '/info - Informasi tentang Bot\n'
        '/developers - Daftar Developer\n'
        '/link - Link Grup Bot\n'
        '/taunting - Taunting Message\n'
        '/versi - Versi Bot\n'
        '/play <song> - Play a song\n'
        '/stop - Stop playback\n'
        '/status - Show current status'
    )
    await update.message.reply_text(help_text)


async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Info command handler
    """
    info_text = (
        '----------------------------\n'
        '        Bot by ALIPCY\n'
        '        Bot gabut wkwk\n'
        '----------------------------'
    )
    await update.message.reply_text(info_text)


async def developers(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Developers command handler
    """
    dev_text = (
        '==============\n'
        '  ALIPCY. 27✅\n'
        '  Running On Grup\n'
        '=============='
    )
    await update.message.reply_text(dev_text)


async def link_grup(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Link Grup command handler
    """
    link_text = (
        'Link Grup Bot:\n'
        't.me/your_group_link'
    )
    await update.message.reply_text(link_text)


async def taunting(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Taunting command handler
    """
    taunting_text = (
        'Wkwk bot gabut aja kok 😂\n'
        'Tapi tetep canggih hehe 🤖'
    )
    await update.message.reply_text(taunting_text)


async def versi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Version command handler
    """
    versi_text = (
        'Telegram Music Bot\n'
        'Versi: 1.0.0\n'
        'Status: Beta'
    )
    await update.message.reply_text(versi_text)


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
    application.add_handler(CommandHandler('info', info))
    application.add_handler(CommandHandler('developers', developers))
    application.add_handler(CommandHandler('link', link_grup))
    application.add_handler(CommandHandler('taunting', taunting))
    application.add_handler(CommandHandler('versi', versi))
    application.add_handler(CommandHandler('play', play))
    application.add_handler(CommandHandler('stop', stop))
    application.add_handler(CommandHandler('status', status))
