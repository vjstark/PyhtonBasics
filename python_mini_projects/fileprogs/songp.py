##pp to play a song after every 1 min as a water reminder.
import pygame.mixer
import time

while True:
	time.sleep(5)
	print('chai pilo')
	pygame.mixer.init()
	pygame.mixer.music.load('song.mp3')
	pygame.mixer.music.play(1)
	time.sleep(1)
	pygame.mixer.music.stop()
