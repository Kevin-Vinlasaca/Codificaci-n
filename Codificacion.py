import cv2
#capture = cv2.VideoCapture('vcomp.mp4')
capture = cv2.VideoCapture('MOVIE-0007.mp4')
cont = 0                                                         #Lenovo/PycharmProjects/frames/imagenes/
path = '/Users/Lenovo/PycharmProjects/frames/imagenes/'
#path ='C:/Users/Lenovo/Desktop/Nuevacarpeta'


while (capture.isOpened()):
    ret, frame = capture.read()
    if (ret == True):
        cv2.imwrite(path + 'IMG_%04d.jpg' % cont, frame)

        cont += 1
        if (cv2.waitKey(1) == ord('s')):
            break
    else:
        break

capture.release()



# juntar los frames
img_array = []

#For para leer imagenes desde un directorio



for x in range (0,200):
    #path ='C:/Users/Lenovo/Desktop/Nuevacarpeta/IMG_%05d.jpg' % x
    path = 'C:/Users/Lenovo/PycharmProjects/frames/imagenes/IMG_%04d.jpg' % x

    img = cv2.imread(path)
    img_array.append(img)

#Tamaño de la última imagen alto y ancho

height, width  = img.shape[:2]

video = cv2.VideoWriter('finalvideo2.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 5, (width,height))

#For para guardar frames en un video




for i in range(len(img_array)):
    video.write(img_array[i])

video.release()


cv2.destroyAllWindows()
