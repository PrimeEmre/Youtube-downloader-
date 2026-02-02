
#YouTube MP4 downloader

#Setting the modules  and window
import customtkinter
import yt_dlp

window = customtkinter.CTk()
window.minsize(1000,1000)
window.title("Youtube Download")
window.config(padx=2,pady=2)

#setting the backend

#Setting the progress bar
def progress_hook(d):
    if d['status'] == 'downloading':
        # Use .get to prevent crashes if the values are missing
        total = d.get('total_bytes') or d.get('total_bytes_estimate')
        downloaded = d.get('downloaded_bytes', 0)

        if total:
            percentage_decimal = downloaded / total

            progress_bar.set(percentage_decimal)
            percentage_label.configure(text=f"{int(percentage_decimal * 100)}%")
            window.update_idletasks()  # This "forces" the 0% to change

    elif d['status'] == 'finished':
        percentage_label.configure(text="100% - You are good to go", text_color='green')
        progress_bar.set(1)



# Setting the MP4 downloader
def downlad_btn ():
    url = url_entry.get()
    if not url:
        print("please enter a valid URL ")
        return

    options = {
        'format': 'best',
        'outtmpl': r'C:\Users\ynsem\Downloads\%(title)s.%(ext)s',
        'noplaylist': True,
        'progress_hooks': [progress_hook],
        # ADD THIS LINE TO FIX THE 403 ERROR:
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }

    try:
         with yt_dlp.YoutubeDL(options) as yt_dl:
            yt_dl.download([url])
            print("success!")
    except Exception as e:
        print(f"Download failed: {e}")

#Setting the UI

title_youtube = customtkinter.CTkLabel(window,text="Youtube Downloader ",font=("Roboto",34))
title_youtube.pack(pady=2)

downlad_title = customtkinter.CTkLabel(window , text="Download your video" , font=("Roboto", 18))
downlad_title.pack(pady=10 )

url_entry= customtkinter.CTkEntry(window , placeholder_text="Plase paste your Youtube link here .... ", width=400 , font=("Roboto" , 12))
url_entry.pack(pady=10)

dwonlad_btn = customtkinter.CTkButton(window,text="download now" ,font=("Roboto" ,16,),fg_color="red" , hover_color="darkred" , command= downlad_btn)
dwonlad_btn.pack()

percentage_label = customtkinter.CTkLabel(window, text="0%", font=("Roboto", 12))
percentage_label.pack()

progress_bar = customtkinter.CTkProgressBar(window, width=400)
progress_bar.set(0)
progress_bar.pack(pady=10)

window.mainloop()
