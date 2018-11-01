import pymysql.cursors
import json
from DBConnector import DBConnector

# Connect to the database
dbconnector = DBConnector('localhost','root','','gerrit_test')

requests = dbconnector.requests()
request_detail = dbconnector.request_detail()

def search(req_id):
    for p in request_detail:
        if p['request_id'] == req_id:
            return p

finalJSON = {}

for row in requests:
    finalJSON["request_id"] = {
        "change_id" : search(row)
    }

    # print(row["request_id"])
     

y = json.dumps(finalJSON)
print(y)
# print(requests[0][0])


