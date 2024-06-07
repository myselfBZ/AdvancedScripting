from pytube import YouTube

url = input("Enter the url: ")
yt = YouTube(url)
print("Title: ", yt.title)
print("Views: ", yt.views)
print("Length: ", yt.length, "seconds")
yt.download("your path")
