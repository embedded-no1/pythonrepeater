import os
import pynput
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()
i=0
#ask the user for input on what will be typed and how many times it will be typed.
p = input("What is your sentence to be repeated?")
j=input("How many times would you like it to be repeated?")
#convert the j input into an integer
j=int(j)
lst = list(p)

#allow to sleep for 3 seconds so the correct program can be selected
time.sleep(3)
for j in range(j):
    for i in range(len(lst)):
        keyboard.tap(lst[i])
        #delay is added as some messengers cannot handle the instant typing of the program otherwise.
        time.sleep(0.05)
    keyboard.tap(Key.enter)    
    time.sleep(0.5)