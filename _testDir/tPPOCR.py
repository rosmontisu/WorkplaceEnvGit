import paddleocr
from paddleocr import PaddleOCR

# PaddleOCR 초기화
ocr = PaddleOCR()

# 이미지 로드
image_path = 'path/to/your/image.jpg'
result = ocr.ocr(image_path)

# 결과 출력
for line in result:
    for word_info in line:
        print('단어:', word_info[1][0], '신뢰도:', word_info[1][1])
    print('------')
