import pyautogui

DURACAO = 0

distance = 200
while distance > 0:
    pyautogui.drag(distance, 0, duration=DURACAO)   # move right
    distance -= 5
    pyautogui.drag(0, distance, duration=DURACAO)   # move down
    pyautogui.drag(-distance, 0, duration=DURACAO)  # move left
    distance -= 5
    pyautogui.drag(0, -distance, duration=DURACAO)  # move up