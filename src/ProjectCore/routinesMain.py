from asyncio.windows_events import NULL
from tkinter import Menubutton
from ppadb.client import Client as AdbClient
import os # 터미널 접근용
import managerAdb as adbFun    # adb 관련 함수 모음
import win32gui
import pyautogui

# main에서 path와 device 가져와둠
from mainSystem import pathImg, pathScreen, deviceInfo

# 메뉴 이름 찾아서 클릭
def menuButton(imgName):
    imgName = pathImg + imgName + ".png" 
    coordinates = adbFun.findCoordinate(pathImg, pathScreen, imgName)
    print(imgName + ".png" + " 이미지를 탐색합니다.")
    adbFun.clickXY(deviceInfo, coordinates[0], coordinates[1])

def favorabilityIncrease():
    print()

def scheduleRecurrence():
    print()

# 1. 카페
def cafeRoutine():
    menuButton("Cafe")
    menuButton("OkButton")
    menuButton("Invitation")
    menuButton("") # 초대
    menuButton("ZoomOut")
    menuButton("Gifts")
    favorabilityIncrease() # 학생 6명 호감 상승
    menuButton("CafeEarnings")
    menuButton("") # 수령
    menuButton("") # 수령창 나가기
    menuButton("") # 카페 수익 현황 나기기
    menuButton("Home")

# 2. 스케쥴
def scheduleRoutine():
    menuButton("Schedule")
    scheduleRecurrence() # 스케쥴 반복 함수
    menuButton("RightArrow")
    menuButton("RightArrow")
    scheduleRecurrence() # 스케쥴 반복 함수
    menuButton("RightArrow")
    scheduleRecurrence() # 스케쥴 반복 함수
    menuButton("Home")

# 3. 학생
def studentRoutine():
    NULL
# 4. 편성
def formationRoutine():
    NULL
# 5. 서클
def clanRoutine():
    menuButton("ExitUseX")
    menuButton("Home")
# 6. 제조
def craftingRoutine():
    NULL
# 7. 상점
def shopRoutine():
    menuButton("WheelDown") * 3


# 8. 업무
def recruitRoutine():
    NULL

# 9. 임무
def campaignRoutine():
    NULL

















    
