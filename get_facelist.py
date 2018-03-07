import requests
import pprint

params_get = {
    'faceListId': ''
}

headers_get = {
    'Ocp-Apim-Subscription-Key': '1a35269c87e5479ab6ed638399b5a449'
}

headers_getlist = {
    'Ocp-Apim-Subscription-Key': '1a35269c87e5479ab6ed638399b5a449'
}


def listed():
    c = 0
    s = requests.get(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/facelists', headers=headers_getlist)
    if len(s.json()) == 0:
        print('No groups found.')
    else:
        print('The groups are as follows-')
        for lists in range(0, len(s.json())):
            pprint.pprint(s.json()[lists]['faceListId'])
        groupname = input('Enter the name of the group whose students you wish to see.')
        x = 0
        for i in range(0, len(s.json())):
            if groupname == s.json()[i]['faceListId']:
                x = 1
                break
            else:
                continue
        if x == 1:
            params_get['faceListId'] = groupname
            r = requests.get(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/facelists/{faceListId}', params=params_get, headers=headers_get)
            print('Students present in this group are- ')
            for face in range(0, len(r.json()['persistedFaces'])):
                pprint.pprint(r.json()['persistedFaces'][face]['userData'])
                # pprint.pprint(r.json()['persistedFaces'][face]['persistedFaceId'])
                c += 1
            print('Total number of students is ', c)
        else:
            print("The group name that you entered was not found. PLease enter a valid group name.")
            listed()
