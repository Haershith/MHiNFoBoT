import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Bot = Client(
    "Info Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)


MHSTART = """
**MH User Details:**

**First Name:** `{user.first_name}`
**Last Name:** `{user.last_name},`" if user.last_name else "
**User Id:** `{user.id}`
**Username:** @{user.username}" if user.username else "
**User Link:** {user.mention}" if user.username else "
**DC ID:** `{user.dc_id}`" if user.dc_id else "
**Is Deleted:** True" if user.is_deleted else "
**Is Bot:** True" if user.is_bot else "
**Is Verified:** True" if user.is_verified else "
**Is Restricted:** True" if user.is_verified else "
**Is Scam:** True" if user.is_scam else "
**Is Fake:** True" if user.is_fake else "
**Is Support:** True" if user.is_support else "
**Language Code:** {user.language_code}" if user.language_code else "
**Status:** {user.status}" if user.status else "
"""

START_TEXT = """<b>Hello {}
I am a Simple Telegram Info Bot, Click /help for more information<b>"""


BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton(text="💞 Join", url=f"https://t.me/MutyalaHarshith")]])


@Bot.on_message(filters.private & filters.command("start"))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )

@Bot.on_message(filters.private & filters.command("myinfo"))
async def start(bot, update):
    await update.reply_text(
        text=MHSTART.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )

@Bot.on_message(filters.private & filters.command("mhinfo"))
async def info(bot, update):
    
    text = f"""--**Information from Harshith**--
**💞 First Name :** {update.from_user.first_name}
**😎 Your Second Name :** {update.from_user.last_name if update.from_user.last_name else 'None'}
**🥳 Your Username :** {update.from_user.username}
**😜 Your Telegram ID :** {update.from_user.id}
**🤫 Your Profile Link :** {update.from_user.mention}"""
    
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )


@Bot.on_message(filters.private & filters.sticker)
async def stickers(_, message):
       await message.reply(f"Your Requested Sticker's ID is   * `{message.sticker.file_id}` *", quote=True)
   
print("Bot Started!!! Now Join on @MutyalaHarshith")
Bot.run()
