import pyautogui
import time
import keyboard
import multiprocessing as mp
import threading
import mouse

def click():
    # mouse = Controller()
    one = time.time_ns()
    iteration = 0
    while True:
        if keyboard.is_pressed("q"):
            print("Q pressed")
            break
        mouse.click('left')
        iteration += 1
    two = time.time_ns()
    print(two-one)
    print(iteration)

if __name__ == '__main__':
    location = pyautogui.locateOnScreen('cookieCenter.png', grayscale=True, confidence=.8)
    x, y = pyautogui.center(location)
    pyautogui.moveTo(x, y)
    n = mp.cpu_count()
    
    for i in range(n):
        t1 = threading.Thread(target=click)
        t1.start()
    

