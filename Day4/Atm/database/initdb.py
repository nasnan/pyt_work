import json
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

from conf import settings


shooping_list = {
    "1": {"name":"book","price" : 50},
    "2": {"name": "phone", "price": 5000},
    "3": {"name": "bag", "price": 120},
    "4": {"name": "pen", "price": 20},
    "5": {"name": "mirror", "price": 25},
    "6": {"name": "glass", "price": 22},
    "7": {"name": "water", "price": 2}
}

user_list ={
    "Wa": {"pw" : "0922" ,"islocked" : 1},
    "Du": {"pw" : "0201" ,"islocked" : 0},
    "Yi": {"pw" : " 01" ,"islocked" : 0}
}

card_list = (
    {"id" : "101101", "owner" : "Du", "balance" : 3000, "line" : 2000 ,"isfrozen" : 0 },
    {"id" : "101232", "owner" : "Wa", "balance" : 5250, "line" : 3300 ,"isfrozen" : 0 },
    {"id" : "101232", "owner" : "Du", "balance" : 350, "line" : 100 ,"isfrozen" : 0 }
)


def init(dbname,dblist):
    with open(dbname,'w+')as f:
        json.dump(dblist,f)


init('shoopinglist.db',shooping_list)
init('userlist.db',user_list)
init('cardlist.db',card_list)