import requests
import pprint
from toBinary import con64
import glob

#assign names to respective images
names={"01.jpg":"1","02.jpg":"2","03.jpg":"3","04.jpg":"4","05.jpg":"5","06.jpg":"6","07.jpg":"7","08.jpg":"8","09.jpg":"9",
       "10.jpg":"10","11.jpg":"11","12.jpg":"12","13.jpg":"13","14.jpg":"14","15.jpg":"15","16.jpg":"16","17.jpg":"17","18.jpg":"18",
       "19.jpg":"19","20.jpg":"20","21.jpg":"21","22.jpg":"22","23.jpg":"23","24.jpg":"24","25.jpg":"25","26.jpg":"26","27.jpg":"27"}

#declare lists for identifying found faces
found=[]

#store location of image to be searched
photo_to_search='sample.jpg'
img1=con64(photo_to_search)

#initializing parameters for api call
params_detect={
    'api_key':'gozbsSP1fxqNSS5YjcFM7qckjKch1tBB',
    'api_secret':'HklHJCzfO87YyIC9DudGArVKJyioEhbO',
    'image_base64':img1
}
params_compare={
    'api_key':'gozbsSP1fxqNSS5YjcFM7qckjKch1tBB',
    'api_secret':'HklHJCzfO87YyIC9DudGArVKJyioEhbO',
    'face_token1':'',
    'face_token2':''
}

#api call to find faces
c=0
print('Finding faces in group photo...')
r = requests.post(url='https://api-us.faceplusplus.com/facepp/v3/detect',data=params_detect)
for face in range(0,len(r.json()['faces'])):
    #pprint.pprint(r.json()['faces'][face]['face_token'])
    c+=1
print('Found %d faces.'%c)

#importing images to be compared to and then comparing
print('Comparing found faces to known faces...')
for file in glob.glob("D:\Attendance_Face_Recog\known_images\*.jpg"):
    img2=con64(file)
    params_detect['image_base64']=img2
    s = requests.post(url='https://api-us.faceplusplus.com/facepp/v3/detect',data=params_detect)
    params_compare['face_token1']=s.json()['faces'][0]['face_token']
    for face in range(0,len(r.json()['faces'])):
        params_compare['face_token2']=r.json()['faces'][face]['face_token']
        t=requests.post(url='https://api-us.faceplusplus.com/facepp/v3/compare',data=params_compare)
        if(t.json()['confidence']>90):
            found.append(names[file[-6:]])
            continue

print('Found-')
print(found,)
