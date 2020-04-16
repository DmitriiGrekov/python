from pytube import YouTube
a = input("Введите ссылку на видео: ").strip()
YouTube(a).streams.first().download()
