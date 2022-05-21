from pynput.keyboard import Key, Controller
import time
import random
#you need to clock into a text chat or somewhere you can write and it will write automacitally
keyboard = Controller()

input_message = input('bot will send ->')
message = input_message #you choose what you want bot to write and send

input_waittime = input('how many seconds until start ->')

print('programme will now send', input_message, 'until you end it')
print(input_waittime, 'seconds to proceed, you can end it by CTR + C')

time.sleep(int(input_waittime))#you schoose time programme have to wait until start

for word in range(1000000): #bot will basically write until you stop it
    for letter in message:
        keyboard.press(letter)
        keyboard.release(letter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randrange(3)+1) #random time waiting for executing another message
