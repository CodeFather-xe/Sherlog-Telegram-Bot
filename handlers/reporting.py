from telebot import TeleBot
from telebot.types import Message

def register_reporting_handlers(bot: TeleBot, config: dict, content: dict):
    """
    Registers handlers for reporting messages to the owner.
    """
    owner_id = config["owner_id"]
    info_content = content["info"]

    @bot.message_handler(commands=['report'])
    def report_message(message: Message):
        """
        Forwards a reported message to the owner with full details.
        """
        if message.reply_to_message:
            reporter = message.from_user
            reporter_ref = f"@{reporter.username}" if reporter.username else reporter.first_name
            
            offender = message.reply_to_message.from_user
            offender_ref = f"@{offender.username}" if offender.username else offender.first_name
            
            chat_title = message.chat.title or "Private Chat"

            report_text = (
                f"🚨 **NEW REPORT ALERT** 🚨\n\n"
                f"👮‍♂️ **Reporter:** {reporter_ref} (`{reporter.id}`)\n"
                f"🚫 **Offender:** {offender_ref} (`{offender.id}`)\n"
                f"📂 **Chat:** {chat_title}\n"
                f"⬇️ **The Message is forwarded below:**"
            )

            try:
                bot.send_message(owner_id, report_text, parse_mode='Markdown')
                bot.forward_message(owner_id, message.chat.id, message.reply_to_message.message_id)
                
                bot.reply_to(message, info_content["report_message_success"])
                
                try:
                    bot.delete_message(message.chat.id, message.message_id)
                except Exception:
                    pass

            except Exception as e:
                print(f"Error reporting message: {e}")
                bot.reply_to(message, info_content["report_message_error"])
        else:
            bot.reply_to(message, info_content["report_message_prompt"])