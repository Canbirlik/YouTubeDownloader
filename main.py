import pytube

url = input("Please, enter the Youtube Video Link: ")

path = ""

try:
    pytube.YouTube(url).streams.get_highest_resolution().download(path)
except:
    print("An error has occurred")
else:
    print("Download is completed successfully")






