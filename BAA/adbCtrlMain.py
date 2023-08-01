import cv2
from ppadb.client import Client as AdbClient
import random
import time

import win32gui
import win32ui
import win32con
import pyautogui
from PIL import Image

deviceport = 7555 # adb diveces로 확인 가능

# adb settings
client = AdbClient(host="127.0.0.1", port=5037)
client.remote_connect("localhost", int(deviceport))
adbdevice = client.device("localhost:"+str(deviceport))
if adbdevice is not None:
    print("Adb detected")
else:
    print("Adb not detected")
    exit(0)


# 내 함수들
# 함수는 아래와 같은 adb shell 명령어의 구조로 작동
# adb shell + "my cmd str"
# ex) adb shell input tap <x> <y>

def click(x,y): # (x, y)좌표 클릭

    cmd = "input touchscreen tap " + str(x) + " " + str(y)
    adbdevice.shell(cmd)


def randomClick(x, y, dx, dy):  # 지정 범위(dx, dy)안에서의 랜덤 클릭
    newy = y
    xx = random.randint(x, x + dx)  # randint(a, b) - a이상 b이하 랜덤 정수 생성
    yy = random.randint(newy, newy + dy)    
    cmd = "input touchscreen tap " + str(xx) + " " + str(yy)

    adbdevice.shell(cmd)


def delayClick(cor):    # 일정 시간 클릭을 유지(input swipe 커맨드 이기에 드래그와 동일한 원리)
    newy = cor[1]
    xx = random.randint(cor[0], cor[0] + cor[2])
    yy = random.randint(newy, newy + cor[3])
    cmd = ("input swipe " + str(xx) + " " + str(yy) # 시작 좌표
    + " " + str(xx) + " " + str(yy)                 # 종료 좌표
    + " " + str(random.randint(51,180)))            # 누르는 시간(delay ms)

    adbdevice.shell(cmd)


def screenCapture(): # screen capture and pull my test dir
    cmd = "screencap -d 0 /sdcard/myScreenCapture.png"
    adbdevice.shell(cmd)
    cmd = "pull /sdcard/myScreenCapture.png"
    adbdevice.shell(cmd)
    print("정상작동")

def imageCenterClick(findImageName):
    center = pyautogui.locateCenterOnScreen(findImageName)  # 이미지 영역 중심 좌표 찾기
    pyautogui.click(center) 

def background_screenshot(hwnd, width, height): # 배경 스크린 찍는 함수
    # 창의 핸들, 스크린샷의 너비 및 높이
    wDC = win32gui.GetWindowDC(hwnd)    # 창의 장치 컨덱트(DC)
    dcObj = win32ui.CreateDCFromHandle(wDC) # 호환 가능 DC 생성
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap() # 비트맵 개체 생성, 이때 크기는 스크린샷과 같다.
    dataBitMap.CreateCompatibleBitmap(dcObj, width, height)

    cDC.SelectObject(dataBitMap)    # 호환 가능 DC에서 비트맵 개체 선택
    cDC.BitBlt((0,0),(width, height) , dcObj, (0,0), win32con.SRCCOPY) 
    # DC의 내용을 비트맵으로 복사, 이때 인자는 다음과 같다.
    # 복사할 사각형의 왼쪽 상단 모서리의 좌표 (0, 0)
    # 사각형의 너비와 높이 (width, height)
    # 소스 DC (dcObj)
    # 소스 사각형의 왼쪽 상단 모서리의 좌표 (0, 0)
    bmpinfo = dataBitMap.GetInfo()  
    # 비트맵 정보 (너비, 높이, 색상형식)
    bmpstr = dataBitMap.GetBitmapBits(True) 
    # 비트맵 원시 바이트 배열 (비트맵 객체의 실제 픽셀 데이터인 원시바이트 배열 == 비트)

    im = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), 
                          bmpstr, 'raw', 'BGRX', 0, 1)
    # 비트맵 비트에서 Image 개체를 생성, 이때 인자는 다음과 같다.
    # 픽셀 형식 (mode: 'RGB')
    # 이미지 크기 튜플 (bmpinfo['bmWidth'], bmpinfo['bmHeight'])
    # 원시 바이트 배열 (bmpstr)
    # 바이트 순서(decorder_name: str = 'raw')
    # 색상공간 ('BGRX')
    # 스트라이드 

    dcObj.DeleteDC()    # DC 객체 제거(해제)
    cDC.DeleteDC()      # 비트맵 객체 제거 
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    return im
   
mumuhwnd = win32gui.FindWindow(None, "설정 - MuMu Player")
# 이때 핸들은 32비트 정수값이다.
print(mumuhwnd)

findImage = "searchImage1.png"

해상도오차보정 = 0 #32
scr_img = background_screenshot(mumuhwnd, 1920, 1080 + 해상도오차보정)
scr_img.show()  # 스크린샷 이미지 확인(디버그용)
#findImage.show()


clickhere = pyautogui.locate(findImage, scr_img, confidence=0.99) 
# confidence = 0 일때 완전 일치
# scr_image 에서 findImage를 허용오차 80%로 서치한다.
print("좌표")
print(clickhere)
pyautogui.click(clickhere)

imageCenterClick(findImage)
        

#randomClick(100,100, 10, 10)
#screenCapture()

# 댓다 

