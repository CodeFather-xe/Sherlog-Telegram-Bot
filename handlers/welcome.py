from telebot import TeleBot
from telebot.types import Message

def register_welcome_handlers(bot: TeleBot, config: dict, content: dict):
    """
    Registers handlers for welcoming new members with a formal tone.
    """
    welcome_content = content["welcome"]
    community_name = config["community_name"]

    @bot.message_handler(content_types=['new_chat_members'])
    def welcome_new_member(message: Message):
        """
        Sends a formal welcome message introducing the bot.
        """
        for new_member in message.new_chat_members:
            if new_member.is_bot:
                continue
            
            user_mention = f"[{new_member.first_name}](tg://user?id={new_member.id})"
            
            welcome_text = welcome_content["new_member_message"].format(
                user_mention=user_mention,
                community_name=community_name
            )

            try:
                bot.send_message(
                    chat_id=message.chat.id,
                    text=welcome_text,
                    message_thread_id=message.message_thread_id,
                    parse_mode='Markdown'
                )
            except Exception as e:
                print(f"Error sending welcome message: {e}")