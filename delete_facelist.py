import requests
import pprint

params_delete = {
    'faceListId': ''
}

headers_delete = {
    'Ocp-Apim-Subscription-Key': '1a35269c87e5479ab6ed638399b5a449'
}

headers_getlist = {
    'Ocp-Apim-Subscription-Key': '1a35269c87e5479ab6ed638399b5a449'
}


def delete():
    s = requests.get(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/facelists', headers=headers_getlist)
    if len(s.json()) == 0:
        print('No groups found.')
    else:
        print('List of groups are as follows- ')
        for lists in range(0, len(s.json())):
            pprint.pprint(s.json()[lists]['faceListId'])
        groupname = input('Enter the name of the group you want to delete.')
        x = 0
        for i in range(0, len(s.json())):
            if groupname == s.json()[i]['faceListId']:
                x = 1
                break
            else:
                continue
        if x == 1:
            params_delete['faceListId'] = groupname
            r = requests.delete(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/facelists/{faceListId}', headers=headers_delete, params=params_delete)
            # pprint.pprint(r.status_code)
            if int(r.status_code) == 200:
                print('Group named ', groupname, ' deleted')
            else:
                print('Group not deleted. Error-', r.status_code)
        else:
            print("The group name that you entered was not found. PLease enter a valid group name.")
            delete()
