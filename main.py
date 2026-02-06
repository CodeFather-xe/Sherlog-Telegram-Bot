import telebot
from utils import load_config, load_content

from handlers.welcome import register_welcome_handlers
from handlers.admin_actions import register_admin_handlers
from handlers.reporting import register_reporting_handlers
from handlers.moderation import register_moderation_handlers
from handlers.auto_replies import register_auto_reply_handlers
from handlers.private_messages import register_private_message_handlers
from handlers.check_updates import register_info_handlers

def main():
    """
    The main function to initialize and run the Telegram bot.
    """
    # 1. Load configurations and content
    config = load_config()
    if not config:
        print("Error: Could not load config.json")
        return

    content = load_content()
    if not content:
        print("Error: Could not load content.json")
        return

    # 2. Create bot instance
    try:
        bot = telebot.TeleBot(config["bot_token"])
    except Exception as e:
        print(f"Error initializing bot: {e}")
        return

    # 3. Register all handlers
    register_moderation_handlers(bot, config, content)
    register_admin_handlers(bot, config, content)
    register_reporting_handlers(bot, config, content)
    register_welcome_handlers(bot, config, content)
    register_auto_reply_handlers(bot, config, content)
    register_private_message_handlers(bot, config["owner_id"])
    register_info_handlers(bot, config, content)

    # 4. Start the bot
    print("🤖 SherLog Bot is running and watching...")
    print("Press Ctrl+C to stop safely.")

    try:
        bot.infinity_polling(timeout=60, long_polling_timeout=60)
    except (KeyboardInterrupt, SystemExit):
        print("\n🛑 Bot stopped safely. Goodbye!")

if __name__ == "__main__":
    main()