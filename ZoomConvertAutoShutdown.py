import pyautogui
import time
import os


# 안전모드 설정
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

# Log 폴더 확인 후 생성
path = './log/'
if not os.path.isdir(path):                                                           
	os.mkdir(path)
	
# 화면 위치 조정
input('작업 완료 후, 종료할 창을 화면에 보이도록 조정하시고 아무키나 누르세요')
print()

# 줌 컨버팅 현황 확인
print('Zoom 컨버팅 종료 확인 시작')
day = time.strftime('%Y-%m-%d', time.localtime())
file_name = f'{path}Log_{day}.txt'

while 1:
    start_time = time.time()
    zoom_con = pyautogui.locateOnScreen('./data/zoom_con.png')
    print(zoom_con)
    end_time = time.time()
    print(f'{(end_time - start_time):.0f}')


    with open(file_name, 'a', encoding='utf-8') as f:
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        if zoom_con is None:
            print('Zoom Convert Exit')
            f.write(f'{now_time} : Zoom Convert Exit\n')
            break
        else:
            print('Zoom Convert in Progress')
            f.write(f'{now_time} : Zoom Convert in Progress\n')

    time.sleep(60)

# 딜레이
time.sleep(5)


# ok1
zoom_ok = pyautogui.locateOnScreen('./data/zoom_ok1.png') 
print(zoom_ok)
if zoom_ok is not None :
    with open(file_name, 'a', encoding='utf-8') as f:
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print('Zoom OK1')
        f.write(f'{now_time} : Zoom OK1 Exit\n')

    buttonx, buttony = pyautogui.center(zoom_ok)
    print(buttonx, buttony)

    pyautogui.click(buttonx, buttony)  

# ok2
zoom_ok = pyautogui.locateOnScreen('./data/zoom_ok2.png')  
print(zoom_ok)
if zoom_ok is not None :
    with open(file_name, 'a', encoding='utf-8') as f:
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print('Zoom OK2')
        f.write(f'{now_time} : Zoom OK2 Exit\n')

    buttonx, buttony = pyautogui.center(zoom_ok)
    print(buttonx, buttony)

    pyautogui.click(buttonx, buttony) 

# ok3
zoom_ok = pyautogui.locateOnScreen('./data/zoom_ok3.png')  
print(zoom_ok)
if zoom_ok is not None :
    with open(file_name, 'a', encoding='utf-8') as f:
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print('Zoom OK3')
        f.write(f'{now_time} : Zoom OK3 Exit\n')

    buttonx, buttony = pyautogui.center(zoom_ok)
    print(buttonx, buttony)

    pyautogui.click(buttonx, buttony)

# ok4
zoom_ok = pyautogui.locateOnScreen('./data/zoom_ok4.png')  
print(zoom_ok)
if zoom_ok is not None :
    with open(file_name, 'a', encoding='utf-8') as f:
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print('Zoom OK4')
        f.write(f'{now_time} : Zoom OK4 Exit\n')

    buttonx, buttony = pyautogui.center(zoom_ok)
    print(buttonx, buttony)

    pyautogui.click(buttonx, buttony)
	
else :
    with open(file_name, 'a', encoding='utf-8') as f:
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print('Zoom ESC')
        f.write(f'{now_time} : Zoom ESC Exit\n')

    pyautogui.press('esc')

print('Zoom 컨버팅 종료 확인')
print('Zoom 컨버팅 파일 저장 후 10초 뒤 시스템 종료')
os.system('shutdown /s /t 10')