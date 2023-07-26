import os
from os import getenv
from dotenv import load_dotenv
from helpers.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCO5p9kWJ8G5ju4XLWE_eMQQEEBXYcNKaOiJBVR6zL1KjAI1qZM7Pj01_qjldNCJWMvSRStqibhVC_wcTGviELKpfsYCvp8BE4rMOKF8l40ACvLzXSCLko_fkvJsr2_mr0mD_2M0uweFeEhNZGAxHooIOgb-cYmRxwDtoB34M92xDZGOS8mZJSXoKZolhhbVWgXXcQeUlliLYgg8B7GLYueO0-ynT32P_pY47I3V3fIH-6oTzHqQr9PGZ3XQRA1Q7mpHh4-ZPxLAofCFU6mB8CH-dYrYRX7obMfdjiklFEJUiJKmPwPfbUPYbe3CwqkS4TNvZqsWjp5OY1f9NMWiWyQAAAAATmDeAIA")
BOT_TOKEN = getenv("BOT_TOKEN", "AAHifZOeb5UURh-X8APKhBVWCidv8aZvI_A")
BOT_NAME = getenv("BOT_NAME", "Multi Person")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/8628c642a266a22effd8c.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/4c39fbb88932761913fff.png")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/73e10ed6e2bd32b478de6.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
API_ID = int(getenv("API_ID", "27957041"))
API_HASH = getenv("API_HASH", "2ae1c9912cd2efdecae7f0208994f0b0")
BOT_USERNAME = getenv("BOT_USERNAME", "SVDmulti_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "pattuchokar")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "https://t.me/SVD_support_group")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/we_are_universee")
# isi dengan username kamu tanpa simbol @
OWNER_NAME = getenv("OWNER_NAME", "soupboy_single")
# fill with your nickname
ALIVE_NAME = getenv("ALIVE_NAME", "force")
# fill with your id as the owner of the bot
OWNER_ID = int(os.environ.get("OWNER_ID", "655594746"))
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Testingbots01:TESTING1122334455@cluster001.exchcbz.mongodb.net/?retryWrites=true&w=majority")  # fill with your mongodb url
# make a private channel and get the channel id
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001600523208"))
# just fill with True or False (optional)
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "999"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "655594746").split()))
# UPDATER CONFIG
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get(
    "UPSTREAM_REPO", "https://github.com/Soupbot/SmartmusicSVD"
)
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)
