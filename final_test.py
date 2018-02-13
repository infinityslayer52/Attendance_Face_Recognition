import requests
import pprint
from toBinary import con64
import glob

#assign names to respective images
names={"01.jpeg":"1","02.jpeg":"2","03.jpeg":"3","04.jpeg":"4","05.jpeg":"5","06.jpeg":"6"}

#declare lists for identifying found faces
found=[]

#store location of image to be searched
photo_to_search='sample6.jpeg'
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
p=0
#importing images to be compared to and then comparing
print('Comparing found faces to known faces...')
for file in glob.glob("D:\Attendance_Face_Recog\known_images5\*.jpg"):
    img2=con64(file)
    params_detect['image_base64']=img2
    s = requests.post(url='https://api-us.faceplusplus.com/facepp/v3/detect',data=params_detect)
    params_compare['face_token1']=s.json()['faces'][0]['face_token']
    for face in range(0,len(r.json()['faces'])):
        p+=1
        params_compare['face_token2']=r.json()['faces'][face]['face_token']
        t=requests.post(url='https://api-us.faceplusplus.com/facepp/v3/compare',data=params_compare)
        if(t.json()['confidence']>90):
            found.append(names[file[-7:]])
            continue
print('Time taken- %d ms'%(p/10000))
print('Found-')
print(found,)
