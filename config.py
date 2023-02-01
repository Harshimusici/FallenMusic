from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID, "15418866")
API_HASH = getenv("API_HASH, "dbbf679a4b429fab1bfea0b52b8f9be8")

BOT_TOKEN = getenv("BOT_TOKEN", "6084181200:AAFIVRN_RmXsxhWr_y7YWP73U-o9VqdQuRs")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID, "5842502218"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/1b554ae6a8b68e7c2eafd.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/1b554ae6a8b68e7c2eafd.jpg")

SESSION = getenv("SESSION", "BQDrRfIAirlP0fL7CQdXc0gt6z8zEwoLfUmbo38NVJxOB8Jti64ydGyeGV-42bc6JHr-BdBnavESFitnZYqk1OfZWAoAg-RWPKjz2SUmS7WvvvM0PleZo0j01cMHkxMhkAD9F-1yjnH5TE55asU9-WtfwcDISdLgaucZGIseuOg20PSCn5R3WhymIffISLYkgRyZ1MvY1DOV6dwYs8U1_hbnvzU9YcPv4Q5S6m96q6Rp1eADx5-rAhQ9cQf4Q95IRU8NLKlvtPj7w8bojl16JdcABnzF0lxd_q7gXxcLLMKlJT3_yVxh8d3A9B09_WLcke2mamxrsSMV9Glhkv162lST4CsF9gAAAAFfhezDAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/chatting_gruap")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/chatting_gruap")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5842502218").split()))


FAILED = "https://te.legra.ph/file/1b554ae6a8b68e7c2eafd.jpg"
