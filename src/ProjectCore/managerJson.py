import json


def imgPathsCreate(editMyPath):
    global imgPath
    imgPath = "pathImgUser.json"
    with open(imgPath, "r") as f:
        data = json.load(f)

    if data["system"]["firstOpen"] != editMyPath:
        for key, value in data.items():
            for subkey, subvalue in value.items():
                data[key][subkey] = f"{editMyPath}{subvalue}"
    
        with open(imgPath, "w") as f:
            json.dump(data, f, indent=4)
            