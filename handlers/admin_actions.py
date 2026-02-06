import time
from telebot import TeleBot
from telebot.types import Message, ChatPermissions

def register_admin_handlers(bot: TeleBot, config: dict, content: dict):
    """
    Registers handlers for admin commands (Ban, Unban, Mute, Unmute) and the help command.
    """
    owner_id = config["owner_id"]
    admin_messages = content["admin_messages"]
    help_content = content["help_command"]

    def is_owner(message: Message) -> bool:
        """Checks if the message sender is the owner."""
        return message.from_user.id == owner_id

    def deny_access(message: Message):
        """
        Sends an access denied message and auto-deletes both messages after 5 seconds.
        """
        try:
            warning_msg = bot.reply_to(message, admin_messages["access_denied"])
            time.sleep(5)
            bot.delete_message(message.chat.id, message.message_id)
            bot.delete_message(message.chat.id, warning_msg.message_id)
        except Exception:
            pass  # Ignore errors if messages are already deleted

    # --- Ban/Unban Commands ---
    @bot.message_handler(commands=['ban'])
    def ban_user(message: Message):
        """
        Bans a user from the chat.
        """
        if not is_owner(message):
            deny_access(message)
            return

        if not message.reply_to_message:
            bot.reply_to(message, admin_messages["ban_reply_prompt"])
            return

        user_to_ban = message.reply_to_message.from_user
        try:
            bot.ban_chat_member(message.chat.id, user_to_ban.id)
            bot.reply_to(message, admin_messages["ban_success"].format(user_first_name=user_to_ban.first_name), parse_mode='Markdown')
        except Exception as e:
            bot.reply_to(message, f"Error: {e}")

    @bot.message_handler(commands=['unban'])
    def unban_user(message: Message):
        """
        Unbans a user from the chat.
        """
        if not is_owner(message):
            deny_access(message)
            return

        if not message.reply_to_message:
            bot.reply_to(message, admin_messages["unban_reply_prompt"])
            return

        user_to_unban = message.reply_to_message.from_user
        try:
            bot.unban_chat_member(message.chat.id, user_to_unban.id, only_if_banned=True)
            bot.reply_to(message, admin_messages["unban_success"].format(user_first_name=user_to_unban.first_name), parse_mode='Markdown')
        except Exception as e:
            bot.reply_to(message, f"Error: {e}")

    # --- Mute/Unmute Commands ---
    @bot.message_handler(commands=['mute'])
    def mute_user(message: Message):
        """
        Mutes a user in the chat.
        """
        if not is_owner(message):
            deny_access(message)
            return

        if not message.reply_to_message:
            bot.reply_to(message, admin_messages["mute_reply_prompt"])
            return

        user_to_mute = message.reply_to_message.from_user
        try:
            bot.restrict_chat_member(
                message.chat.id,
                user_to_mute.id,
                permissions=ChatPermissions(can_send_messages=False)
            )
            bot.reply_to(message, admin_messages["mute_success"].format(user_first_name=user_to_mute.first_name), parse_mode='Markdown')
        except Exception as e:
            bot.reply_to(message, f"Error: {e}")

    @bot.message_handler(commands=['unmute'])
    def unmute_user(message: Message):
        """
        Unmutes a user in the chat.
        """
        if not is_owner(message):
            deny_access(message)
            return

        if not message.reply_to_message:
            bot.reply_to(message, admin_messages["unmute_reply_prompt"])
            return

        user_to_unmute = message.reply_to_message.from_user
        try:
            bot.restrict_chat_member(
                message.chat.id,
                user_to_unmute.id,
                permissions=ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_other_messages=True
                )
            )
            bot.reply_to(message, admin_messages["unmute_success"].format(user_first_name=user_to_unmute.first_name), parse_mode='Markdown')
        except Exception as e:
            bot.reply_to(message, f"Error: {e}")

    # --- Help Command ---
    @bot.message_handler(commands=['help', 'start'])
    def help_command(message: Message):
        """
        Displays the help message.
        """
        help_text = (
            f"{help_content['title']}\n\n"
            f"{help_content['intro']}\n\n"
            f"{help_content['reporting_title']}\n"
            f"{help_content['reporting_body']}\n\n"
            f"{help_content['code_style_title']}\n"
            f"{help_content['code_style_body']}\n\n"
            f"{help_content['code_example']}\n\n"
            f"{help_content['link_safety_title']}\n"
            f"{help_content['link_safety_body']}\n\n"
            f"{help_content['outro']}"
        )
        
        try:
            bot.reply_to(message, help_text, parse_mode='Markdown')
        except Exception as e:
            print(f"Error sending help message: {e}")