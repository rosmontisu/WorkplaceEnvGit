from ppadb.client import Client as AdbClient
import os # 터미널 접근용
import adbCtrlFuns as adbFun    # adb 관련 함수 모음
import win32gui

# 경로 변수
findImagePath = "./BaaMain/FindImages/" 
screenImagePath = "./BaaMain/ScreenImages/" 

# 사전 변수 
deviceHandleName = "설정 - MuMu Player"

# adb 연결
adbPort = 7555 # 에뮬레이터 포트
client = AdbClient(host="127.0.0.1", port=5037) # adb를 사용해 통신할 client 객체 
client.remote_connect("localhost", int(adbPort)) # 에뮬레이터와 연결하는 메서드 
deviceInfo = client.device("localhost:"+str(adbPort)) # device() 반환값, 에뮬의 참조 저장

print("Adb detected" if deviceInfo is not None else "Adb not detected")

# 핸들값 추출
deviceHandle = win32gui.FindWindow(None, deviceHandleName)
print("mumuplayer handle is " + str(deviceHandle)) # 이때 핸들은 32비트 정수값이다.

# 현재 에뮬레이터 스크린 캡쳐
adbFun.captureAppScreen(deviceInfo)
cmdCommand = "adb pull /sdcard/screen.png" + " " + screenImagePath
os.system(cmdCommand)

# 이미지 탐색 후 좌표 추출
imageNum = adbFun.findImageNumber(findImagePath, screenImagePath)

# 이미지 좌표 클릭
adbFun.clickXY(deviceInfo, imageNum[0], imageNum[1])


