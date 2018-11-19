import cv2
import os
import glob
import sys
from skvideo.io import FFmpegWriter
import glob

def frames2vid(dir_path, output):
    images = []
    for f in glob.glob(dir_path + "/*.jpg"):
        images.append(f)
    images.sort()
    frame = cv2.imread(images[0])
    height, width, layers = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'DIVX') 

    video = cv2.VideoWriter(output, fourcc, 60, 1, (width,height))

    for image in images:
        video.write(cv2.imread(image))

    #cv2.destroyAllWindows()
    video.release()
    print("The output video is {}".format(output))
 

def frames2vid_2(dir_path, output):
    images = []

    for f in glob.glob(dir_path + "/*.jpg"):
        images.append(f)
    images.sort()
    # Define the codec and create VideoWriter object
    writer = FFmpegWriter(output, outputdict={'-r': 60})
    for i in range(len(images)):
        # Modify below based on file names
        frame = cv2.imread(dir_path + 'frame' + str(i) + '.jpg')
        writer.writeFrame(frame) # Write out frame to video
    # Release everything if job is finished
    writer.close()
    print("The output video is {}".format(output))
    
    
if __name__ == '__main__':
    if not len(sys.argv) == 3:
        print('Usage: python frames2vid.py frames_dir video_output')
        exit()
    else:
        frames_dir = sys.argv[1]
        video_output = sys.argv[2]
        frames2vid_2(frames_dir, frames_dir + video_output) 
