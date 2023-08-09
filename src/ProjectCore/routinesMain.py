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


def favorabilityIncrease(): # 선물클릭, 위로 드래그, 캐릭터 찾아서 선택까지
    print()

def scheduleRecurrence():
    print()

# 1. 카페
def cafeRoutine():
    # 카페-초대권-정렬-초대-확인
    menuButton("Cafe")
    menuButton("OkButton")
    menuButton("Invitation") 
    menuButton("Arrange") 
    menuButton("Invite") 
    menuButton("OkButton") 
    # delay 7s
    # 수익수령-수령-허공터치
    menuButton("CafeEarnings")
    menuButton("ReceiveButton") 
    menuButton("ExitUseNotX") 
    menuButton("ExitUseNotX") 
    # 선물창 들어가서 캐릭터 누르기
    menuButton("Gifts") 
    favorabilityIncrease() # 선물클릭, 위로 드래그, 캐릭터 찾아서 선택까지
    menuButton("Home")
    # 끝

# 2. 스케쥴
def scheduleRoutine():
    menuButton("Schedule")
    ###############################################
    # 스케쥴 선택 미구현, 단순 초기값 반복
    #############################################
    menuButton("ScheduleTest")
    menuButton("AllSchedule")
    scheduleRecurrence() 
    # 스케쥴 반복 함수
    # 너무 귀찮으니까 일단 6개 대충 눌러버리는걸로~
    menuButton("Home")
    # 끝

# 3. 학생
def studentRoutine():
    NULL
# 4. 편성
def formationRoutine():
    NULL
# 5. 서클
def clanRoutine():
    menuButton("Clan")
    menuButton("ExitUseX")
    menuButton("Home")
    # 끝
    
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
