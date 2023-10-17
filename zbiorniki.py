import numpy as np

def materialVisualised(spaceship:list[int], animated=False):    #visualise the tank and fill with liquid
    import cv2  #image creation and display
    
    def drawGrid(img:np.ndarray, x:int, y:int, sajz:int):       #to draw squares surrounding each unit
        h,w=img.shape[:2]                       #height an width of the image
        for hor in range(int(y/sajz)):          #draw horizontal lines (rectangles one pixel wide)
            img=cv2.rectangle(img, (0, hor*sajz), (w, hor*sajz+1), (255,255,255), -1)
        for ver in range(int(x/sajz)):          #draw vertical lines
            img=cv2.rectangle(img, (ver*sajz, 0), (ver*sajz+1, h), (255,255,255), -1)

        return img

    arr=np.array(spaceship)

    SAJZ=int(min(min(1700/len(spaceship),100),900/max(spaceship)))  #standard unit, large for small sets, but limited to not exceed 1700x900p
    
    wys=max(spaceship)*SAJZ                     #height of resulting image
    szer=len(spaceship)*SAJZ                    #width of resulting image
    img=np.zeros((wys,szer,3), np.uint8)    #empty image (numpy array)
    img[:]=(53,30,54)                       #set background color

    for i,slup in enumerate(spaceship):         #draw each wall and add border to the "tank"
        img=cv2.rectangle(img, (i*SAJZ, wys-slup*SAJZ), (i*SAJZ+SAJZ, wys), (145,119,139), -1)
    img = cv2.copyMakeBorder(img,1,1,1,1,cv2.BORDER_CONSTANT,value=(255,255,255))

    total=0                         #units filled with liquid
    for i in range(1,arr.max()+1):  #go bottom-up, find units surrounded by walls
        sciany=np.where(arr>=i)[0].tolist()
        dzbany=[ind for ind in range(min(sciany)+1, max(sciany)) if arr[ind]<i] #vertical indices of units with walls on both sides
        total+=len(dzbany)
        if animated:                #display animation filling up units that won't spill
            for progres in range(100):
                for dzban in dzbany:
                    img=cv2.rectangle(img, (dzban*SAJZ, wys-i*SAJZ+int(SAJZ*(100-progres)/100)), (dzban*SAJZ+SAJZ, wys-i*SAJZ+SAJZ), (156,86,139), -1)
                img=drawGrid(img, szer, wys, SAJZ)
                outputImage = cv2.copyMakeBorder(img,SAJZ,SAJZ,SAJZ,SAJZ,cv2.BORDER_CONSTANT,value=(0,0,0))
                cv2.imshow('img',outputImage)
                cv2.waitKey(1)
        else:                       #or not, I won't judge
            for dzban in dzbany:
                img=cv2.rectangle(img, (dzban*SAJZ, wys-i*SAJZ), (dzban*SAJZ+SAJZ, wys-(i-1)*SAJZ), (156,86,139), -1)
    
    print('result:',total)          #display filled units and final image
    img=drawGrid(img, szer, wys, SAJZ)
    outputImage = cv2.copyMakeBorder(img,SAJZ,SAJZ,SAJZ,SAJZ,cv2.BORDER_CONSTANT,value=(0,0,0))
    cv2.imshow('img',outputImage) 
    cv2.waitKey(0)

    return(total)

def material(spaceship:list[int]):
    arr=np.array(spaceship)             #input list as numpy array
    total=0                         #units filled with liquid
    for i in range(1,arr.max()+1):  #go bottom-up, find units surrounded by walls
        sciany=np.where(arr>=i)[0]  #find all walls on height i
        total+=len([ind for ind in range(np.min(sciany)+1, np.max(sciany)) if arr[ind]<i])  #vertical indices of units with walls on both sides
    return total

def tests():
    assert material([0,1,0,2,1,0,3,1,2,0])                                  == 5, f'This tank should fit 5 units of liquid, got {material([0,1,0,2,1,0,3,1,2,0])}'
    assert material([0,3,2,0,3,2,0,4,2,0])                                  == 8, f'This tank should fit 8 units of liquid, got {material([0,3,2,0,3,2,0,4,2,0])}'
    assert material([0,1,0,2,1,0,1,3,2,1,2,1])                              == 6, f'This tank should fit 6 units of liquid, got {material([0,1,0,2,1,0,1,3,2,1,2,1])}'
    assert material([0,1,0,2,1,0,3,1,0,1,2])                                == 8, f'This tank should fit 8 units of liquid, got {material([0,1,0,2,1,0,3,1,0,1,2])}'
    assert material([4,2,0,3,2,5])                                          == 9, f'This tank should fit 9 units of liquid, got {material([4,2,0,3,2,5])}'
    assert material([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3])  == 83, f'This tank should fit 83 units of liquid, got {material([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3])}'
    assert material([6,2,1,1,8,0,5,5,0,1,8,9,6,9,4,8,0,0])                  == 50, f'This tank should fit 50 units of liquid, got {material([6,2,1,1,8,0,5,5,0,1,8,9,6,9,4,8,0,0])}'

tests()

# print(material([0,1,0,2,1,0,3,1,2,0]))                                                          #5
# print(material([0,3,2,0,3,2,0,4,2,0]))                                                          #8
# print(material([0,1,0,2,1,0,1,3,2,1,2,1]))                                                      #6
# print(material([0,1,0,2,1,0,3,1,0,1,2]))                                                        #8
# print(material([4,2,0,3,2,5]))                                                                  #9
# print(material([6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3])) #83
# print(material([6, 2, 1, 1, 8, 0, 5, 5, 0, 1, 8, 9, 6, 9, 4, 8, 0, 0]))                         #50


# materialVisualised([0,1,0,2,1,0,3,1,2,0])
# materialVisualised([0,3,2,0,3,2,0,4,2,0])
# materialVisualised([0,1,0,2,1,0,1,3,2,1,2,1])
# materialVisualised([0,1,0,2,1,0,3,1,0,1,2])
# materialVisualised([4,2,0,3,2,5])
materialVisualised([6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3], animated=True)
materialVisualised([6, 2, 1, 1, 8, 0, 5, 5, 0, 1, 8, 9, 6, 9, 4, 8, 0, 0], animated=True)