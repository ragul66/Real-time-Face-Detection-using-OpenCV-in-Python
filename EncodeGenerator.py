import cv2
import face_recognition
import os
import numpy as np
import pickle

folderModePath = 'Images'
PathList = os.listdir(folderModePath)
print(PathList)

imgList = []
studentIds = []

for path in PathList:
    img_path = os.path.join(folderModePath, path)
    img = cv2.imread(img_path)
    if img is None:
        print(f"Error loading image: {img_path}")
    else:
        print(f"Loaded {img_path} with shape {img.shape} and dtype {img.dtype}")
        # Convert to grayscale and back to RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgList.append(img)
        studentIds.append(os.path.splitext(path)[0])

print(studentIds)

def findEncodings(imgList):
    encodeList = []
    for img in imgList:
        try:
            print(f"Converted image shape: {img.shape} and dtype: {img.dtype}")
            encodings = face_recognition.face_encodings(img)
            if encodings:
                encodeList.append(encodings[0])
            else:
                print("No faces found in the image.")
        except Exception as e:
            print(f"Error encoding image: {e}")
    return encodeList

print("Encoding Starts ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print(encodeListKnown)
print("Encoding Complete")


file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")
