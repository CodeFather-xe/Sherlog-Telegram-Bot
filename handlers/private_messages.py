from telebot import TeleBot
from telebot.types import Message

def register_private_message_handlers(bot: TeleBot, owner_id: int):
    """
    Registers handlers to forward private messages (DMs) to the owner.
    """
    @bot.message_handler(func=lambda m: m.chat.type == 'private')
    def handle_private_messages(message: Message):
        """
        Forwards private messages to the bot owner.
        """
        if message.from_user.id == owner_id:
            return

        sender = message.from_user
        username = f"@{sender.username}" if sender.username else "No Username"
        
        info_text = (
            f"📨 **New Private Message**\n\n"
            f"👤 **From:** {sender.first_name}\n"
            f"🔗 **User:** {username}\n"
            f"🆔 **ID:** `{sender.id}`\n"
            f"⬇️ **Content Below:**"
        )

        try:
            bot.send_message(owner_id, info_text, parse_mode='Markdown')
            bot.forward_message(owner_id, message.chat.id, message.message_id)
        except Exception as e:
            print(f"Error forwarding private message: {e}")