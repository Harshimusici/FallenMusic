from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID, "15418866"))
API_HASH = getenv("API_HASH, "dbbf679a4b429fab1bfea0b52b8f9be8")

BOT_TOKEN = getenv("BOT_TOKEN", "6084181200:AAFIVRN_RmXsxhWr_y7YWP73U-o9VqdQuRs")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID, "5842502218"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/1b554ae6a8b68e7c2eafd.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/1b554ae6a8b68e7c2eafd.jpg")

SESSION = getenv("SESSION", "BQDrRfIAIqXoFPBp-VszfbumgbfjaiR4dKglrq4mA57LlzL30w1OE8H33spBD6zVk3ZSVsPFsovqjV-5Hv7jdeynL7EYSP4D6LApMGM8nWTTjIykls-rDy5DXWU91fX9pYIiBu3ML2yAstDGVzBVOiCFgVYy-IUFTbCx1aRvMToKEOOzkygTItU2B44a85nh9bYoUQ7R3hscpS43slqHcHLUSsWSUYGGIHDN8pOJVXWg_Svl1RvGJ_rnsYkDf-f2DeV9KRb1HIqzwtZ6p2AyKhisHYY_PNqfHUgvRMe3_GcQOeVhYwRwVn3zXzEFvZ7GRcWN6QFc7IFkHU9caGmYPMMQ-HWFTAAAAAFfhezDAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/chatting_gruap")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/chatting_gruap")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5842502218").split()))


FAILED = "https://te.legra.ph/file/1b554ae6a8b68e7c2eafd.jpg"
