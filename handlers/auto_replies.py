from telebot import TeleBot
from telebot.types import Message

def register_auto_reply_handlers(bot: TeleBot, config: dict, content: dict):
    """
    Registers handlers for both smart guides (Regex) and simple dictionary replies.
    """
    auto_replies_content = content["auto_replies"]
    auto_replies_config = config["auto_replies"]

    # --- Smart/Complex Handlers ---

    @bot.message_handler(regexp=r'(?i)(install|setup|guide).*(flutter|dart)')
    def flutter_installation_guide(message: Message):
        """
        Sends a comprehensive guide on how to install Flutter.
        """
        bot.send_chat_action(message.chat.id, 'typing')

        guide_text = (
            f"{auto_replies_content['flutter_installation_guide_title']}\n"
            f"{auto_replies_content['flutter_installation_guide_body']}"
        )

        try:
            bot.reply_to(message, guide_text, parse_mode='Markdown', disable_web_page_preview=True)
        except Exception as e:
            print(f"Error sending guide: {e}")

    # --- Simple Dictionary-based Replies ---

    @bot.message_handler(func=lambda message: message.text and message.text.lower() in auto_replies_config)
    def simple_auto_reply(message: Message):
        """
        Replies to a message if its text is found in the auto_replies dictionary.
        """
        try:
            reply_text = auto_replies_config[message.text.lower()]
            bot.reply_to(message, reply_text)
        except Exception as e:
            print(f"Error in auto reply: {e}")