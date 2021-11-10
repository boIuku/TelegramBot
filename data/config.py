import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = "2125978238:AAGqBYxgm6k2d5Ue4soUkX0j9638NlJ4Z2Y"
admins = [
    362089194
]

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
