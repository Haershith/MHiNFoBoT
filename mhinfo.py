import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Bot = Client(
    "Info Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)



START_TEXT = """<b>Hello {}
I am a Simple Telegram Info Bot, Click /help for more information<b>"""


BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton(text="💞 Join", url=f"https://t.me/MutyalaHarshith"),
                                 InlineKeyboardButton(text="Support", url=f"https://t.me/MHGcHaT")]])


@Bot.on_message(filters.private & filters.command("start"))
async def start(bot, update):
    await update.reply_chat_action("Typing")
    await message.reply_sticker("CAACAgUAAxkBAAIalGLE9oYp8uXULytxu4OyVDWmIzK4AALfAAMulAABVkmUkirdqMRQHgQ")
    await asyncio.sleep(1)
    await m.delete()
    await message.reply_photo(
        photo="https://telegra.ph/file/236794ce4bb2213eaae1e.jpg",
        caption=START_TEXT.format(update.from_user.mention),
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
**🤫 Your Profile Link :** {update.from_user.mention}

**DC ID:** {update.from_user.dc_id}
**Language Code:** {update.from_user.language_code if update.from_user.language_code else 'None'}
**Status:** {update.from_user.status if update.from_user.status else 'None'}
"""
    
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
