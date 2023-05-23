# © Telegram @HMF_Owner_1, GitHub @ThiruXD 

import os
from f import *


class Config(object):
	API_ID = int(os.environ.get("API_ID", "14553761"))
	API_HASH = os.environ.get("API_HASH", "a1cab49dcdfd2eb3bea5e5a552c5d479")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "Bot Token")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "Bot Username")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "DB Channel Id"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "604152966"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "MongoDB URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "Logs Channel Id")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	BASE_SITE = os.environ.get("BASE_SITE", "kpslink.in")
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

👑 **Owner:** @Nanthakps

📢 **Updates Channel:** @KPSLink

👥 **Support Group:** @KPSLinkGroup

"""
	ABOUT_DEV_TEXT = f"""
**🌐 This Bot Was Devloped By** : @Nanthakps"""
	SHORTENER_API_MESSAGE = """**To add or update your Shortner Website API,
            
Example : `/api 8f17fbb5023fcc76fa7e379e3b9157a84e56e0ba`

Current Website: {base_site}

Current Shortener API: `{shortener_api}`**"""

PREFIX = ["/", ".", "?", "#", "@", "₹", "+", ":", "!", "^", "|"]
START_MEDIA = "https://telegra.ph/file/d20dee1ba93fc0b0c05ac.jpg"
START_TEXT = """Hɪ/Hᴇʟʟᴏ [{}](tg://user?id={})

I'ᴍ Uʟᴛʀᴀ Fᴀsᴛ Tᴇʟᴇɢʀᴀᴍ Cᴏᴜʟᴅ Sᴛᴏʀᴀɢᴇ Bᴏᴛ  Fᴏʀ [KPS Link](https://kpslink.in). Sᴇɴᴅ Mᴇ Aɴʏ Fɪʟᴇs/Lɪɴᴋs Aɴᴅ Sᴇʟᴇᴄᴛ Mᴇᴛʜᴏᴅ Wᴀɪᴛ Fᴇᴡ Sᴇᴄᴏɴᴅs Bᴏᴛ Wɪʟʟ Bᴇ Uᴘʟᴏᴀᴅ Tᴏ Oᴜʀ Sᴇʀᴠᴇʀ Aɴᴅ Gᴇɴᴀʀᴀᴛᴇ  [KPS Link](https://kpslink.in) ......

Cᴜʀʀᴇɴᴛʟʏ Sᴜᴘᴘᴏʀᴛᴇᴅ Fᴏʀᴍᴀᴛs :

• Lɪɴᴋs - Aʟsᴏ Sᴜᴘᴘᴏʀᴛ Bᴜʟᴋ Lɪɴᴋs 
• Fɪʟᴇs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB
• Vɪᴅᴇᴏs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB
• Aᴜᴅɪᴏs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB
• Pʜᴏᴛᴏs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB

Mᴏʀᴇ Fᴏʀᴍᴀᴛs Cᴏᴍᴍɪɴɢ Sᴏᴏɴ ......

Pᴏᴡᴇʀᴇᴅ Bʏ : [KPS Link](https://kpslink.in)"""

HELP_TEXT = """Hᴏᴡ Tᴏ Cᴏɴɴᴇᴄᴛ Wɪᴛʜ Wᴇʙsɪᴛᴇ:

Sᴛᴇᴘ Nᴏ 1 : Jᴜsᴛ Cʟɪᴄᴋ 'Cʟɪᴄᴋ Tᴏ Gᴇᴛ Aᴘɪ' Bᴜᴛᴛᴏɴ Aɴᴅ Cᴏᴘʏ Yᴏᴜʀ [KPS Link](https://kpslink.in) Aᴄᴄᴏᴜɴᴛ Aᴘɪ Tᴏᴋᴇɴ.

Sᴛᴇᴘ Nᴏ 2 : Tʜᴇɴ Cᴏᴍ Aɢᴀɪɴ Hᴇʀᴇ Aɴᴅ Usᴇ /api Tᴏ Cᴏɴɴᴇᴄᴛ Wɪᴛʜ Yᴏᴜʀ [KPS Link](https://kpslink.in) Aᴄᴄᴏᴜɴᴛ.

Exᴀᴍᴘʟᴇ : `/api 8f17fbb5023fcc76fa7e379e3b9157a84e56e0ba` """

ABOUT_TEXT = """🤖 Name :  Tamizh Masters Link Convertor

👑 Owner     : @Nanthakps

©️Powered By @KPSLink """



