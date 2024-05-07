from flask import Flask

app = Flask(__name__)

from datetime import datetime

def updateByWhiteList(productMasterDataObj, white_lists):
    try:
        print("updateByWhiteList:")
        for whiteList in white_lists:
            productCode=""
            start_time = ""
            end_time = ""
            if len(whiteList)>0:
                productCode = whiteList[0]
            if len(whiteList) > 1:
                start_time = whiteList[1]
            if len(whiteList) > 2:
                end_time = whiteList[2]
            if productMasterDataObj["productCode"] == productCode and withinRangeTime(start_time, end_time):
                productMasterDataObj.update({"shipInOwnContainerIndicator": "True"})
                break
    except Exception as e:
        print("updateByWhiteList occurs exception",e)

def withinRangeTime(start_time,end_time):
    now = datetime.now()
    now_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(now_time)
    if start_time and end_time :
        return  start_time < now_time < end_time

    if len(start_time) == 0  and len(end_time) == 0 :
        return True
    
    if start_time :
        return start_time < now_time

    return end_time > now_time

def load_white_list(self):
    path = os.path.dirname(__file__)
    fullPath = os.path.join(path, "resources")
    global data_list
    with open(fullPath + "/white_list.txt", 'r' , encoding="utf-8") as f:
        data_list = [line.strip().split(',') for line in f]
    return data_list


@app.before_first_request
def load_data():
    global data_list
    with open('data.txt', 'r',encoding="utf-8") as f:
        data_list = [line.strip().split(',') for line in f]




productMasterDataObj ={"productCode":"12"}
load_data()
updateByWhiteList(productMasterDataObj,data_list)
print(productMasterDataObj)

