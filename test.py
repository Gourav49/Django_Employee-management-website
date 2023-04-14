import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT= 'api/'
# def get_resource(id):
#     resp=requests.get(BASE_URL+ENDPOINT+id+'/')
#     print(resp.status_code)
#     print(resp.json())
# #id=input("Enter any Id:")
# #get_resource(id)

# def get_resource(id=None):
#     data={}
#     if id is not None:
#         data={
#         'id':id
#         }
#     resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# id=input("Enter any Id:")
# get_resource(id)

# def get_all():
#     resp=requests.get(BASE_URL+ENDPOINT)
#     print(resp.status_code)
#     print(resp.json())
# #get_all()
#
# def create_resource():
#     new_emp={
#     'eno':800,
#     'ename': 'kamina',
#     'esal': 80000,
#     'eaddr': 'Ranchi'
#     }
#     resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# create_resource()
# def update_resource(id):
#     new_emp={
#     'eno':700,
#     'ename':'Sonu',
#     'eaddr':'Banglore'
#     }
#     resp=requests.put(BASE_URL+ENDPOINT+str(id)+'/',data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# #update_resource(6)
#
# def update_resource(id):
#     new_emp={
#     'id':id,
#     'eno':700,
#     'ename':'Maglu',
#     'eaddr':'Banglore'
#     }
#     resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# update_resource(9)


def delete_resource(id):
    data={}
    data={
    'id':id
    }
    resp=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
delete_resource(9)
