import asyncio
from ProMusic import app
from pyrogram import Client, filters
from datetime import datetime, timedelta
from pyrogram.errors import FloodWait
from ProMusic.core.mongo import db as nayka
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ProMusic.utils.database import get_served_users, get_served_chats


OWNER_ID = 6348268237
