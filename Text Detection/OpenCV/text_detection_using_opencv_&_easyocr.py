# -*- coding: utf-8 -*-
"""Text detection using OpenCV & EasyOCR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oKS-cQM3JjBngV6JSbtUMEyiiJXGQUo7
"""

!pip install opencv-python

!pip3 install torch torchvision torchaudio

!pip install easyocr

"""Note: we need PyTorch because the deep learning framework of easyocr is built using PyTorch."""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import cv2
import easyocr

"""# Load Images"""

carplate_img = 'CarPlate.jpg'
handwriting1_ing = 'HandWriting1.jpg'
digits1_img = 'digits1.jpg'
digits2_img = 'digits2.jpg'
invoice_img = 'invoice.png'
notice1_img = 'notice1.jpg'
notice2_img = 'notice2.jpg'

"""# Extract text using Easyocr"""

def recognize_text(img_path):
  #load images
  reader = easyocr.Reader(['en']) #detect only english texts
  #recognize text
  return reader.readtext(img_path)

carplate = recognize_text(carplate_img)

# It returns a list of 4 positions of the text detected, 
# text of the image, confidence(accuracy of each twxt detectd)
carplate

# Check accuracy by displaying the original image
carplate_original = cv2.imread(carplate_img)
carplate_original = cv2.cvtColor(carplate_original, cv2.COLOR_BGR2RGB)
plt.imshow(carplate_original)

# Function to draw a rectangle around each recognized text
def overlay_ocr_text(img_path, save_as_name):
  #Load images
  img = cv2.imread(img_path)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

  # Define dots per inch of the image
  dpi = 80
  #speciy the figure width and height
  fig_width, fig_height = int(img.shape[0]/dpi), int(img.shape[1]/dpi)
  plt.figure()
  f, axarr = plt.subplots(1, 2, figsize = (fig_width, fig_height))
  axarr[0].imshow(img)  #display the original image on the left side

  # Recognize text
  result_img = recognize_text(img_path)  

  # If OCR Confidence > 0.5, draw bounding box and text
  for(b_box, text, prob) in result_img:
      if prob >= 0.5:
        #display the box
        print(f'Detected text: {text} (Probability: {prob:.2f})')

        # Get top-left and bottom-right b_box vertices
        (top_left, top_right, bottom_right, bottom_left) = b_box
        top_left = (int(top_left[0]), int(top_left[1]))
        bottom_right = (int(bottom_right[0]), int(bottom_right[1]))

        # Create a rectangle for b_box display
        cv2.rectangle(img = img, pt1 = top_left, pt2 = bottom_right, 
                      color = (255, 0, 0), thickness = 10)
        
        # Put recognized text
        cv2.putText(img = img, text = text, org = (top_left[0], top_left[1] - 10),
                    fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1, 
                    color = (255, 0, 0), thickness = 8)
        
  # show and save image
  axarr[1].imshow(img)
  #plt.savefig(f'./output/{save_as_name}', bbox_inches='tight')

"""# See output"""

overlay_ocr_text(carplate_img, 'text_carplate')

overlay_ocr_text(handwriting1_ing, 'text_HandWriting_1')

overlay_ocr_text(digits1_img, 'text_digits_1')

overlay_ocr_text(digits2_img, 'text_digits_2')

overlay_ocr_text(invoice_img, 'text_invoice')

overlay_ocr_text(notice1_img, 'text_notice_1')

overlay_ocr_text(notice2_img, 'text_invoice_2')