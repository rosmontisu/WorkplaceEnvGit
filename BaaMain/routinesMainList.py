from asyncio.windows_events import NULL
from tkinter import Menubutton
from ppadb.client import Client as AdbClient
import os # 터미널 접근용
import adbCtrlFuns as adbFun    # adb 관련 함수 모음
import win32gui
import pyautogui

# main에서 path와 device 가져와둠
from mainSystem import pathImg, pathScreen, deviceInfo

menuImgPath = {
    "Cafe": pathImg + "cafe.png", # 카페
    "Invitation": pathImg + "invitation.png", # 초대
    "ZoomOut": pathImg + "zoom_out.png", # 줌 아웃
    "Gifts": pathImg + "gifts.png", # 선물
    "CafeEarnings": pathImg + "cafe_earnings.png", # 카페 수익
    "Receive": pathImg + "receive.png", # 수령
    "Home": pathImg + "home.png", # 홈
    "Schedule": pathImg + "schedule.png", # 스케쥴
    "RightArrow": pathImg + "right_arrow.png", # 오른쪽 화살표
}
universalImgPath = {
    "Back": pathImg + "back.png", # 뒤로 가기
    "Home": pathImg + "home.png", # 홈
    "ExitUseX": pathImg + "exit_use_x.png", # x
    "ExitUseNotX": pathImg + "exit_use_not_x.png", # 빈 공간 클릭
    "okButton": pathImg + "ok_button.png", # 확인 버튼
    "ZoomOut": pathImg + "zoom_out.png", # 줌 아웃
    "ZoomIn": pathImg + "zoom_in.png", # 줌 인
    "WheelDown": pathImg + "wheel_down.png", # 휠 다운
    "WheelUp": pathImg + "wheel_up.png", # 휠 업
}
cafeImgPath = {
    "Gifts": pathImg + "gifts.png", # 선물
    "Invitation": pathImg + "invitation.png", # 초대
    "CafeEarnings": pathImg + "cafe_earnings.png", # 카페 수익
}
scheduleImgPath = {
    "LeftArrow": pathImg + "left_arrow.png", # 왼쪽 화살표
    "RightArrow": pathImg + "right_arrow.png", # 오른쪽 화살표
    "Facility": pathImg + "facility.png", # 시설
}

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

















    
