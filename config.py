import re
import os
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Required
API_ID = 26950458
API_HASH = "d818b8d530e4a9b209509815ab1b9c7c"
BOT_TOKEN = "8023030133:AAGlaP-jDQQ3fVYMui10qyIsIfwZMSiSkPE"
MONGO_DB_URI = "mongodb+srv://knight4563:knight4563@cluster0.a5br0se.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
MUSIC_BOT_NAME = "LOVER MUSIC"
PRIVATE_BOT_MODE = False

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 10000))

LOGGER_ID = -1002881142866
OWNER_ID = 7926944005

# Heroku
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/code663/DAXXMUSIC")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = "https://t.me/dark_x_knight_musiczz_support"
SUPPORT_CHAT = "https://t.me/+DbezTihsh_VlYzY1"

AUTO_LEAVING_ASSISTANT = False
AUTO_GCAST = False
AUTO_GCAST_MSG = "Hello everyone! I’m online now 🤖"

SPOTIFY_CLIENT_ID = "1c21247d714244ddbb09925dac565aed"
SPOTIFY_CLIENT_SECRET = "709e1a2969664491b58200860623ef19"

SERVER_PLAYLIST_LIMIT = 50
PLAYLIST_FETCH_LIMIT = 100
SONG_DOWNLOAD_DURATION = 180
SONG_DOWNLOAD_DURATION_LIMIT = 2000

TG_AUDIO_FILESIZE_LIMIT = 104857600
TG_VIDEO_FILESIZE_LIMIT = 1073741824

# Sessions
STRING1 = "BQGbOzoAhG-dxyPz6hooGFhrmC2U_T5LNH-DV7SiFaHmaXbnDDhqg5Sticnf2Pi1FLktn0lrEeePxyIke64e8KJZThs8Mtc7Yx0eWDjRNdjkOeviRAVbYNP3dt6unOGtmzrvwB8gbV2vJevctK1U5rhj95ZiTAMtbCRAY0vWLt3mAyIdrPuXAjbclhJ72AWwkwx9W1Tbg2yk06xmzMSdqs43XX6Jnxf35GABkVPdx41nwAwMJemqjtIpnUnTH3TDnQu0RTbE2Uwvmlxp6C1LRLYESRsRS9Pkdrjeo1e3MfQP6Pto3-4pfkywhFlbVsnEbcDgo11k0Cy1ZC2WwqKVJdM8gQhwrwAAAAGsmbxnAA"
STRING2 = STRING3 = STRING4 = STRING5 = None

# Internal
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Image URLs
START_IMG_URL = "https://graph.org/file/121bc9e109f540a8befac-c19eeddc86e8f53bcf.jpg"
PING_IMG_URL = "https://telegra.ph/file/29bf663a3b91c7e0086bc.jpg"
PLAYLIST_IMG_URL = "https://telegra.ph/file/14eb59ea7d31229d8d751.jpg"
STATS_IMG_URL = "https://telegra.ph/file/2abd798099b17a5a9b2fb.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/590f5404cdc7840b63a1c.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/590f5404cdc7840b63a1c.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/982b01ba53c3d69b0d0ce.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/590f5404cdc7840b63a1c.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/5eb646ee0bf810113af22.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"

# Duration calc
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# URL check
if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - SUPPORT_CHANNEL must start with https://")

if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - SUPPORT_CHAT must start with https://")