import glob
import requests
import pprint

# initializing required variables
# directory='.\known_images\known_images1'

names = {"01.jpg": "1", "02.jpg": "2", "03.jpg": "3", "04.jpg": "4", "05.jpg": "5", "06.jpg": "6", "07.jpg": "7",
         "08.jpg": "8", "09.jpg": "9",
         "10.jpg": "10", "11.jpg": "11", "12.jpg": "12", "13.jpg": "13", "14.jpg": "14", "15.jpg": "15", "16.jpg": "16",
         "17.jpg": "17", "18.jpg": "18",
         "19.jpg": "19", "20.jpg": "20", "21.jpg": "21", "22.jpg": "22", "23.jpg": "23", "24.jpg": "24", "25.jpg": "25",
         "26.jpg": "26", "27.jpg": "27"}

params_add = {
    'faceListId': ''
}

headers_add = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '1a35269c87e5479ab6ed638399b5a449'
}

headers_getlist = {
    'Ocp-Apim-Subscription-Key': '1a35269c87e5479ab6ed638399b5a449'
}


def add_faces():
    c = 0
    s = requests.get(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/facelists', headers=headers_getlist)
    if len(s.json()) == 0:
        print('No groups found.')
    else:
        print('The groups are as follows-')
        for lists in range(0, len(s.json())):
            pprint.pprint(s.json()[lists]['faceListId'])
        groupName = input('Enter the name of the group to which the students have to be added')
        params_add['faceListId'] = groupName
        directory = input('Enter the directory of the source folder containing the photos of the students')
        directory += '\*jpg'
        for file in glob.glob(directory):
            img = open(file, 'rb').read()
            params_add['userData'] = names[file[-6:]]
            r = requests.post(url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/facelists/{faceListId}/persistedFaces', params=params_add, data=img, headers=headers_add)
            # pprint.pprint(r.json())
            c += 1
        print(c, ' students added to ', groupName)
