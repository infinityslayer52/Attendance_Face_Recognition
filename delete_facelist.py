import requests
import pprint

#initializing required variables
params_delete={
    'faceListId':'class_1'
}

headers_delete={
    'Ocp-Apim-Subscription-Key':'1a35269c87e5479ab6ed638399b5a449'
}

#api call to delete face list
r=requests.delete(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/facelists/{faceListId}',headers=headers_delete,params=params_delete)
#pprint.pprint(r.status_code)
if(int(r.status_code)==200):
    print('Face List Deleted')
else:
    print('Face List not Deleted. Error-',(r.status_code))
