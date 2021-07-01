from vidstream import *
import tkinter as tk
import threading

#local IP
import socket
local_ip_address = socket.gethostbyname(socket.gethostname()) # get provate IP Address
print(f"local ip: {local_ip_address}")

#Public IP
import requests
public_ip_address = requests.get('https://api.ipify.org').text
print(f"public ip: {public_ip_address}")

#Server that the client needs to connect to
server = StreamingServer(local_ip_address, 7777)
reciever = AudioReceiver(local_ip_address, 6666)

def start_listeting():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=reciever.start_server)
    t1.start()
    t2.start()

def start_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0, 'end-1c'), 9999)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start()

def start_screen_sharing():
    screen_client = ScreenShareClient(text_target_ip.get(1.0, 'end-1c'), 9999)
    t4 = threading.Thread(target=screen_client.start_stream)
    t4.start()

def start_audio_stream():
    audio_sender = AudioSender(text_target_ip.get(1.0, 'end-1c'), 8888)
    t5 = threading.Thread(target=audio_sender.start_stream)
    t5.start()

# Graphic User Interface
window = tk.Tk()
window.title("Call v0.0.1 Alpha")
window.geometry('300x200')

label_target_ip = tk.Label(window, text="Target IP:")
label_target_ip.pack()

text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

btn_listen = tk.Button(window, text= "Start Listening", width=50, command=start_listeting)
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_camera = tk.Button(window, text= "Start Camera Stream", width=50, command = start_camera_stream)
btn_camera.pack(anchor=tk.CENTER, expand=True)

btn_screen = tk.Button(window, text= "Start Screen Sharing ", width=50, command = start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER, expand=True)

btn_audio = tk.Button(window, text= "Start Audio", width=50, command = start_audio_stream)
btn_audio.pack(anchor=tk.CENTER, expand=True)

btn_end = tk.Button(window, text= "End Meeting", width=50, command = window.destroy)
btn_end.pack(anchor=tk.CENTER, expand=True)

window.mainloop()