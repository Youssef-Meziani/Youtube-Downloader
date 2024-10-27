from pytube import YouTube
import os
from time import sleep

while True:
    os.system("cls")
    url = input("\u001b[37;1mEnter The Youtube URL : \u001b[0m")
    print("\u001b[35mGetting URL Info...\u001b[0m")
    yt = YouTube(url)

    print("\n\u001b[34mVideo Title : \u001b[0m", yt.title)
    print("\u001b[34mVideo length : \u001b[0m", "{:.2f}".format(float(yt.length)/60), "min")
    if yt.views < 1000:
        print("\u001b[34mVideo Views : \u001b[0m", yt.views)
    elif yt.views >= 1000 | yt.views <= 1000000:
        print("\u001b[34mVideo Views : \u001b[0m", str(int(yt.views/1000))+"K")
    elif yt.views >= 1000000:
        print("\u001b[34mVideo Views : \u001b[0m", "{:.1f}".format(float(yt.views/1000000))+"M")
    print("\u001b[34mVideo Publish Date : \u001b[0m", yt.publish_date)
    print("\u001b[34mVideo Author : \u001b[0m", yt.author)

    print("\n\u001b[33;1m-----Streams-----\u001b[0m")
    print("\u001b[33;1m1.\u001b[0m Video")
    print("\u001b[33;1m2.\u001b[0m Only Video")
    print("\u001b[33;1m3.\u001b[0m Only Audio")
    print("\u001b[33;1m4.\u001b[0m All The Streams")

    choice = input("\nSelect what you want to download : ")

    while choice >= "5" or choice <= "0":
        choice = input("\n\u001b[31mUnavailable Option,\u001b[0m Try Again : ")
    if choice == "1":
        i = 1
        for s in yt.streams.filter(progressive=True).order_by('resolution').desc():
            print(str(i)+".", s)
            i += 1
    elif choice == "2":
        i = 1
        for s in yt.streams.filter(only_video=True).order_by('resolution').desc():
            print(str(i)+".", s)
            i += 1
    elif choice == "3":
        i = 1
        for s in yt.streams.filter(only_audio=True):
            print(str(i)+".", s)
            i += 1
    elif choice == "4":
        i = 1
        for s in yt.streams.order_by('type').desc():
            print(str(i)+".", s)
            i += 1

    resolution = int(input("Select The Quality To Download (itag) : "))

    file = yt.streams.get_by_itag(resolution)

    print("\n\u001b[35mDownloading...\u001b[0m ", "{:.2f}".format(float(file.filesize*9.5367431640625e-7)), "MB")

    file.download('Downloads')

    print('=' * 19)
    print("\u001b[32;1mDownload Completed\u001b[0m")
    print('=' * 19)

    action = input("\n\u001b[38;5;245mYou Want To Download Another Video (y/n) ?\u001b[0m ")

    while True:
        if action == 'n' or action == 'N' or action == 'No' or action == 'no' or action == 'NO':
            print("\nThanks for downloading :)")
            s = 3
            while s >= 0:
                print("\rExit in " + str(s), end="")
                sleep(1)
                s -= 1
            exit()
        elif action == 'y' or action == 'Y' or action == 'Yes' or action == 'yes' or action == 'YES':
            break
        action = input("\u001b[31mInvalid Input, \u001b[38;5;245mYou Want To Download Another Video (y/n) ?\u001b[0m")
