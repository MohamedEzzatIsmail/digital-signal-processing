import customtkinter
from tkinter import messagebox
import pyaudio
import wave
import numpy as np
import pygame
import numpy
import time
import sounddevice
import matplotlib.pyplot as plt
import os
import scipy.fftpack

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


frequency=0
bits = 16
sample_rate = 48000
amplitude = 2 ** (bits - 1) - 1

def E5():
    global frequency
    frequency = 695

def A4():
    global frequency
    frequency = 440

def D4():
    global frequency
    frequency = 293

def G3():
    global frequency
    frequency = 196


def play():
    pygame.mixer.pre_init(sample_rate, -bits)
    pygame.init()
    global duration
    duration = 1
    n_samples = int(round(duration * sample_rate))
    buf = numpy.zeros((n_samples, 2), dtype=numpy.int16)
    for sumple_num in range(n_samples):
        t = float(sumple_num) / sample_rate
        buf[sumple_num][0] = int(round(amplitude * numpy.sin(2 * numpy.pi * frequency * t)))
        buf[sumple_num][1] = int(round(amplitude * 0.5 * numpy.sin(2 * numpy.pi * frequency * t)))
    sound = pygame.sndarray.make_sound(buf)
    sound.play(loops=1, maxtime=int(duration * 1000))
    time.sleep(duration)

def display():
    time1 = numpy.arange(0, 0.01, 0.001 / sample_rate)
    y = amplitude * numpy.sin(2 * numpy.pi * frequency * time1)
    plt.figure(figsize=(10, 4))
    plt.plot(time1, y)
    plt.grid(True)
    plt.title("sine wave")
    plt.xlabel("time")
    plt.ylabel("amp")
    plt.show()

def play2():
    i=0
    frequency2=695
    while(i<4):
        if(i == 1):
            frequency2 = 440
        elif(i == 2):
            frequency2 = 293
        elif(i == 3):
            frequency2 = 196
        pygame.mixer.pre_init(sample_rate, -bits)
        pygame.init()
        duration = 0.5
        n_samples = int(round(duration * sample_rate))
        buf = numpy.zeros((n_samples, 2), dtype=numpy.int16)
        for sumple_num in range(n_samples):
            t = float(sumple_num) / sample_rate
            buf[sumple_num][0] = int(round(amplitude * numpy.sin(2 * numpy.pi * frequency2 * t)))
            buf[sumple_num][1] = int(round(amplitude * 0.5 * numpy.sin(2 * numpy.pi * frequency2 * t)))
        sound = pygame.sndarray.make_sound(buf)
        sound.play(loops=1, maxtime=int(duration * 1000))
        time.sleep(duration)
        i=i+1


root=customtkinter.CTk()
root.title("tune")
root.geometry('400x600')

lable=customtkinter.CTkLabel(master=root,text='Tune',text_color='#095783',font=('',40))
lable.pack(pady=10,padx=20)

tabview = customtkinter.CTkTabview(master=root, width=250)
tabview.pack(pady=20,padx=60,fill="both",expand=True)
tabview.add("NOTES")
tabview.add("Frequency")
tabview.tab("NOTES").grid_columnconfigure(0, weight=1)
tabview.tab("Frequency").grid_columnconfigure(0, weight=1)
tabview.add("Tuner")
tabview.tab("Tuner").grid_columnconfigure(0, weight=1)

lable=customtkinter.CTkLabel(master=tabview.tab("NOTES"),text='Choose The Tone',text_color='#095783',font=('',20))
lable.pack(pady=10,padx=20)

btnf=customtkinter.CTkFrame(master=tabview.tab("NOTES"))
btnf.columnconfigure(0,weight=1)
btnf.columnconfigure(1,weight=1)
btnf.columnconfigure(3,weight=1)
btnf.columnconfigure(4,weight=1)

btn1=customtkinter.CTkButton(master=btnf,text="E5",command=E5)
btn1.grid(row=0 , column=0,pady=5,padx=5)

btn2=customtkinter.CTkButton(master=btnf,text="A4",command=A4)
btn2.grid(row=0 , column=1,pady=5,padx=5)

btn3=customtkinter.CTkButton(master=btnf,text="D4",command=D4)
btn3.grid(row=1 , column=0,pady=5,padx=5)

btn4=customtkinter.CTkButton(master=btnf,text="G3",command=G3)
btn4.grid(row=1 , column=1,pady=5,padx=5)

btnf.pack(pady=10)

entry1=customtkinter.CTkEntry(master=tabview.tab("Frequency"),placeholder_text='Enter The Frequency')
entry1.pack(pady=10,padx=20)

import subprocess

def rec():
    subprocess.call(["python", "Tuner.py"])


def set():
    global frequency
    s=entry1.get()
    frequency=float(s)
def show():
    messagebox.showinfo(message=(frequency,"Hz"))

btn9 = customtkinter.CTkButton(master=tabview.tab("NOTES"),text="show",command=show)
btn9.pack(pady=10)

btn7 = customtkinter.CTkButton(master=tabview.tab("NOTES"),text="play",command=play)
btn7.pack(pady=10)

btn6 = customtkinter.CTkButton(master=tabview.tab("NOTES"),text="display",command=display)
btn6.pack(pady=10)

btn11 = customtkinter.CTkButton(master=tabview.tab("NOTES"),text="play all",command=play2)
btn11.pack(pady=10)

btn81 = customtkinter.CTkButton(master=tabview.tab("Frequency"),text="set",command=set)
btn81.pack(pady=10)

btn91 = customtkinter.CTkButton(master=tabview.tab("Frequency"),text="show",command=show)
btn91.pack(pady=10)

btn71 = customtkinter.CTkButton(master=tabview.tab("Frequency"),text="play",command=play)
btn71.pack(pady=10)

btn61 = customtkinter.CTkButton(master=tabview.tab("Frequency"),text="display",command=display)
btn61.pack(pady=10)

btn62 = customtkinter.CTkButton(master=tabview.tab("Tuner"),text="Tune",command=rec)
btn62.pack(pady=10)



def change_appearance_mode_event( new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)

appearance_mode_label = customtkinter.CTkLabel(root, text="Appearance Mode:", anchor="w")
appearance_mode_label.pack()
appearance_mode_optionemenu = customtkinter.CTkOptionMenu(root, values=["Light", "Dark"],
                                                                       command=change_appearance_mode_event)
appearance_mode_optionemenu.pack(pady=10)

appearance_mode_optionemenu.set("Dark")

root.mainloop()

