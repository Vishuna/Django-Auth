from django.shortcuts import render
from pytube import YouTube
import os
import requests
from django.http import HttpResponse
import glob
from django.conf import settings


def download_video(request):
    try:
        if request.method=="POST":
            try:
                link=request.POST['link']
                video=YouTube(link)
                print(video)

                stream=video.streams.get_lowest_resolution()
                stream.download('media/video_uploads/')

                return render(request,'video/download_video.html',{'msg':'video downloaded'})
            except:
                 return render(request,'video/download_video.html',{'msg':'video not downloaded'})
        return render(request,'video/download_video.html',{'msg':''})
    except:
        return render(request,'video/download_video.html',{'msg':"Sorry something went wrong!"})
    



def video_view(request):
    media_root=settings.MEDIA_ROOT
    media_url=settings.MEDIA_URL
    video_files=[]
    media_path=os.path.join(media_root,'video_uploads')
    for root,dirs,files in os.walk(media_path):
                for file in files:
                    file_path=os.path.join(root,file)
                    relative_path=file_path.replace(media_root,'')
                    print('mediaaaaaaaaa',relative_path)
                    video_files.append(media_url+relative_path)
    print(video_files)
    context={'video_files':video_files}
    return render(request,'video/view_video.html',context)