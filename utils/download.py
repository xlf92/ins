import json
import os
import re
import time
import flickrapi
import requests
import imghdr
import math

def save_csv_file(List, filePath, mode):
    try:
        file = open(filePath, mode)
        for item in List:
            item = str(item).encode('gbk',errors='replace').decode('gbk')
            if item=='':
                item='None'
            file.write(item.replace("\n",". ").replace("\r",". ").replace("\t",". ").replace(",",". ")+',')
        file.write("\n") 
    except Exception :
        print("write data error!")
    finally:
        file.close()

def save_media(media_link, user_id, photo_id):
    if not os.path.exists('images/'+ user_id):
        os.makedirs('images/'+ user_id)
    save_path = 'images/'+ user_id + '/' + photo_id + '.jpg'
    if not os.path.exists(save_path) or not imghdr.what(save_path): 
        try:
            media = requests.get(media_link)
            with open(save_path,'wb') as f:
                f.write(media.content)
        except:
            print("save media fail: "+save_path+'\n'+media_link)


if __name__=='__main__':

    with open('user_list.csv', 'r', encoding='utf-8') as f:
        user_list = f.read().splitlines()