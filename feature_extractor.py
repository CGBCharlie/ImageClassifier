import cv2 
from PIL import Image
from collections import Counter
import csv
import os

def showImage(image) :  
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# ****************** Features ******************
def getContrast(img):
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    mean = cv2.mean(grayImg)[0]
    std_dev = cv2.meanStdDev(grayImg)[1][0][0]

    contrast = 1
    if std_dev == 0:
        if mean == 255.0:
            contrast = 0
    else:
        contrast = std_dev / mean
    return contrast

def getBrightness(img):
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    mean = cv2.mean(grayImg)[0]
    brightness = mean / 255.0
    return brightness

def getSaturation(img):
    hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    h, s, v = cv2.split(hsvImg)
    mean = cv2.mean(s)[0]
    saturation = mean / 255.0
    return saturation

def mostRepeatedColors(img):
    val = list(img.getdata())
    val = Counter(val)
    mc = val.most_common(5)
    cc = [p[0] for p in mc]
    return cc

def getHue(img):
    hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    h, s, v = cv2.split(hsvImg)
    mean = cv2.mean(h)[0]
    return mean / 255.0


# ****************** Main ******************
def main():
    directories = ['Images/cats', 'Images/ducks', 'Images/pandas']
    e = open('features.csv', 'w')
    writer = csv.writer(e)
    writer.writerow(['      ', 'Contrast', 'Brightness', 'Saturation', 'Hue', 'Repeated Colors'])
    for directory in directories:
        for filename in sorted(os.listdir(directory), key=len):
            print(filename)
            f = os.path.join(directory, filename)
            if os.path.isfile(f):
                image = cv2.imread(f)
                writer.writerow(['{}'.format(f.split(".")[0]), getContrast(image), getBrightness(image), getSaturation(image), getHue(image),mostRepeatedColors(Image.open(f))])

if __name__ == "__main__":
    main()