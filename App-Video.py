from cv2 import cv2
import numpy as np
import time

from PIL import Image

captura = cv2.VideoCapture('Video-Termico-Corte.mp4')
i =0


# Rojo higt
Scala1 = "High Red"
Scala1_bajos = np.array([170, 100, 20])
Scala1_altos = np.array([179, 255, 255])

# Rojo Log
Scala2 = "Low Red"
Scala2_bajos = np.array([0, 100, 20])
Scala2_altos = np.array([8, 255, 255])

# orange
Scala3 = "orange"
Scala3_bajos = np.array([9, 100, 20])
Scala3_altos = np.array([19, 255, 255])

# yellow
Scala4 = "yellow"
Scala4_bajos = np.array([20, 100, 20])
Scala4_altos = np.array([40, 255, 255])

# Green
Scala5 = "Green"
Scala5_bajos = np.array([41, 100, 20])
Scala5_altos = np.array([69, 255, 255])

# light blue
Scala6 = "light blue"
Scala6_bajos = np.array([70, 100, 20])
Scala6_altos = np.array([105, 255, 255])

# blue
Scala7 = "blue"
Scala7_bajos = np.array([106, 100, 20])
Scala7_altos = np.array([129, 255, 255])

# fuchsia
Scala8 = "fuchsia"
Scala8_bajos = np.array([130,50,50])
Scala8_altos = np.array([168, 255, 255])

PorcentajePixel = []
AnalisListColor = []

def AnalisFrame (color, rango_bajos, rango_altos):
  i=0
  PorcentajeBlack =0 
  Pcolor=0
  while (captura.isOpened()):
    ret, imagen = captura.read()
    # Frame capturado
    cv2.imwrite('./Frames-Video/FramePresado.png', imagen)

    #Cargamos Frame:
    img = cv2.imread('./Frames-Video/FramePresado.png')

    #Convertimos Frame a hsv:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #Detectamos los píxeles que estén dentro del rango que hemos establecido:
    mask = cv2.inRange(hsv, rango_bajos, rango_altos)

    cv2.imwrite('./Frames-Video/FramePresado-Scala.png',mask)
    foto = Image.open('./Frames-Video/FramePresado-Scala.png')
    datos = list(foto.getdata())
    for dato in datos:
      if (int(dato)> 0):
          #print(dato)
          Pcolor += 1
      else:
        PorcentajeBlack += 1
    foto.close()

    Porcentajecolor = Pcolor*100/(Pcolor + PorcentajeBlack)
    AnalisisColor = [color, Porcentajecolor]

    AnalisListColor.append(AnalisisColor)
    PorcentajePixel.append(Porcentajecolor)

    

    time.sleep(.100)
    i+=1
    print ("***************************************************************")
    print (" - Frame Processed", i)
    print ("   - Scala: ", color)
    print ("   - Back-Pixel", PorcentajeBlack)
    print ("   - Color-Pixel", Pcolor)
    print ("   - (%) Color-Pixel", "{0:.2f}".format(Porcentajecolor))
    print ("   - Total-pixel", Pcolor + PorcentajeBlack)
    print ("")

  captura.release()
  cv2.destroyAllWindows()

AnalisFrame (Scala1, Scala1_bajos, Scala1_altos)