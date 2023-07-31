from ppadb.client import Client as AdbClient

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

# function
def click(x,y):
    # https://adbinstaller.com/commands/adb-shell-input-tap-5b67dc5ee7958178a295553f
    cmd = "input touchscreen tap " + str(x) + " " + str(y)
    adbdevice.shell(cmd)

def screenCapture():
    # https://adbinstaller.com/commands/adb-shell-screencap-5b69ae0032e0461ad1db1ca8
    cmd = "screencap -d 0 /sdcard/test.png"
    adbdevice.shell(cmd)
    adbdevice.shell("pull /sdcard/test.png")



click(100,100)
screenCapture()

