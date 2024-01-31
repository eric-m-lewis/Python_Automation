import webbrowser, time, os
from datetime import datetime


def calcTimeDiff(target, current):
    targetTime = datetime.strptime(target, '%H:%M:%S')
    currentTime = datetime.strptime(current, '%H:%M:%S')
    timeRemain = targetTime - currentTime
    timeRemainString = datetime.strptime(str(timeRemain), "%H:%M:%S")
    timeRemainString = timeRemainString.strftime("%H:%M:%S")
    return timeRemainString

urlList = ["https://www.twitch.tv/twitchrivals", "https://www.twitch.tv/stankrat_","https://www.twitch.tv/gingy"]
targetTime = '15:00:10'

currentTime = '00:00:00'
while currentTime != targetTime:
    os.system('cls')
    now = datetime.now()
    currentTime = now.strftime('%H:%M:%S')
    timeDiffString = calcTimeDiff(targetTime, currentTime)
    printString = f'Time Remaining: {timeDiffString}'
    print(printString)
    time.sleep(1)

for url in urlList:
    print(f"\nOpening URL: {url}")
    webbrowser.open(url)
