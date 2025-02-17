from tkinter import *
import tkinter as tk

from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz



root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

#change the color of the background
baseColor = "#81d4fa"
root.configure(bg=baseColor)



def update_time(home):
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M:%S:%p")
    clock.config(text=current_time)
    clock.after_id = clock.after(1000, update_time, home)

def getWeather():
    try:
        city = textfield.get()

        geolocator = Nominatim(user_agent="WeatherApp/1.0")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        

        home = pytz.timezone(result)

        name.config(text="CURRENT TIME")
        if hasattr(clock, 'after_id'):
            clock.after_cancel(clock.after_id)
        update_time(home)
        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=e18b677fa487ce423a66bd818d725dcd"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] -273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']


        if temp > 30:
            feel = "HOT"
        elif temp >20 and temp < 30:
            feel = "NORMAL"
        elif temp > 10 and temp < 20: 
            feel = "COLD"
        elif temp < 10:
            feel = "FREEZING"
        
        t.config(text=(temp, "°"))
        c.config(text=(condition, "|", "FEELS", "LIKE", feel))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
        
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!!")
    
    






    

#search box
Search_image = PhotoImage(file="search.png")
myimage = Label(image=Search_image, bg=baseColor)
myimage.place(x=20, y=20)

textfield=tk.Entry(root,justify="center", width=17, font = ("poppins", 25 , "bold"), bg="#404040", border=0, fg = "white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

#logo
Logo_image = PhotoImage(file="logo.png")
Logo = Label(image=Logo_image)
Logo.place(x=650, y=0)

#Bottom box
Frame_image = PhotoImage(file="box.png")
frame_myimage = Label(image=Frame_image, bg=baseColor)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)


#time
name = Label(root, font=("arial", 15, "bold"), bg = baseColor)
name.place(x=30, y=100)
clock= Label(root, font=("Helvetica", 20), bg = "white")
clock.place(x=30, y=130) 

#Label
label1 = Label(root,text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120,y=400)

label2 = Label(root,text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=225,y=400)

label3 = Label(root,text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=430,y=400)

label4 = Label(root,text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=("arial", 70, "bold"), fg="#ee666d", bg = baseColor)
t.place(x=400, y=150)
c=Label(font=("arial", 15, "bold"), bg = baseColor)
c.place(x=400, y=250)

w=Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=130, y=430)
h=Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=260, y=430)
d=Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=480, y=430)
p=Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=690, y=430)



root.mainloop()





#!python
