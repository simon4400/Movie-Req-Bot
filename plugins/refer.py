from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

BOT_USERNAME = os.environ.get("BOT_USERNAME")
REFERAL_COUNT = os.environ.get("REFERAL_COUNT", 20)

@Client.on_message(filters.command("refer") & filters.private)
async def refer_handler(client, message):
    user = message.from_user
    refer_link = f"https://t.me/{BOT_USERNAME}?start=VJ-{user.id}"

    text = f"""👥 **Your Referral Link**

🔗 `{refer_link}`

📣 Share this with friends and get **Premium** after **{REFERAL_COUNT} referrals**!
"""

    buttons = [[
        InlineKeyboardButton("📋 Copy Referral Link", url=refer_link)
    ]]

    await message.reply(
        text,
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True
  )
