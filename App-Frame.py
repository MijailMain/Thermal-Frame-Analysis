#Python 3.6.8
from cv2 import cv2
import numpy as np
import time

from PIL import Image
 

#Nota 1: la constante COLOR_BGR2HSV indica que queremos pasar de BGR a HSV.
#Nota 2: la función cvtColor() también sirve para transformar a otros espacios de color.

#///////////////////////////////////////////////////////////////////////////////////////////////////
#Establecemos el rango mínimo y máximo de H-S-V (Scalas)
#///////////////////////////////////////////////////////////////////////////////////////////////////
# Puede definir todas las Scalas que desee, solo debe configurar los bajos y altos

# Rojo higt Scala-1
Scala1 = "High Red"
Scala1_bajos = np.array([170, 100, 20])
Scala1_altos = np.array([179, 255, 255])

# Rojo Log Scala-2
Scala2 = "Low Red"
Scala2_bajos = np.array([0, 100, 20])
Scala2_altos = np.array([8, 255, 255])

# orange Scala-3
Scala3 = "Orange"
Scala3_bajos = np.array([9, 100, 20])
Scala3_altos = np.array([19, 255, 255])

# yellow Scala-4
Scala4 = "Yellow"
Scala4_bajos = np.array([20, 100, 20])
Scala4_altos = np.array([40, 255, 255])

# Green Scala-5
Scala5 = "Green"
Scala5_bajos = np.array([41, 100, 20])
Scala5_altos = np.array([69, 255, 255])

# light blue Scala-6
Scala6 = "Light Blue"
Scala6_bajos = np.array([70, 100, 20])
Scala6_altos = np.array([105, 255, 255])

# blue Scala-7
Scala7 = "Blue"
Scala7_bajos = np.array([106, 100, 20])
Scala7_altos = np.array([129, 255, 255])

# fuchsia Scala-8
Scala8 = "Fuchsia"
Scala8_bajos = np.array([130,50,50])
Scala8_altos = np.array([168, 255, 255])

PorcentajePixel = []
AnalisListColor = []

#Cargamos la imagen:
img = cv2.imread('Frame-Test.jpg')

#//////////////////////////////////////////////////////////////////////////////////
# Fuincion para Procesar Frame por Scala de color
#//////////////////////////////////////////////////////////////////////////////////
def AnalisFrame (color, rango_bajos, rango_altos):

    Pcolor = 0
    PorcentajeBlack = 0

    #Convertimos la imagen a hsv (scala de colores Lineal):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #Detectamos los píxeles que estén dentro del rango que hemos establecido:
    mask = cv2.inRange(hsv, rango_bajos, rango_altos)
    #print(len(mask))

    #Mostramos la imagen original y la máscara:
    cv2.imshow("./Frames/Original", img)

    #Mostramos la imagen original y la máscara:
    cv2.imshow(color, mask)

    # Guardamos Los resultados de la Imagen carpeta Frames 
    # Una Imagen Por cada Scala
    FramePresado = './Frames/Scala-' + color + '.png'
    cv2.imwrite(FramePresado,mask)
    
    Frame = Image.open(FramePresado)

    DatosFrame = list(Frame.getdata())
    for dato in DatosFrame:
        if (int(dato)> 0):
            #print(dato)
            Pcolor += 1
        else:
            PorcentajeBlack += 1
    Frame.close()
    
    Porcentajecolor = Pcolor*100/(Pcolor + PorcentajeBlack)
    AnalisisColor = [color, Porcentajecolor]

    AnalisListColor.append(AnalisisColor)
    PorcentajePixel.append(Porcentajecolor)

    

    
    """print ("Scala: ", color)
    print ("back", PorcentajeBlack)
    print ("Color", Pcolor)
    print ("%", "{0:.2f}".format(Porcentajecolor))
    print ("Total-pixel", Pcolor + PorcentajeBlack)
    cv2.waitKey(0)
    cv2.destroyAllWindows()"""
    

    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
 
AnalisFrame (Scala1, Scala1_bajos, Scala1_altos)

AnalisFrame (Scala2, Scala2_bajos, Scala2_altos)

AnalisFrame (Scala3, Scala3_bajos, Scala3_altos)

AnalisFrame (Scala4, Scala4_bajos, Scala4_altos)

AnalisFrame (Scala5, Scala5_bajos, Scala5_altos)

AnalisFrame (Scala6, Scala6_bajos, Scala6_altos)

AnalisFrame (Scala7, Scala7_bajos, Scala7_altos)

AnalisFrame (Scala8, Scala8_bajos, Scala8_altos)

print("")
for Dato in AnalisListColor:
    print ("{0:.2f}".format(Dato[1]), "% ---" , Dato[0])

print ("Total %:", sum(PorcentajePixel))