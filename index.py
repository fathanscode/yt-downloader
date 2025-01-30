from yt_dlp import YoutubeDL

# Enter the YouTube video URL
video_url = input("Enter the YouTube video URL: ")

# Set options for downloading
ydl_opts = {
    'format': 'best',  # Download the best quality available
    'outtmpl': '%(title)s.%(ext)s',  # Save file as <title>.<ext>
}

# Download the video
with YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
    print("Download complete!cls")