from django.shortcuts import render
from pytube import YouTube
import os
import requests
from django.http import HttpResponse


def download_video(request):
    try:
        if request.method=="POST":
            try:
                link=request.POST['link']
                video=YouTube(link)
                print(video)

                stream=video.streams.get_lowest_resolution()
                stream.download('media/video_uploads/')

                return render(request,'video/video.html',{'msg':'video downloaded'})
            except:
                 return render(request,'video/video.html',{'msg':'video not downloaded'})
        return render(request,'video/video.html',{'msg':''})
    except:
        return render(request,'video/video.html',{'msg':"Sorry something went wrong!"})
    