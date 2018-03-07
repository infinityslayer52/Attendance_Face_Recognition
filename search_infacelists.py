import requests
import pprint

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
    groupname = input('Enter the name of the group for which attendance has to be marked.')
    x = 0
    for i in range(0, len(u.json())):
        if groupname == u.json()[i]['faceListId']:
            x = 1
            break
        else:
            continue
    if x == 1:
        body_search['faceListId'] = groupname
        params_get['faceListId'] = groupname
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
            pprint.pprint(s.json())
            if not s.json():
                continue
            elif s.json()[0]['confidence'] > 0.5:
                f = s.json()[0]['persistedFaceId']
                for faces in range(0, len(t.json()['persistedFaces'])):
                    if f == t.json()['persistedFaces'][faces]['persistedFaceId']:
                        found.append(t.json()['persistedFaces'][faces]['userData'])
                        break
        print('The students who were present in the class were-')
        '''
        r = sorted(found, key=lambda item: (int(item.partition(' ')[0])
                                           if item[0].isdigit() else float('inf'), item))
        print(', '.join(r))
        '''
        print(found)
    else:
        print("The group name that you entered was not found. PLease enter a valid group name.")
        search()
