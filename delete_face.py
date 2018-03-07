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
        groupname = input('Enter the name of the group from which a student has to be deleted')
        x = 0
        for i in range(0, len(t.json())):
            if groupname == t.json()[i]['faceListId']:
                x = 1
                break
            else:
                continue
        if x == 1:
            params_delete['faceListId'] = groupname
            params_get['faceListId'] = groupname
            r = requests.get(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/facelists/{faceListId}', params=params_get, headers=headers_get)
            # pprint.pprint(r)
            if len(r.json()['persistedFaces']) == 0:
                print('No students present in this group.')
            else:
                print('The students present in this group are- ')
                for face in range(0, len(r.json()['persistedFaces'])):
                    pprint.pprint(r.json()['persistedFaces'][face]['userData'])
                faceid = input('Enter the name of the student who has to be deleted from this list')
                for face in range(0, len(r.json()['persistedFaces'])):
                    if faceid == r.json()['persistedFaces'][face]['userData']:
                        params_delete['persistedFaceId'] = r.json()['persistedFaces'][face]['persistedFaceId']
                        s = requests.delete(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/facelists/{faceListId}/persistedFaces/{persistedFaceId}', params=params_delete, headers=headers_delete)
                        # pprint.pprint(s)
                        if int(s.status_code) == 200:
                            print(faceid, ' was deleted from the group ', groupname)
                        else:
                            print(faceid, ' was not Deleted. Error-', r.status_code)
        else:
            print("The group name that you entered was not found. PLease enter a valid group name.")
            delete()
