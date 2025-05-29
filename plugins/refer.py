import os, string, logging, random, asyncio, time, datetime, re, sys, json, base64
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Script import script
from database.users_chats_db import (
    db,
    delete_all_referal_users,
    get_referal_users_count,
    get_referal_all_users,
    referal_add_user
)
from info import BOT_USERNAME, ADMINS, PREMIUM_AND_REFERAL_MODE, REFERAL_PREMEIUM_TIME, REFERAL_COUNT, LOG_CHANNEL, GRP_LNK, SUPPORT_CHAT

@Client.on_message(filters.command("refer") & filters.private)
async def refer_handler(client, message):
    user = message.from_user
    refer_link = f"https://t.me/{BOT_USERNAME}?start=VJ-{user.id}"

    text = f"""👥 Your Referral Link

🔗 {refer_link}

📣 Share this with friends and get Premium after {REFERAL_COUNT} referrals!
"""

    buttons = [[
        InlineKeyboardButton("📋 Copy Referral Link", url=refer_link)
    ]]

    await message.reply(
        text,
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True
    )
