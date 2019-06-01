 import pyautogui

'''

left_mouse click	
right_mouse click
middle_mouse click
scroll_up
scroll_down
scroll_left
scroll_right
page_up
page_down
zoom_in
zoom_out
refresh
screenshot
volume_up
volume_down
next_track
prev_track 
play/pause


'''

 
def execute(]str):


	if str == 'left_mouse click':
		pyautogui.click( button = 'left' )
		print('kam hoise')
	elif str == 'right_mouse click':
		pyautogui.click( button = 'right' )
	elif str == 'middle_mouse click':
		pyautogui.click( button = 'middle' )
	elif str == 'scroll_up':
		pyautogui.scroll(10)
	elif str == 'scroll_down':
		pyautogui.scroll(-10)
	elif str == 'scroll_right':
		pyautogui.hscroll(10)
	elif str == 'scroll_left':
		pyautogui.hscroll(-10)
	elif str == 'page_up':
		pyautogui.press('pgup')
	elif str == 'page_down':
		pyautogui.press('pgdn')
	elif str == 'zoom_out':
		pyautogui.keydown('shift')
		pyautogui.press('+')
		pyautogui.keyup('shift')
	elif str == 'zoom_in':
		pyautogui.keydown('shift')
		pyautogui.press('-')
		pyautogui.keyup('shift')
	elif str == 'refresh':
		pyautogui.press('f5')
	elif str == 'screenshot':
		pyautogui.screenshot()
	elif str == 'volume_up':
		pyautogui.press('volumeup')
	elif str == 'volume_down':
		pyautogui.press('volumedown')
	elif str == 'next_track':
		pyautogui.press('nexttrack')
	elif str == 'prev_track':
		pyautogui.press('prevtrack')
	elif str == 'play/pause':
		pyautogui.press('playpause')