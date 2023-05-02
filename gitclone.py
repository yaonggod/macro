import pyautogui as pag
import time

# 한글 인식이 안됨;;

# gitbash 위치 저장하고 클릭을 하든 더블클릭을 하든 오픈 알아서하기
# git = pag.position() 찾아서 하면 됩니다
git = (568, 1073)
pag.click(git)
# 경로 찾아서 가기
time.sleep(0.5)
pag.write("cd ~")
pag.press("enter")
time.sleep(0.5)
pag.write("cd desktop")
pag.press("enter")
time.sleep(0.5)
pag.write("cd Vue.js")
pag.press("enter")

# 내 아이디
id = "jy23698/"
# 과목
subject = "vue_"
# 실습, 과제
t = "ws_"
# 날짜
day = "01_"
# 번호
num = ["1", "2", "3", "4", "5"]
url = "https://lab.ssafy.com/" + id + subject + t + day
for n in num:
    pag.write("git clone " + url + n)
    pag.press("enter")