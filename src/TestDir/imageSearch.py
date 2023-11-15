import pyautogui

result = pyautogui.locateOnScreen("imageSearchTest.png", confidence = 0.9)  # 이미지 영역 찾기
center = pyautogui.center(result)   # 중심 좌표 찾기
print(result)
print(center)
pyautogui.click(center)

# 위 두개의 기능을 합친 함수
center = pyautogui.locateCenterOnScreen('imageSearchTest.png')  # 이미지 영역 중심 좌표 찾기
pyautogui.click(center) 

