import os
from os import path, getenv
from dotenv import load_dotenv

if path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()

class PrinceX(object):
        admins = {}
        BOT_TOKEN = getenv("BOT_TOKEN", None)
        CHANNEL = int(os.getenv('CHANNEL', -1001246426926))
        API_ID = int(getenv("API_ID", "1234567"))
        API_HASH = getenv("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
        SESSION_NAME = getenv("SESSION_NAME", None)
        DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
        SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1994755645").split()))
        ASSISTANT_NAME = getenv("ASSISTANT_NAME", "PrinceX_VideoAssistant")
        BOT_USERNAME = getenv("BOT_USERNAME", "PrinceX_VideoBot")
        COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
