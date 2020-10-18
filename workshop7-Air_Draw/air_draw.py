import cv2 #imports
import numpy as np
import time

x_pos, y_pos, point_selected = 0, 0, False #Setting global variables

def starting_point(event, x_clicked, y_clicked, flag, param):
    global x_pos, y_pos, point_selected #getting global variabels
    if event == cv2.EVENT_LBUTTONDOWN:
        x_pos = x_clicked #Updating variables at clicked location
        y_pos = y_clicked
        point_selected = True

cv2.namedWindow('enter_point') #Linking window and function to left click action
cv2.setMouseCallback('enter_point', starting_point)

cap = cv2.VideoCapture(0) #Starting video capture

while True:
    _, pre_img = cap.read() 
    pre_img = cv2.flip(pre_img, 1) #Flip image
    gray_pre_img = cv2.cvtColor(pre_img, cv2.COLOR_BGR2GRAY) #Conver to gray for algorithm used
    
    cv2.imshow("enter_point", pre_img)
    if point_selected == True or cv2.waitKey(1) == 27:
        
        cv2.destroyAllWindows()
        break

#Setting up format of points
old_pts = np.array([[x_pos, y_pos]], dtype=np.float32)
mask = np.zeros_like(pre_img) #Set black mask

time_end = time.time() + 5 # 5 second timer

while time.time() < time_end:
    _, inp_img = cap.read()
    inp_img = cv2.flip(inp_img, 1)
    gray_inp_img = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)

    #Below is the algorithm we use to detect movement detection
    new_pts,status,err = cv2.calcOpticalFlowPyrLK(gray_pre_img, 
                         gray_inp_img, 
                         old_pts, 
                         None)
    print(status,err)
    x,y = new_pts.ravel() #Seperate points from array
    a,b = old_pts.ravel()

    mask = cv2.line(mask, (a,b), (x,y), (255,255,255), 20) #Draw line connecting new and old points

    cv2.circle(inp_img, (x,y), 6, (0,255,0), -1) #Circle for user guidance

    inp_img = cv2.addWeighted(mask, 0.3, inp_img, 0.7, 0) #Blends images
    cv2.imshow("output", inp_img) #Displaying images
    cv2.imshow("result", mask)

    gray_pre_img = gray_inp_img.copy() #Updating values for next loop
    old_pts = new_pts

    if cv2.waitKey(1) == 27: #If esc pressed quit
        break
    
cv2.imwrite('Test.png', mask) #Saves mask image
cv2.destroyAllWindows
cap.release()


'''
This code was inspired by https://www.youtube.com/watch?v=BDyhyQ1qjBY. The same algorithm and structure
are used in this code with my own unique implementations
'''
