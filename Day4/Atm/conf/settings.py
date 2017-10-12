import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)



DB_DIR = os.path.join(BASE_DIR,'database')

RP_DIR = os.path.join(BASE_DIR,'report')