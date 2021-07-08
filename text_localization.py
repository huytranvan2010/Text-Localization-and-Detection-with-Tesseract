# Hướng dẫn chạy
# python text_localization.py --image image2.png

import re
import pytesseract
from pytesseract import Output
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required=True, help="path to the input image")
parser.add_argument("-c", "--min_confidence", type=float, default=0., help="min confidence value to filter the weak text detection")
args = vars(parser.parse_args())

image = cv2.imread(args["image"])
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)    # chuyển về RGB trước khi đưa vào Tesseract

# lấy boxes quanh các từ 
results = pytesseract.image_to_data(image, output_type=Output.DICT)     # ở đây để output_type=Output.DICT để trả về dạng dictionary

# in ra để biết các keys trong dict là gì
# print(results)

# số bounding boxes trả về
n_boxes = len(results['level'])

# duyệt qua các bounding boxes đó
for i in range(n_boxes):
    # lấy x, y, w, h cho từng bounding box
    x = results['left'][i]
    y = results['top'][i]
    w = results['width'][i]
    h = results['height'][i]

    text = results['text'][i]
    conf = int(results['conf'][i])  # chuyển về int nha, nó đang ở string

    # Lọc các text có confidence thấp
    if conf < args["min_confidence"]:
        continue
    
    # In ra confidence và text
    print("Confidence: {}".format(conf))
    print("Text: {}".format(text))
    print("")

    # loại bỏ các kí tự ko phải ASCII để có thể in ra trên ảnh, dùng list comprehension, .strip() loại bỏ dấu trắng đầu cuối
    text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
	
    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('Output', image)
cv2.waitKey(0)