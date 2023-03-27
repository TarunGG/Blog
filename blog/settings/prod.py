from .base import *
import dj_database_url
import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    "database":dj_database_url(os.environ.get("DATABASE_URL"))
}

DEBUG = False
ADMIN_ENABLE = False