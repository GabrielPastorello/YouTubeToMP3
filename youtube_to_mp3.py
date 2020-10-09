import youtube_dl
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

def run():
    video_url = e.get()
    try:
        video_info = youtube_dl.YoutubeDL().extract_info(url=video_url, download=False)
    except:
        popupmsg('Invalid URL')

    filename = f"{video_info['title']}.mp3"

    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
        'postprocessors':[{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            }]
        }

    youtube = youtube_dl.YoutubeDL(options)
    youtube.download([video_info['webpage_url']])
    popupmsg('Success')
        
def popupmsg(msg):
    if msg == 'Invalid URL':
        response = messagebox.showinfo('Error', 'Make sure you typed the URL correctly')
    if msg == 'Success':
        response = messagebox.showinfo('MP3 File Successfully Generated', 'Check the folder where this program is located!')
    
screen = Tk()
width_of_window = 500
height_of_window = 280

screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()

x_coordinate = int((screen_width/2) - (width_of_window/2))
y_coordinate = int((screen_height/2) - (height_of_window/2))

screen.geometry("{}x{}+{}+{}".format(width_of_window, height_of_window, x_coordinate, y_coordinate))
screen.title('YouTube MP3 Converter')
screen.iconbitmap('yt.ico')
screen.config(background='#c4302b')

img = Image.open("youtube-logo.png")
resized = img.resize((260,60), Image.ANTIALIAS)
img = ImageTk.PhotoImage(resized)
Label(screen, image=img, background='#c4302b').pack(pady=20)

Label(screen, text="Enter the YouTube URL here:", font=('Helvetica', 14, 'bold'), background='#c4302b', fg='white').pack(pady=10)
e = Entry(screen, borderwidth=4, width=55)
e.pack(pady=0)
e.config(fg='black')

myButton = Button(screen, text="Generate MP3 File", command=run, fg='black', font=('Helvetica', 14, 'bold'))
myButton.pack(pady=30)

screen.mainloop()
