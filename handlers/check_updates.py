from telebot import TeleBot
from telebot.types import Message

def register_info_handlers(bot: TeleBot, config: dict, content: dict):
    """
    Registers handlers for general information commands like checkupdate.
    """
    info_content = content["info"]
    developer_username = config["developer_username"]

    @bot.message_handler(commands=['checkupdate'])
    def check_update_command(message: Message):
        """
        Displays the changelog and upcoming features for the bot.
        """
        update_text = info_content["update_changenlog"].format(developer_username=developer_username)
        
        try:
            bot.reply_to(message, update_text, parse_mode='Markdown')
        except Exception as e:
            print(f"Error sending update message: {e}")