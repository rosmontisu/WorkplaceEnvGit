import cv2
import numpy as np


import paddleocr
from paddleocr import PaddleOCR

# PaddleOCR 초기화
ocr = PaddleOCR()

# 이미지 로드
image_path = './testDir/nowscreen.png'

print('------')
print('------')
img = cv2.imread("./testDir/nowScreen.png", cv2.IMREAD_COLOR)
print(img)
print('------')
print('------')


print(image_path)
result = ocr.ocr(image_path)

# 결과 출력
for line in result:
    for word_info in line:
        print('t1:', word_info[1][0], 't2:', word_info[1][1])
    print('------')
