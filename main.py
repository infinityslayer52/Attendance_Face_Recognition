import create_facelist
import delete_facelist
import get_facelist
import add_facestolist
import delete_face
import search_infacelists
import add_facetolist

print('1. Create a group.')
print('2. Add multiple students to a group from a folder.')
print('3. Add a single student from a file.')
print('4. Display list of students in a group.')
print('5. Mark attendance for a group from a photo.')
print('6. Delete a student from a group.')
print('7. Delete a group.')
n = True
while n:
    try:
        x = input('Choose a valid option')
        if x == '1':
            create_facelist.create()
        elif x == '2':
            add_facestolist.add_faces()
        elif x == '3':
            add_facetolist.add()
        elif x == '4':
            get_facelist.listed()
        elif x == '5':
            search_infacelists.search()
        elif x == '6':
            delete_face.delete()
        elif x == '7':
            delete_facelist.delete()
        else:
            print('Please enter a valid option.')
    except Exception as e:
        print(e)
    r = input('Do you want to perform another task?(y/n)')
    if r == 'n' or r == 'N':
        n = False
        print('Exiting...')
    elif r == 'y' or r == 'Y':
        continue
    else:
        n = False
        print('Exiting...')
