import pymysql.cursors
import json
from DBConnector import DBConnector

# Connect to the database
dbconnector = DBConnector('localhost','root','','gerrit_test')

p = dbconnector.inline_comments()
print(p)

# def search(req_id):
#     for p in request_detail:
#         if p['request_id'] == req_id:
#             return p


#     finalJSON = {}

#     for row in requests:
#         finalJSON["request_id"] = {
#             "change_id" : search(row["request_id"])
#         } 

#     y = json.dumps(finalJSON)
#     print(y)



