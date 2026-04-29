# Telegram Music Bot

A Python-based Telegram bot for playing and managing music.

## Features

- Search and play music
- Queue management
- Playlist support
- User-friendly controls

## Requirements

- Python 3.8+
- Telegram Bot API token

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/asnow27/telegram-music-bot.git
   cd telegram-music-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your Telegram bot token and configuration
   ```

4. Run the bot:
   ```bash
   python main.py
   ```

## Configuration

Create a `.env` file with the following variables:

```
TELEGRAM_BOT_TOKEN=your_bot_token_here
LOG_LEVEL=INFO
```

## Usage

Start a chat with your bot on Telegram and use the available commands:

- `/start` - Start the bot
- `/help` - Show help message
- `/play <song>` - Play a song
- `/stop` - Stop playback
- `/status` - Show current status

## Project Structure

```
telegram-music-bot/
├── main.py
├── bot/
│   ├── __init__.py
│   ├── handlers.py
│   └── music.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License - see LICENSE file for details
