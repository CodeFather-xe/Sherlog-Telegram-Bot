# SherLog: Your Vigilant Telegram Group Moderator

SherLog is a powerful and customizable Telegram bot designed to help you manage and moderate your group with ease. Built with Python and the `pyTelegramBotAPI` library, SherLog is particularly well-suited for programming and developer communities, helping to maintain a clean, organized, and professional environment.

![SherLog Banner](https://github.com/user-attachments/assets/112429ea-4c59-4d80-92fe-e3a15096f6c5)

## 🌟 Key Features

SherLog comes packed with features to make your group a better place:

- **👋 Welcome Messages:** Greet new members with a customizable welcome message, setting the right tone for your community from the very beginning.
- **🚫 Content Moderation:**
    - **Bad Word Filter:** Automatically deletes messages containing words from a configurable blacklist.
    - **Link Filter:** Restricts links to a whitelist of approved domains, preventing spam and malicious links.
    - **Code Formatting Police:** Enforces clean code sharing by reminding users to format their code properly.
- **👑 Admin Tools:**
    - `/ban` & `/unban`: Easily ban and unban users from your group.
    - `/mute` & `/unmute`: Temporarily mute and unmute members.
    - `/clean <n>`: Smartly deletes the last `n` messages. It uses a topic-aware history manager to ensure messages are deleted only from the current topic, keeping other topics safe.
- **🚨 Reporting System:**
    - `/report`: Allows group members to report inappropriate messages to the admins.
- **🤖 Auto-Replies:**
    - Set up custom replies for common questions or phrases.
    - Includes a detailed guide on how to install Flutter, perfect for Flutter communities.
- **🕵️‍♂️ Privacy:**
    - Forwards all private messages sent to the bot directly to the owner.
- **📢 Updates & Info:**
    - `/checkupdate`: Displays the latest changelog and upcoming features.
    - `/help` or `/start`: Shows a comprehensive guide on how to use the bot.
    

## 🚀 Getting Started

To get SherLog up and running for your own group, follow these simple steps:

### 1. Prerequisites

- Python 3.x
- `pip` for installing packages

### 2. Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/CodeFather-xe/Sherlog-Bot.git
   cd SherLog
   ```
2. **Install the required packages:**
   ```bash
   pip install pytelegrambotapi
   ```

### 3. Configuration

1. **Create a `config.json` file:**
   In the root of the project, create a file named `config.json`.

2. **Add your configuration:**
   Copy and paste the following JSON structure into your `config.json` and fill in the values:

   ```json
   {
     "bot_token": "YOUR_TELEGRAM_BOT_TOKEN",
     "owner_id": YOUR_TELEGRAM_USER_ID,
     "bad_words": [
       "badword1",
       "badword2"
     ],
     "whitelisted_domains": [
       "github.com",
       "stackoverflow.com"
     ],
     "auto_replies": {
       "hello": "Hello! How can I help you?",
       "help": "Please refer to the group description for help."
     }
   }
   ```
   - `bot_token`: Your Telegram bot token from @BotFather.
   - `owner_id`: Your personal Telegram user ID.

### 4. Running the Bot

Once you have completed the configuration, you can start the bot:

```bash
python main.py
```

## 🤖 Usage

Here are the commands you can use with SherLog:

- `/help` or `/start`: Get a list of all commands and how to use them.
- `/report`: Reply to a message with this command to report it.
- `/checkupdate`: See what's new with the bot.

### Admin Commands

- `/ban`: Reply to a user's message to ban them.
- `/unban`: Reply to a user's message to unban them.
- `/mute`: Reply to a user's message to mute them.
- `/unmute`: Reply to a user's message to unmute them.

## 📁 Project Structure

```
/SherLog
├── config.json
├── main.py
├── utils.py
├── handlers/
│   ├── admin_actions.py
│   ├── auto_replies.py
│   ├── check_updates.py
│   ├── moderation.py
│   ├── private_messages.py
│   ├── reporting.py
│   └── welcome.py
└── README.md
```

## 🤝 Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
