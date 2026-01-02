import os

class Config(object):
    BOT_TOKEN = os.environ.get("8225118430:AAEOFTRcVH3Au1LR0iFyasUb4U5CGATuoT4")
    API_ID = int(os.environ.get("22447622"))
    API_HASH = os.environ.get("543b62d58d3e723e766ba57a984ab65d")
    VIP_USER = os.environ.get('VIP_USERS', '').split(',')
    VIP_USERS = [int() for user_id in VIP_USER]
