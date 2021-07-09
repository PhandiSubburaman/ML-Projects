import sys
import pandas as pd
import pymongo
import json
import os
from watchdog.events import RegexMatchingEventHandler


def import_content(filepath):
    mng_client = pymongo.MongoClient('localhost', 27017)
    mng_db = mng_client['stearnsDB']
    collection_name = 'sfaccounts'
    db_cm = mng_db[collection_name]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)
    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json)

if __name__ == "__main__":
  filepath = "sf_accounts_report1609036148677.csv"
  import_content(filepath)


# class ImagesEventHandler(RegexMatchingEventHandler):
# 	mng_client = pymongo.MongoClient('localhost', 27017)
#     mng_db = mng_client['stearnsDB']
#     collection_name = 'sfaccounts'
#     db_cm = mng_db[collection_name]
#     cdir = os.path.dirname(__file__)
#     file_res = os.path.join(cdir, filepath)

#     data = pd.read_csv(file_res)
#     data_json = json.loads(data.to_json(orient='records'))
#     db_cm.remove()
#     db_cm.insert(data_json)