import json


def imgPathsCreate(pathImgResource):

    imgPath = "./src/ProjectCore/pathImgUser.json"
    with open(imgPath, "r") as f:
        data = json.load(f)

    if data["system"]["firstOpen"] != pathImgResource:
        for key, value in data.items():
            for subkey, subvalue in value.items():
                data[key][subkey] = f"{pathImgResource}{subvalue}"
    
        with open(imgPath, "w") as f:
            json.dump(data, f, indent=4)
            