from pygame import init, mixer, event

init()
mixer.music.load('./add-ons/ex021.mp3')
mixer.music.play()
input()
event.wait()
