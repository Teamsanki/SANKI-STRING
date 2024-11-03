from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", 24740695))
API_HASH = getenv("API_HASH", 'a95990848f2b93b8131a4a7491d97092')

BOT_TOKEN = getenv("BOT_TOKEN", '8197260139:AAF3RWmRhUYo4GgYRqERMT_s-9Qc_3ApuiM')
MONGO_DB_URI = getenv("MONGO_DB_URI", 'mongodb+srv://Mrdaxx123:Mrdaxx123@cluster0.q1da65h.mongodb.net/?retryWrites=true&w=majority')

OWNER_ID = int(getenv("OWNER_ID", '7759282826'))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", 'https://t.me/ABOUT_VIP_STRANGER')
