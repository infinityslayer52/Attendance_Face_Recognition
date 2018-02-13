import requests
import pprint

faceListId='class_1'
faceId='4'
params_delete={
    'faceListId':faceListId,
    'persistedFaceId':''
}

headers_delete={
    'Ocp-Apim-Subscription-Key':'1a35269c87e5479ab6ed638399b5a449'
}

params_get={
    'faceListId':faceListId
}

headers_get={
    'Ocp-Apim-Subscription-Key':'1a35269c87e5479ab6ed638399b5a449'
}

r=requests.get(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/facelists/{faceListId}',params=params_get,headers=headers_get)
#pprint.pprint(r)
for face in range(0,len(r.json()['persistedFaces'])):
    if(faceId==r.json()['persistedFaces'][face]['userData']):
        params_delete['persistedFaceId']=r.json()['persistedFaces'][face]['persistedFaceId']
        s=requests.delete(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/facelists/{faceListId}/persistedFaces/{persistedFaceId}',params=params_delete,headers=headers_delete)
        #pprint.pprint(s)
        if(int(r.status_code)==200):
            print(faceId,' Face Deleted')
        else:
            print(faceId,' Face not Deleted. Error-',(r.status_code))
        break

