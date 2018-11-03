import pymysql.cursors
import json
from DBConnector import DBConnector

# Connect to the database
dbconnector = DBConnector('localhost','root','','gerrit_test')

requests = dbconnector.requests()
request_details = dbconnector.request_detail()

def search(req_id):
    for p in request_details:
        if p['request_id'] == req_id:
            return p

def MakeRequestDict(req_id):
    for request_detail in request_details:
        if request_detail["request_id"] == req_id:
            return {'change_id': request_detail["change_id"]}

finalJSON = []

for request in requests:
    dict = MakeRequestDict(request["request_id"])
    finalJSON.append({request["request_id"]: dict}) 





y = json.dumps(finalJSON)
print(y)
# print(requests[0][0])


