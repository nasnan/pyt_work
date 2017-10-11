import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from database import dbapi
from conf import settings

db_dir = os.path.join(settings.DB_DIR,'shoopinglist.db')

shop_list = dbapi.load_data_from_db(db_dir)

a = shop_list
print(a['1']['price'])
