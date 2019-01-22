import itchat
import time


itchat.auto_login(hotReload=True)
time_scheme = []


def read_time_file():
    with open("test.txt", 'r', encoding="UTF-8") as time_s:
        for line in time_s:
            time_scheme.append(line)


def check_with_sleep(sleep_time):
    remainder = sleep_time % (3600 * 5)
    count = sleep_time / (3600 * 5)
    print(count)
    i = 0
    for i in range(int(count)):
        time.sleep(3600 * 5)
        friend_test = itchat.search_friends(remarkName="YaqueOK")
        itchat.send("加油，加油！", toUserName=friend_test[0]['UserName'])

    time.sleep(remainder)


read_time_file()
i = 0
print("system start")
while(True):
    min_time = 0
    notes = ""
    start_time = ""
    end_time = ""
    data = ""
    for line in time_scheme:
        temp = line.split("\n")[0].split(" + ")
        temp_notes = temp[1]
        temp = temp[0].split("  ")
        temp_data = temp[0]
        temp = temp[1].split("-")
        temp_start_time = temp[0]
        temp_end_time = temp[1]

        now_time = time.time()
        start_time_second = time.mktime(time.strptime(temp_data + " " + temp_start_time, '%Y-%m-%d %H:%M:%S'))
        dis_time = start_time_second - now_time - 1800
        if min_time > dis_time > 0:
            min_time = dis_time
            notes = temp_notes
            data = temp_data
            start_time = temp_start_time
            end_time = temp_end_time
        elif min_time == 0 and dis_time > 0:
            min_time = dis_time
            notes = temp_notes
            data = temp_data
            start_time = temp_start_time
            end_time = temp_end_time

    print(min_time)
    now_time = time.time()
    check_with_sleep(min_time)

    result = ""
    if end_time == "00:00:00":
        result = "你好，你今天" + start_time + "有直播网课还有30分钟将开始直播,结束时间待定"
    else:
        result = "你好，你今天" + start_time + "有直播网课还有30分钟将开始直播,持续播放到" + end_time

    # print("time coming", result)
    friend_test = itchat.search_friends(remarkName="YaqueOK")
    itchat.send(result, toUserName=friend_test[0]['UserName'])
    itchat.send_image("Pimage/5.jpg", toUserName=friend_test[0]['UserName'])

