import keras_ocr
import matplotlib.pyplot as plt
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

ocr_keras = keras_ocr.pipeline.Pipeline()
ocr_img_keras = [
    		keras_ocr.tools.read(ocr_img_keras) for ocr_img_keras in ["C:/Users/ASUS/Desktop/HomeWorkDavid/day56/image/image_pr/file.png","C:/Users/ASUS/Desktop/HomeWorkDavid/day56/image/image_pr/f70ae7817be476fd069f63cb3733d5e7.png"]
]
ocr_pred = ocr_keras.recognize (ocr_img_keras)
fig, axs = plt.subplots(nrows=len(ocr_img_keras), figsize=(10, 20))
for ax, image, predictions in zip(axs, ocr_img_keras, ocr_pred):
    		keras_ocr.tools.drawAnnotations(image=image, 
                                    predictions=predictions, 
                                    ax=ax)		
ocr_img = ocr_pred [1]
for text, box in ocr_img:
    print(text)