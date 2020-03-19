import tkinter as tk
from tkinter import messagebox
from tkinter import Text
import random
import csv
from datetime import datetime
import os.path
import sys

def decide_workout(seed):
	random.seed(seed)
	myint = (random.randint(1,10))
	workout = None
	if myint == 1:
	  workout = ("Your health challenge today is to go the whole day without eating bread! Good luck!")
	elif myint == 2:
	  workout = ("Your health challenge today is to go to the gym for at least an half an hour! Best of luck!")
	elif myint == 3:
	  workout = ("Your health challenge today is no sweets/junk food today! Godspeed!")
	elif myint == 4:
	  workout = ("Your health challenge today is to go for a walk! You can do it!")
	elif myint == 5:
	  workout = ("Your health challenge today is to get at least 8 hours of sleep! This one's easy!")
	elif myint == 6:
	  workout = ("Your health challenge today is to drink at least a gallon of water! Chug, chug, chug!")
	elif myint == 7:
	  workout = ("Your health challenge today is to eat home-cooked, healthy meals! Health is wealth!")
	elif myint == 8:
	  workout = ("Your health challenge today is to meditate/pray/stretch for at least 15 minutes! Your mind is your strongest muscle!")
	elif myint == 9:
	  workout = ("Your health challenge today is to not sit down for more than an hour at a time! Get off your butt!")
	else:
	  workout = ("Make up your own health challenge! But run it by Shrey or Shaurya to make sure that it is hard enough! Have fun!")
	return workout

def schedule(time, workout):
	exercise = False
	root= tk.Tk()
	canvas1 = tk.Canvas(root, width = 500, height = 125)
	canvas1.pack()
	if time == 1:
		button1 = tk.Button(root, text='View My Workout',command=lambda: first_time(root, workout),bg='green',fg='white')
		canvas1.create_window(250, 100, window=button1)
		canvas1.create_text(250,35,fill="darkblue",font="Times 20 italic",
		                        text="Good morning! Hope you are ready for a healthy and happy day!", width = 400)
		root.mainloop()
	elif time == 2:
		# root.withdraw()
		temp = "Reminder: " + str(workout)
		canvas1.create_window(250, 120)
		canvas1.create_text(250,50,fill="darkblue",font="Times 20 italic",
		                        text=temp, width = 400)
		MsgBox = tk.messagebox.askquestion('Response', "Good Afternoon? Did you complete your workout?")
		if MsgBox == 'yes':
			exercise = True
			tk.messagebox.showinfo('Return','Awesome! Good Job :)')
			root.destroy()
		else:
			exercise = False
			tk.messagebox.showinfo('Return','You will be marked off for today :(')
			root.destroy()
		write_csv(exercise)

def first_time(root, workout):
	# MsgBox = tk.messagebox.showinfo('Your Workout', workout)
	root.destroy()
	nroot = tk.Tk()
	canvas2 = tk.Canvas(nroot, width = 500, height = 140)
	canvas2.pack()
	button2 = tk.Button(nroot, text='Sounds Good', command = lambda: nroot.destroy(), bg='green',fg='white')
	canvas2.create_window(250, 120, window = button2)
	canvas2.create_text(250,50,fill="darkblue",font="Times 20 italic",
		                        text=workout, width = 400)
	nroot.mainloop()

def date_stuff():
	months = ["None", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
	a = str(datetime.now())
	curr_date = a.rsplit(' ', 1)[0]
	datee = datetime.strptime(curr_date, "%Y-%m-%d")
	month = months[datee.month]
	day = datee.day
	return month, day

def write_csv(exercise):
	month, day = date_stuff()
	val = 1 if exercise else 0
	csv_title = "workout" + str(month) + ".csv"
	csv_exists = os.path.isfile(csv_title)
	if csv_exists:
		with open(csv_title, "a", newline = '') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow([day, val])
	else:
		with open(csv_title, "w+", newline = '') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow(["Date", "Workout"])
			writer.writerow([day, val])

def execute(args):
	month, day = date_stuff()
	seed = month * day
	designated_workout = decide_workout(seed)
	print(designated_workout)
	schedule(args, designated_workout)

args = int(sys.argv[1:][0])
execute(args)
