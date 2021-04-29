from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import os
from pygame import mixer
mixer.init()
root = Tk()
musicfiles=[]

musicExts=['.mp3','.aac','.wav','.aa']
index=0
n=0


def song_folder():
    global musicfiles,directory
    directory= filedialog.askdirectory()
    os.chdir(directory)
    musicfiles=[file for file in os.listdir(directory) if os.path.splitext(file)[1].lower() in musicExts]
    print(musicfiles)
    

def about_Us():
    tkinter.messagebox.showinfo('Information','Music player by WM')

def vol_set(val):
    volume=int(val)/100
    mixer.music.set_volume(volume)

def playsong():
    try:
        mixer.music.load(musicfiles[index])
        mixer.music.play()
    except:
        tkinter.messagebox.showerror('LISTEN','No files Found!Go to Open.')

def nextsong():
    global index 
    index+=1
    mixer.music.load(musicfiles[index])
    mixer.music.play()

def presong():
    global index 
    index-=1
    mixer.music.load(musicfiles[index])
    mixer.music.play()

def stopsong():
    global n
    if n%2==0:
        mixer.music.stop()
        n+=1
    else:
        mixer.music.load(musicfiles[index])
        mixer.music.play()
        n+=1







root.title("LISTEN")
root.geometry('350x400')
root.iconbitmap(r'C:\Users\Wasim\Desktop\desktop junks\Visual code\music.ico')
menubar=Menu(root)
root.config(menu=menubar)
submenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=submenu)
submenu.add_command(label='Open',command=song_folder)
submenu.add_command(label='Exit',command=root.destroy)
submenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=submenu)
submenu.add_command(label='About Us',command=about_Us)



#.....................buttons
playbutton=Button(root,text='Play',command=playsong)
playbutton.pack()
nextbutton=Button(root,text='Next',command=nextsong)
nextbutton.pack()
previousbutton=Button(root,text='Previous',command=presong)
previousbutton.pack()
stopbutton=Button(root,text='Stop',command=stopsong)
stopbutton.pack()
scale=Scale(root,from_=0,to=100,orient=HORIZONTAL,command=vol_set)
scale.set(60)
mixer.music.set_volume(0.6)
scale.pack()
statusbar=Label(root,text='Enjoy Music...',relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM,fill=X)





root.mainloop()
