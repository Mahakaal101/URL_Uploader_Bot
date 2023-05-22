import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("BOT_TOKEN", "5699760927:AAFPVcL8t12eLfpe_4dcg-vH6X6Hj84u6FE") # Make a bot from https://t.me/BotFather and enter the token here
    
    APP_ID = int(os.environ.get("API_ID", 22710277)) # Get this value from https://my.telegram.org/apps
    
    API_HASH = os.environ.get("API_HASH", "723eb90b39789f313564d51da18b2182") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(os.environ.get("OWNER_ID", 5791145987)) # Your(owner's) telegram id
    
    MONGO_STR = os.environ.get("MONGO_STR", "mongodb+srv://W9Uyj61afEXSw601:W9Uyj61afEXSw601@cluster0.zsxso.mongodb.net/?retryWrites=true&w=majority") # Get from MongoDB Atlas

    DOWNLOAD_LOCATION = "app//DOWNLOADS//" # The download location for users. (Don't change anything in this field!)
