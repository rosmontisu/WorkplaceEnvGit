import json

def imgPathsCreate(pathImg):
    with open("./BaaMain/imgPaths.json", "r") as f:
        data = json.load(f)

    if data["system"]["firstOpen"] != pathImg:
        for key, value in data.items():
            for subkey, subvalue in value.items():
                data[key][subkey] = f"{pathImg}{subvalue}"
    
        with open("./BaaMain/imgPaths.json", "w") as f:
            json.dump(data, f, indent=4)
            