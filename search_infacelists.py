import requests
import pprint

# initializing required variables
# img='./samples/sample1.jpg'

headers_search = {
    'Ocp-Apim-Subscription-Key': '1a35269c87e5479ab6ed638399b5a449'
}

body_search = {
    'faceId': '',
    'faceListId': '',
    'maxNumOfCandidatesReturned': 1
}

headers_detect = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '1a35269c87e5479ab6ed638399b5a449'
}

params_get = {
    'faceListId': ''
}

headers_get = {
    'Ocp-Apim-Subscription-Key': '1a35269c87e5479ab6ed638399b5a449'
}

headers_getlist = {
    'Ocp-Apim-Subscription-Key': '1a35269c87e5479ab6ed638399b5a449'
}


def search():
    found = []
    u = requests.get(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/facelists', headers=headers_getlist)
    for lists in range(0, len(u.json())):
        pprint.pprint(u.json()[lists]['faceListId'])
    groupName = input('Enter the name of the group for which attendance has to be marked.')
    body_search['faceListId'] = groupName
    params_get['faceListId'] = groupName
    img = input('Enter the location of the image taken during attendance.')
    # searching and mapping found faces
    t = requests.get(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/facelists/{faceListId}', params=params_get, headers=headers_get)
    # pprint.pprint(t.json()['persistedFaces'])
    img = open(img, 'rb').read()
    r = requests.post(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect', headers=headers_detect, data=img)
    # pprint.pprint(r.json())
    for face in range(0, len(r.json())):
        body_search['faceId'] = r.json()[face]['faceId']
        s = requests.post(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/findsimilars', headers=headers_search, json=body_search)
        # pprint.pprint(s.json())
        if s.json() == []:
            continue
        elif s.json()[0]['confidence'] > 0.85:
            f = s.json()[0]['persistedFaceId']
            for faces in range(0, len(t.json()['persistedFaces'])):
                if f == t.json()['persistedFaces'][faces]['persistedFaceId']:
                    found.append(t.json()['persistedFaces'][faces]['userData'])
                    break

    found.sort(key=int)
    print('The student who were present in the class were-')
    print(found)
