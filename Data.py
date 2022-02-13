from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}
Bot For help You to Create Session.
[➼](https://telegra.ph/file/e1d35e61bd7e3bef4bfc8.jpg) So What U Waiting For Generat STRING Session
───────────────────────

If you don't trust this bot, 
1) stop reading this message
2) delete this chat
───────────────────────
Still reading?
You can use me to generate pyrogram and telethon string session. Use below buttons to learn more !

✗ Pᴏᴡᴇʀᴇᴅ �🔰 Bʏ: [XTREAM BOTS!](https://t.me/XTREAMUPDATES)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("💛 Start Generating Session 💛", callback_data="generate")],
    ]

    generate_button = [
        [InlineKeyboardButton("🔰 Start Generating Session 🔰", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🎉 START GENERATING SESSION 🎉", callback_data="generate")],
        [InlineKeyboardButton("😇 BOT STATUS AND UPDATES 😇", url="https://t.me/XTREAMUPDATES")],
        [
            InlineKeyboardButton("😉HOW TO USE 😉❔", callback_data="help"),
            InlineKeyboardButton("😎 ABOUT BOT 😎", callback_data="about")
        ],
        [InlineKeyboardButton("💖 UPDATES 💖", url="https://t.me/XTREAMUPDATES")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to Manage group and generate pyrogram and telethon string session by @XTREAMUPDATES

Source Code : [Click Here](https://github.com/priyanshutgbot/XTREAM SESSION GENERATOR)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @BELONGS_TO_LORDKRISHNA
    """
