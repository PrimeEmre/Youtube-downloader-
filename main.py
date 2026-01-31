
# Youtube downlad
#Setting the youtube
import customtkinter
import yt_dlp

window = customtkinter.CTk()
window.minsize(1000,1000)
window.title("Youtube Download")
window.config(padx=2,pady=2)

#setting the backend

def downlad_btn ():
    url = url_entry.get()
    if not url:
        print("please enter a valid URL ")
        return

    options = {
        'format': 'best',
        'outtmpl': r'C:\Users\ynsem\Downloads\%(title)s.%(ext)s',
        'noplaylist': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'referer': 'https://www.youtube.com/',
    }

    try:
         with dwonlad_btn.YoutubeDL(options) as yt_dl:
            yt_dl.download([url])
            print("success!")
    except Exception as e:
        print(f"Download failed: {e}")

title_youtube = customtkinter.CTkLabel(window,text="Youtube Downloader ",font=("Roboto",34))
title_youtube.pack(pady=2)

downlad_title = customtkinter.CTkLabel(window , text="Download your video" , font=("Roboto", 18))
downlad_title.pack(pady=10 )

url_entry= customtkinter.CTkEntry(window , placeholder_text="Plase paste your Youtube link here .... ", width=400 , font=("Roboto" , 12))
url_entry.pack(pady=10)

dwonlad_btn = customtkinter.CTkButton(window,text="download now" ,font=("Roboto" ,16,),fg_color="red" , hover_color="darkred" , command= downlad_btn)
dwonlad_btn.pack()

progress_label = customtkinter.CTkLabel(window, text="0%", font=("Roboto", 12))
progress_label.pack()

progress_bar = customtkinter.CTkProgressBar(window, width=400)
progress_bar.set(0)
progress_bar.pack(pady=10)

window.mainloop()