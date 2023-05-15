import cv2

from myblog.settings import *


def convertBlackAndWhiteImage(image,intensite):
  print("bonjour fonction 1")
  """variable:"""

  # page = "page9.L"
  cheminImage = str(traitementImg) + image # media url pour trouver le repertoire media (la variable viens du fichier settings.py)
  # image = "ImageBlackAndWhite"
  originalImage = cv2.imread(cheminImage)


  # convertion sur une trame partant du noir jusqu'au blanc (grayscale)
  grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)


  #plus le premier chiffre est bas, plus le gris basculeras vers le blanc

  (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, intensite, 255, cv2.THRESH_BINARY)

  cv2.imwrite(cheminImage, blackAndWhiteImage) 

  return image


def convertBlackAndWhiteImage2():
  return "bonjour fonction2"
  

