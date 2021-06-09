import tkinter as tk 
from tkinter import ttk, Entry, messagebox, StringVar
import med,drink
MyFont =("Times New Roman", 35)

class TheElderly(tk.Tk):
	
	def __init__(self, *args, **kwargs):
		
		tk.Tk.__init__(self, *args, **kwargs)
		
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 5)
		container.grid_columnconfigure(0, weight = 5)
		self.frames = {}

		for F in (home, water_reminder, medicine_reminder):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row = 0, column = 0, sticky ="nsew")
		self.show_frame(home)


	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()


class home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="Welcome to TheElderly!!", font = MyFont)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        button2 = ttk.Button(self, text ="BMIcalculator",
        command = lambda : controller.show_frame(BMIcalculator))
        button2.grid(row = 3, column = 4, padx = 10, pady = 10)

        button1 = ttk.Button(self, text ="Medicine Reminder",
        command = lambda : controller.show_frame(medicine_reminder))
        button1.grid(row = 1, column = 4, padx = 10, pady = 10)
        
        button2 = ttk.Button(self, text ="Drink Water Reminder",
        command = lambda : controller.show_frame(water_reminder))
        button2.grid(row = 2, column = 4, padx = 10, pady = 10)
 
       

class BMIcalculator(tk.Frame):
    def bmi():
        res=int(e1.get())/int(e2.get()*int(e2.get()))
        myText.set(res)
        myText=StringVar()

    def __init__(self, parent, controller):
        myText=StringVar()
        tk.Frame.__init__(self, parent)
        l1 = ttk.Label(self, text ="Calculate your BMI", font = MyFont)
        l1.grid(row = 0, column = 1, padx = 10, pady = 10)
        ttk.Label(self, text="Height").grid(row=1)
        ttk.Label(self, text="Weight").grid(row=2)
        ttk.Label(self, text="BMI:").grid(row=5)
        BMI=ttk.Label(self, text="", textvariable=myText).grid(row=3,column=1)
            
        e1 = Entry(self)
        e2 = Entry(self)
            
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)

        res=int(e1.get())/int(e2.get()*int(e2.get()))
        x= myText.set(res)

        b = ttk.Button(self, text="Calculate", command= print("x"))
        b.grid(row=0, column=2,columnspan=2, rowspan=2, padx=5, pady=5)
        
        b1 = ttk.Button(self, text ="Home",command = lambda : controller.show_frame(home))
        b1.grid(row = 1, column = 1, padx = 10, pady = 10)

class medicine_reminder(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        l1 = ttk.Label(self, text ="Set reminder for your medicine", font = MyFont)
        l2 = ttk.Label(self, text = "Set Time")
        
        set_time = Entry(self)
        l1.grid(row = 0, column = 1, padx = 10, pady = 10)
        l2.grid(row = 1, column = 2, padx = 10, pady = 10)
        set_time.grid(row = 1, column = 4, padx = 10, pady = 10)
        
        b2 = ttk.Button(self, text ="Done",command = med)
        b2.grid(row = 2, column = 1, padx = 10, pady = 10)

        b1 = ttk.Button(self, text ="Home",command = lambda : controller.show_frame(home))
        b1.grid(row = 1, column = 1, padx = 10, pady = 10)


class water_reminder(tk.Frame):
    def drink(self):
        return 10
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        l1 = ttk.Label(self, text ="Set reminder for Drinking water", font = MyFont)
        l2 = ttk.Label(self, text = "Just click on set and we will send you text messages to drink 8 glasses of water every day!!")
        
        l1.grid(row = 0, column = 1, padx = 10, pady = 10)
        l2.grid(row = 1, column = 0, padx = 10, pady = 10)

        b2 = ttk.Button(self, text ="Set",command = water)
        b2.grid(row = 2, column = 1, padx = 10, pady = 10)
        b1 = ttk.Button(self, text ="Home",command = lambda : controller.show_frame(home))
        b1.grid(row = 1, column = 1, padx = 10, pady = 10)


app = TheElderly()
app.mainloop()