'''
Created on Sep 18, 2016

@author: rezecib
'''
#tk.Scale -> slider

import Tkinter as tk
import cv2
from PIL import Image, ImageTk

class Window(tk.Tk, object):
	
	def __init__(self):
		super(Window, self).__init__()
		
		frame_control = tk.Frame(self)
		button_openVideo = tk.Button(frame_control, text="Open video...")
		button_openVideo.pack(side=tk.LEFT)
		frame_control.pack(side=tk.LEFT)
		
		frame_video = tk.Frame(self) #Will need to graduate to its own subclass at some point
		video = cv2.VideoCapture("input/C_6.avi") #Note: Framerate is 1 per 33ms
		img = ImageTk.PhotoImage(image=Image.fromarray(video.read()[1]))
		label_video = tk.Label(frame_video, image=img)#text="There will be a video here soon!")
		label_video.pack()
		frame_video.pack(side=tk.RIGHT)

		
# 		w = tk.Label(self, text="Hello, world!")
# 		w.pack()
		
		self.mainloop()
