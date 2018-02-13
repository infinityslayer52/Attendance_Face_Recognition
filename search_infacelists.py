import requests
import pprint

#initializing required variables
faceListId='class_1'
img='./samples/sample6.jpg'
found=[]

headers_search={
    'Ocp-Apim-Subscription-Key':'1a35269c87e5479ab6ed638399b5a449'
}

body_search={
    'faceId':'',
    'faceListId':faceListId,
    'maxNumOfCandidatesReturned':1
}

headers_detect={
    'Content-Type':'application/octet-stream',
    'Ocp-Apim-Subscription-Key':'1a35269c87e5479ab6ed638399b5a449'
}

params_get={
    'faceListId':faceListId
}

headers_get={
    'Ocp-Apim-Subscription-Key':'1a35269c87e5479ab6ed638399b5a449'
}

#searching and mapping found faces
t=requests.get(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/facelists/{faceListId}',params=params_get,headers=headers_get)
#pprint.pprint(t.json()['persistedFaces'])
img=open(img,'rb').read()
r=requests.post(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect',headers=headers_detect,data=img)
#pprint.pprint(r.json())
for face in range(0,len(r.json())):
    body_search['faceId']=r.json()[face]['faceId']
    s=requests.post(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/findsimilars',headers=headers_search,json=body_search)
    #pprint.pprint(s.json())
    if(s.json()==[]):
        continue
    elif(s.json()[0]['confidence']>0.85):
        f=s.json()[0]['persistedFaceId']
        for face in range(0,len(t.json()['persistedFaces'])):
            if(f==t.json()['persistedFaces'][face]['persistedFaceId']):
                found.append(t.json()['persistedFaces'][face]['userData'])
                break

print(found)

