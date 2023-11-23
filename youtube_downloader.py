import os
from pytube import YouTube
from pytube import Playlist
from typing import Any, Callable, Optional
import requests

def download_image(url, file_name):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f"Image downloaded as '{file_name}'")
        else:
            print("Failed to download the image")
    except requests.RequestException as e:
        print(f"Error downloading the image: {e}")
        

def YouTube_Audio_Downloader(save_path: str, download_link: str) -> str:
		URL = None
		
		if os.path.exists(save_path):	
			try:
                            #in case you want to bypass age gate you need to login
				URL = YouTube(download_link##, use_oauth=True, allow_oauth_cache= True)
				)
                
				URL.streams.filter(only_audio = True).order_by('abr').desc().first().download(save_path, filename = URL.title + ".mp3")           
				download_image(URL.thumbnail_url, save_path + "/" + URL.title + ".jpg")
				return URL.title
			except Exception as ex:
				print("Got Error:" + ex.args)
				return None						
		else:
			print("Saving Path Not Exist")
			return None
			
