import cv2
import face_recognition

# Load as RGB (face_recognition returns RGB)
imgElon = face_recognition.load_image_file('/home/asoliman/project/face_recog/images/elon.jpg')
imgTest = face_recognition.load_image_file('/home/asoliman/project/face_recog/images/elontest.jpg')

# Face locations/encodings (expects RGB)
faceLoc = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]

# Draw on copies converted to BGR for display
elon_disp = cv2.cvtColor(imgElon, cv2.COLOR_RGB2BGR)
test_disp = cv2.cvtColor(imgTest, cv2.COLOR_RGB2BGR)

cv2.rectangle(elon_disp, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)
cv2.rectangle(test_disp, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)
print(faceLoc)
print(faceLocTest)

# Finding the distance between the test image and the actual image
results = face_recognition.compare_faces([encodeElon], encodeTest)
faceDis = face_recognition.face_distance([encodeElon], encodeTest)
print(results, faceDis)
cv2.putText(test_disp, f'{results} {round(faceDis[0], 2)}', (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)

cv2.imshow('Elon Musk', elon_disp)
cv2.imshow('Elon Musk Test', test_disp)
cv2.waitKey(0)
cv2.destroyAllWindows()
