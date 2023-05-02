import pyautogui as pag
import time

x = 1460
# 실습 1 2 3 4 5 과제 2 4
yposition = [320, 394, 472, 554, 632, 728, 808]
y = 3

# 로그인 문제, 창 전환 문제
# 검사 자체를 막아놓음;;
# 그냥 수동으로 원래 페이지로 돌아가서 하는수밖에 없나?
pag.click(x, yposition[y])
time.sleep(0.5)
pag.scroll(-50000)
pag.click(1469, 935)
