from .base import *
import dj_database_url
import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
    
}

DEBUG = False
ADMIN_ENABLE = False

ALLOWED_HOSTS = ['*']