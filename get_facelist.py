import requests
import pprint

#initializing required variables
faceListId='class_1'
c=0

params_get={
    'faceListId':faceListId
}

headers_get={
    'Ocp-Apim-Subscription-Key':'1a35269c87e5479ab6ed638399b5a449'
}

#api call to display list of faces in specified list
r=requests.get(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/facelists/{faceListId}',params=params_get,headers=headers_get)
print('Faces present in this list are- ')
for face in range(0,len(r.json()['persistedFaces'])):
    pprint.pprint(r.json()['persistedFaces'][face]['userData'])
    c+=1

print('Total number of faces is ',c)
