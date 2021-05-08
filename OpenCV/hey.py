import cv2 as cv

#reading the image
img = cv.imread('NumberPlate_Swift.jpg')
cv.imshow('Original', img)
cv.waitKey(0)

#Resizing the image
resized = cv.resize(img, (500,500), interpolation = cv.INTER_AREA)
cv.imshow('Resized',resized)
cv.waitKey(0)

#Converting to grayscale
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
cv.waitKey(0)

#Noise filtering
gray = cv.bilateralFilter(gray,11,17,17)
cv.imshow('Smoother Image', gray)
cv.waitKey(0)

#Canny edge detection
edged = cv.Canny(gray, 170, 200)
cv.imshow('Edge Detection', edged)
cv.waitKey(0)

#Finding contours based on the images
cnts, new = cv.findContours(edged.copy(), cv.RETR_LIST,  cv.CHAIN_APPROX_SIMPLE)

#Creating a copy image to draw all contours
image1 = resized.copy()
cv.drawContours(image1, cnts, -1, (0,255,0), 3)
cv.imshow("Contouring",image1)
cv.waitKey(0)


cnts = sorted(cnts,key = cv.contourArea, reverse = True)[:10]
NumberPlateCount = None

image2 = resized.copy()
cv.drawContours(image2 , cnts, -1, (0,255,0), 3)
cv.imshow("Top 10 contours", image2)
cv.waitKey(0)


count = 0
name = 1

for i in cnts :
    perimeter = cv.arcLength(i, True)
    approx = cv.approxPolyDP(i, 0.02*perimeter, True)


    if (len(approx) == 4):
        NumberPlateCount = approx

        x,y,w,h = cv.boundingRect(i)
        crp_img = resized[y:y+h, x:x+w]

        cv.imwrite(str(name)+ '.jpg', crp_img)
        name += 1

        break
cv.drawContours(resized, [NumberPlateCount], -1, (0,255,0), 3)
cv.imshow("Final Image", resized)
cv.waitKey(0)

crp_img_loc = '1.jpg'
cv.imshow("Cropped image", cv.imread(crp_img_loc))
cv.waitKey(0)

