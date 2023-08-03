from asyncio.windows_events import NULL
from tkinter import Menubutton
from ppadb.client import Client as AdbClient
import os # 터미널 접근용
import adbCtrlFuns as adbFun    # adb 관련 함수 모음
import win32gui
import pyautogui

# main에서 path와 device 가져와둠
from mainSystem import pathFindImage, pathScreenImage, deviceInfo

# 메뉴화면
menuList = ["Cafe", "Schedule", "Student",      # 카페, 스케쥴, 학생
            "Formation", "Club", "Crafting",    # 편성, 서클, 제조
            "Shop", "Recruit", "Campaign",      # 상점, 모집, 업무
            "Tasks", "Ap", "Mail"]              # 미션, ap, 우편함
              


# 범용UI
universalList = ["Back", "Home",                # 뒤로가기, 홈
                 "ExitUseX", "ExitUseNotX", "okButton",     # x, 빈공간 클릭
                 "ZoomOut", "ZoomIn",           # 줌아웃, 줌인
                 "WheelDown", "WheelUp"]        # 휠다운, 휠업
   
# 카페 
cafeList = ["Gifts", "Invitation", "CafeEarnings", ] # 선물, 초대, 수익

# 스케쥴
Facility = [1, 2, 3, 4, 5, 6, 7, 8] # 나중에 시설 이름으로 변경
scheduleList = ["LeftArrow", "RightArrow", Facility]


# 메뉴 이름 찾아서 클릭
def menuButton(menuName):
    imgName = pathFindImage + menuName + ".png" 
    imgCooldinateArr = adbFun.findImageCooldinate(pathFindImage, pathScreenImage, menuName)
    print(menuName + ".png" + " 이미지를 탐색합니다.")
    adbFun.clickXY(deviceInfo, imgCooldinateArr[0], imgCooldinateArr[1])

def favorabilityIncreaseFunction():
    print()

def scheduleRecurrenceFunction():
    print()

# 1. 카페
def cafeRoutine():
    menuButton("Cafe")
    menuButton("Invitation")
    menuButton("") # 초대
    menuButton("ZoomOut")
    menuButton("Gifts")
    favorabilityIncreaseFunction() # 학생 6명 호감 상승
    menuButton("CafeEarnings")
    menuButton("") # 수령
    menuButton("") # 수령창 나가기
    menuButton("") # 카페 수익 현황 나기기
    menuButton("Home")

# 2. 스케쥴
def scheduleRoutine():
    menuButton("Schedule")
    scheduleRecurrenceFunction() # 스케쥴 반복 함수
    menuButton("RightArrow")
    menuButton("RightArrow")
    scheduleRecurrenceFunction() # 스케쥴 반복 함수
    menuButton("RightArrow")
    scheduleRecurrenceFunction() # 스케쥴 반복 함수
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

#- 상단 파랑, 노랑, 보라 선택
#- 일정 거리 위에서 아래로 드래그
#- 중단 파랑, 노랑, 보라, 하양, 우상단 하양 선택
#- 우하단 선택 구매 클릭
- 확인 클릭
    menuButton("ExitUseNotX")
- 좌측 전술 대회 선택
- 에너지 드링크 30, 60 선택 
- 우하단 선택 구매 클릭
    menuButton("okButton")
    menuButton("ExitUseNotX")
- 우상단 홈버튼


# 8. 업무
def recruitRoutine():

# 9. 임무
def campaignRoutine():

















    
