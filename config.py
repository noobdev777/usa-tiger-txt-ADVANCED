import os

API_ID = API_ID = 26993820

API_HASH = os.environ.get("API_HASH", "3f233d7b9fedd96b09f92b1c5ab51e92")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7106503206:AAHBQUSfO05EcBxgQthLz3AaqyJuV2-3sG0")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6428889750))

LOG = -1002071495284

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6428889750").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


