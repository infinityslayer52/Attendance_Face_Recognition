import requests
import pprint

# initializing required variables
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
        groupName = input('Enter the name of the group whose students you wish to see.')
        params_get['faceListId'] = groupName
        # api call to display list of faces in specified list
        r = requests.get(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/facelists/{faceListId}', params=params_get, headers=headers_get)
        print('Students present in this group are- ')
        for face in range(0, len(r.json()['persistedFaces'])):
            pprint.pprint(r.json()['persistedFaces'][face]['userData'])
            # pprint.pprint(r.json()['persistedFaces'][face]['persistedFaceId'])
            c += 1
        print('Total number of students is ', c)
