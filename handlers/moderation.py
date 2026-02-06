import re
from telebot import TeleBot
from telebot.types import Message

# A dictionary to store the number of warnings for each user (in memory)
user_warnings = {}

def register_moderation_handlers(bot: TeleBot, config: dict, content: dict):
    """
    Registers handlers for message moderation with admin immunity.
    """
    owner_id = config["owner_id"]
    bad_words = config["bad_words"]
    whitelisted_domains = config["whitelisted_domains"]
    moderation_content = content["moderation"]

    bad_words_pattern = re.compile(r'\b(' + '|'.join(map(re.escape, bad_words)) + r')\b', re.IGNORECASE)

    @bot.message_handler(func=lambda m: m.text and bad_words_pattern.search(m.text))
    def filter_bad_words(message: Message):
        """
        Filters messages containing bad words.
        """
        if message.from_user.id == owner_id:
            return

        try:
            user_ref = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
            
            try:
                bot.forward_message(owner_id, message.chat.id, message.message_id)
                log_text = moderation_content["bad_word_log"].format(user_ref=user_ref, user_id=message.from_user.id)
                bot.send_message(owner_id, log_text, parse_mode='Markdown')
            except Exception as e:
                print(f"Error forwarding bad word evidence: {e}")

            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(
                message.chat.id,
                moderation_content["bad_word_warning"].format(user_ref=user_ref)
            )
        except Exception as e:
            print(f"Error in bad words filter: {e}")

    @bot.message_handler(func=lambda m: m.text and re.search(r'https?://[^\s]+', m.text))
    def filter_links(message: Message):
        """
        Filters messages containing links from non-whitelisted domains.
        """
        if message.from_user.id == owner_id:
            return

        try:
            urls = re.findall(r'https?://[^\s]+', message.text)
            
            for url in urls:
                domain_match = re.search(r'https?://(?:www\.)?([^/]+)', url)
                if domain_match:
                    domain = domain_match.group(1).lower()
                    
                    if domain not in whitelisted_domains:
                        user_id = message.from_user.id
                        current_count = user_warnings.get(user_id, 0) + 1
                        user_warnings[user_id] = current_count

                        user_ref = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
                        
                        bot.reply_to(
                            message,
                            moderation_content["link_warning"].format(user_ref=user_ref)
                        )

                        log_text = moderation_content["link_log"].format(
                            user_ref=user_ref,
                            user_id=user_id,
                            warning_count=current_count,
                            url=url
                        )
                        bot.send_message(owner_id, log_text, parse_mode='Markdown')
                        bot.forward_message(owner_id, message.chat.id, message.message_id)
                        
                        break 
        except Exception as e:
            print(f"Error in link filter: {e}")

    @bot.message_handler(func=lambda m: m.text and len(m.text.splitlines()) > 10 and any(c in m.text for c in ['{', '}', ';']) and '```' not in m.text)
    def code_police(message: Message):
        """
        Deletes messages containing long unformatted code and sends a warning.
        """
        if message.from_user.id == owner_id:
            return

        try:
            bot.delete_message(message.chat.id, message.message_id)
            user_ref = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
            
            bot.send_message(
                message.chat.id,
                moderation_content["code_police_warning"].format(user_ref=user_ref)
            )
        except Exception as e:
            print(f"Error in code police: {e}")