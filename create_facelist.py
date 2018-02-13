import requests
import pprint

#initializing required variables
name='class_1'
userData='Class 1'
faceListId='class_1'

params_create={
    'faceListId':faceListId
}

headers_create={
    'Ocp-Apim-Subscription-Key':'1a35269c87e5479ab6ed638399b5a449'
}

body_create={
    'name':name,
    'userData':userData
}

#api call to create face list
r=requests.put(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/facelists/{faceListId}',json=body_create,headers=headers_create,params=params_create)
#pprint.pprint(r.status_code)
if(int(r.status_code)==200):
    print('Face List Created')
else:
    print('Face List not Created. Error-',(r.status_code))
