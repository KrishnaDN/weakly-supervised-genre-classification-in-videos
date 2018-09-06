import cv2
import numpy as np
import glob
import os
from shutil import move
import multiprocessing


def extract_frames(video_path):
    video_name=video_path.split('/')[-1][:-4]
    video_name_frames='_'.join(video_name.split(' '))
    new_path='/'.join(video_path.split('/')[:-1])+'/'+video_name_frames+'.mp4'
    move(video_path,new_path)
    
    frames_folder = 'frames/'+video_path.split('/')[-2]+'/'+video_name_frames+'/images'
    audio_folder =   'frames/'+video_path.split('/')[-2]+'/'+video_name_frames+'/audio'
    if not os.path.exists(frames_folder):
        os.makedirs(frames_folder)
    if not os.path.exists(audio_folder):
        os.makedirs(audio_folder)
        
    os.system('ffmpeg -i '+new_path+' -r 1 '+frames_folder+'/'+video_path.split('/')[-2]+'_'+video_name_frames+'_frame_%05d.jpg')
    os.system('ffmpeg -i '+new_path+' -f wav '+audio_folder+'/'+'audio.wav')
    

def extract_multi(list_videos):
    pool = multiprocessing.Pool(processes=32) 
    pool.map(extract_frames, list_videos)    
  

all_folders = glob.glob('download_folder/*/')
for folder_path in all_folders:
    folder_name = folder_path.split('/')[-2]
    frames_folder='frames/'+folder_name
    if not os.path.exists(frames_folder):
        os.makedirs(frames_folder)
    videos = glob.glob(folder_path+'/*.mp4')
    extract_multi(videos)

###############################################################################

##### Create list files
###############################################################################
genres = glob.glob('frames/*/')
fid = open('file_list.txt','w')
for genre_path in genres:
    videos_path=glob.glob(genre_path+'/*/')
    for video_path in videos_path:
        all_images = glob.glob(video_path+'images/*.jpg')
        for file_path in all_images:
            to_write=file_path.split('/')[-1].split('.')[0]+'\t'+os.getcwd()+'/'+file_path
            fid.write(to_write+'\n')
fid.close()
