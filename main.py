
#YouTube MP4 downloader

#Setting the modules  and window
import os
import re
import customtkinter
import yt_dlp

YOUTUBE_URL_RE = re.compile(
    r'^(https?://)?(www\.)?(youtube\.com/(watch\?v=|shorts/)|youtu\.be/)',
    re.IGNORECASE,
)

# Google search result pages sometimes link to a video via a "vid:<id>" reference
# (e.g. in the #fpstate=ive fragment) instead of a real YouTube URL.
GOOGLE_VIDEO_ID_RE = re.compile(r'vid:([a-zA-Z0-9_-]{11})')


def resolve_youtube_url(url):
    if YOUTUBE_URL_RE.match(url):
        return url

    match = GOOGLE_VIDEO_ID_RE.search(url)
    if match:
        return f'https://www.youtube.com/watch?v={match.group(1)}'

    return None

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
    url = url_entry.get().strip()
    if not url:
        percentage_label.configure(text="Please enter a URL", text_color='red')
        return

    resolved_url = resolve_youtube_url(url)
    if not resolved_url:
        percentage_label.configure(
            text="That's not a YouTube video URL", text_color='red'
        )
        return

    percentage_label.configure(text="0%", text_color=('black', 'white'))
    progress_bar.set(0)

    options = {
        'format': 'best',
        'outtmpl': os.path.join(os.path.expanduser('~'), 'Downloads', '%(title)s.%(ext)s'),
        'noplaylist': True,
        'progress_hooks': [progress_hook],
        # ADD THIS LINE TO FIX THE 403 ERROR:
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }

    try:
         with yt_dlp.YoutubeDL(options) as yt_dl:
            yt_dl.download([resolved_url])
            print("success!")
    except Exception as e:
        print(f"Download failed: {e}")
        percentage_label.configure(text="Download failed - check the URL", text_color='red')

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
