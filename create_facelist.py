import requests
import pprint

params_create = {
    'faceListId': ''
}

headers_create = {
    'Ocp-Apim-Subscription-Key': '1a35269c87e5479ab6ed638399b5a449'
}

body_create = {
    'name': ''
}


def create():
    print('Enter the name of the group')
    groupName = input('Note- Name of the group should be in small letters and should not contain spaces. Hyphens and underscores are allowed.')
    params_create['faceListId'] = groupName
    body_create['name'] = groupName
    r = requests.put(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/facelists/{faceListId}', json=body_create, headers=headers_create, params=params_create)
    # pprint.pprint(r.status_code)
    if int(r.status_code) == 200:
        print('Group named ', groupName, ' created.')
    else:
        print('Group not Created. Error-', r.status_code)
