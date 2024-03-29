import os

API_ID = API_ID = 25046127

API_HASH = os.environ.get("API_HASH", "b98e578e8b500c77c6a80839dfbdc4a5")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6715527106:AAHSeA8pNVja245YkLWn1wNJWxdHeFiuyww")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6222170405))

LOG = -1002102444164

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6222170405").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


