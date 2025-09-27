import logging 
from os import environ, path, remove
from sys import exit
from pyrogram import Client 
from pyromod import listen

if path.exists('log.txt'):
    remove('log.txt')
    
logging.basicConfig(filename='log.txt', level=logging.INFO)
LOG = logging.getLogger("AutoPahe")
LOG.setLevel(level=logging.INFO)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}

API_ID = int(environ.get('26356837', 45647)) #API ID
API_HASH = environ.get('67149e16a6f1c2f7f21549802f59d3ec', 'Your Api Id') #API HASH
BOT_TOKEN = environ.get('8179038680:AAEZnsLYPVnYX04T1rPf3qrl2l5kZ9I55Rk', 'Your Bot Token') #BOT TOKEN
DATABASE_URL = environ.get('mongodb+srv://<sensheela02_db_user>:<ufX47rNdBjIEy3sj>@cluster0.ohudpmn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0', 'Your MongoDb') #MONGO DB
OWNER_ID = int(environ.get('5473837554,7805758243', None)) #OWNER ID
MAIN_CHANNEL = int(environ.get('-1003089588137', None))#YOUR MAIN CHANNEL ID
ARCHIVE_CHANNEL = int(environ.get('-1003145184142', None))#YOUR ARCHIVE CHANNEL
MESSAGE_ID = int(environ.get('-1003145184142', None)) #SUB CHANNEL STATUS ID

soheru = Client('SoheruBots', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
