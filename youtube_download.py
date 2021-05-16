
'''

Youtube Downloader

Current functionalities :
Accepts user URL, 
Checks whether it is valid, otherwise gives error message,
Download either as video, or mp3
Select download path

Possible additions:
User option to specify file name


'''

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube
from PIL import ImageTk
import os

#default download directory
file1 = "C:/Users/HP/Downloads"

root = Tk()
root.geometry('500x300+550+250')
root.resizable(0,0)
root.title("YouTube Video Downloader")

background_image=ImageTk.PhotoImage(file = "C:\\Users\\HP\\Desktop\\Python programs\\1353663.jpg")
background_label = Label(root, image =background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


heading = Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold',bg = "yellow") 
heading.pack(pady = 10)



##enter link
link = StringVar()

paste = Label(root, text = 'Paste Link Here:', font = 'arial 15',bg = "yellow") #.place(x= 160 , y = 60)
paste.place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link) #.place(x = 32, y = 100)
link_enter.place(x = 32, y = 100)


#function to download video
def Downloader():

    try: 
        url =YouTube(str(link.get()))
        video = url.streams.first()
        video.download(output_path=file1) # File path where downloaded file is stored
        messagebox.showinfo("Pop up", "Download complete!")

    except:
        error()

#function to download mp3
def get_audio():

    try: 
        url =YouTube(str(link.get()))
        video = url.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=file1) # File path where downloaded file is stored
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        messagebox.showinfo("Pop up", "Download complete!")

    except:
        error()

#function to get the title of the video
def get_title():

    try: 
        url =YouTube(str(link.get()))
        video_title = url.title
        messagebox.showinfo("Video Title", video_title)

    except:
        error()

#function invoked when incorrect url is entered
def error():
    messagebox.showinfo("ERROR", "Video not found! Check URL and try again.")


#function invoked for download path selection
def path_selection():
    global file1
    file1 = filedialog.askdirectory()
    if file1 == '':
        file1 = "C:/Users/HP/Downloads"
    messagebox.showinfo("Download Path", "Current Download Path : " + file1)

#button to check title
check_title = Button(root,text = 'Check Video Title', font = 'arial' ,bg = 'yellow', command = get_title)
check_title.place(x=10 ,y = 130)

#button to download video
download = Button(root,text = 'Download', font = 'arial 15' ,bg = 'yellow', padx = 2, command = Downloader)
download.place(x=182 ,y = 130)

#button to download mp3
audio_download = Button(root,text = 'Download as mp3', font = 'arial' ,bg = 'yellow', padx = 2, command = get_audio)
audio_download.place(x=288 ,y = 130)

#option to select download path
download_path = Button(root,text = 'Select file path', font = 'arial', bg = 'yellow', padx = 2, command = path_selection)
download_path.place(x = 165, y = 180)


root.mainloop()
