from pytube import YouTube

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video.download(save_path)
        print("Download successful!")
    except Exception as e:
        print("Download failed:", str(e))

# Example usage:
video_url = "https://www.youtube.com/watch?v=ORrrKXGx2SE"
save_location = "test_files/walking.mp4"
download_video(video_url, save_location)

