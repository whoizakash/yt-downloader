import tkinter
import customtkinter
from pytube import YouTube


# Function
def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink,on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finishLable.configure(text="")
        video.download()
        finishLable.configure(text="Downloaded!")
    except:
        finishLable.configure(text="Download Error!", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percetage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percetage_of_completion))
    pPercentage.configure(text=per+ '%')
    pPercentage.update()

    # update progress bar
    progressBar.set(float(percetage_of_completion)/100)

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# UI
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10,pady=10)

# input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app,width=350,height=40,textvariable=url_var)
link.pack()

# asthetic
finishLable = customtkinter.CTkLabel(app, text="")
finishLable.pack()

# progress
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10,pady=10)

# Download
download = customtkinter.CTkButton(app,text="Download",command=startDownload)
download.pack(padx=10,pady=10)

# Exec
app.mainloop()