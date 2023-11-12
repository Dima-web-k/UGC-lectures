import cv2
from pvrecorder import PvRecorder
import wave
import os
import struct
import threading
from moviepy.editor import VideoFileClip, AudioFileClip

output_mp4=0
stop=0
output_wav=0
def AudioRecord():
    global stop
    global output_wav
    recorder = PvRecorder(device_index=-1, frame_length=512)
    audio = []

    try:
        recorder.start()

        while True:
            frame = recorder.read()
            audio.extend(frame)
            if stop == True:
                break
        recorder.stop()
        with wave.open(os.getcwd() + '\\' + output_wav, 'wb') as f:
            f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
            f.writeframes(struct.pack("h" * len(audio), *audio))
    finally:
        recorder.delete()

def VideoRecord():
    global stop
    global output_mp4
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 24)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    codec = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_mp4, codec, 25.0, (1280, 720))

    while True:
        ret, frame = cap.read()
        cv2.imshow('Web-camera', frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            stop = True
            break

    out.release()
    cap.release()
    cv2.destroyAllWindows()


def main():
    videotitle = input("Enter video title: ")
    clas = input("Enter class number: ")
    filename = clas + ' класс. ' + videotitle + '.mp4'
    global output_mp4
    global output_wav
    output_mp4 = 'output.mp4'
    output_wav = 'output.wav'

    audioThread = threading.Thread(target=AudioRecord)
    videoThread = threading.Thread(target=VideoRecord)
    global stop
    stop = False
    audioThread.start()
    videoThread.start()
    audioThread.join()
    videoThread.join()

    video = VideoFileClip(os.getcwd() + '\\' + output_mp4)
    audio = AudioFileClip(os.getcwd() + '\\' + output_wav)
    video = video.set_audio(audio)
    video.write_videofile(os.getcwd() + '\\classes\\' + clas + '\\' + filename, codec='libx264', audio_codec='aac')

    os.remove(os.getcwd() + '\\' + output_mp4)
    os.remove(os.getcwd() + '\\' + output_wav)