import requests
import pprint

params_delete = {
    'faceListId': '',
    'persistedFaceId': ''
}

headers_delete = {
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


def delete():
    t = requests.get(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/facelists', headers=headers_getlist)
    if len(t.json()) == 0:
        print('No groups found.')
    else:
        print('The groups are as follows-')
        for lists in range(0, len(t.json())):
            pprint.pprint(t.json()[lists]['faceListId'])
        groupName = input('Enter the name of the group from which a student has to be deleted')
        params_delete['faceListId'] = groupName
        params_get['faceListId'] = groupName
        r = requests.get(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/facelists/{faceListId}', params=params_get, headers=headers_get)
        # pprint.pprint(r)
        if len(r.json()['persistedFaces']) == 0:
            print('No students present in this group.')
        else:
            print('The students present in this group are- ')
            for face in range(0, len(r.json()['persistedFaces'])):
                pprint.pprint(r.json()['persistedFaces'][face]['userData'])
            faceId = input('Enter the name of the student who has to be deleted from this list')
            for face in range(0,len(r.json()['persistedFaces'])):
                if faceId == r.json()['persistedFaces'][face]['userData']:
                    params_delete['persistedFaceId'] = r.json()['persistedFaces'][face]['persistedFaceId']
                    s = requests.delete(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/facelists/{faceListId}/persistedFaces/{persistedFaceId}', params=params_delete, headers=headers_delete)
                    # pprint.pprint(s)
                    if int(s.status_code) == 200:
                        print(faceId, ' was deleted from the group ', groupName)
                    else:
                        print(faceId, ' was not Deleted. Error-', r.status_code)
                    break
