from pywebio.input import *

meaning = input("What is the meaning of life?") #not the built-in method
pill_color = select("Which one will you choose", ['Red Pill', 'Blue Pill'], multiple=True)
device = radio("What device are you using right now?", options=["Laptop", "Desktop", "Smartphone", "Tablet"])
os = checkbox("What operating system do you prefer for smartphones?", options=["Android", "iOS"]) 

from pywebio.output import *
from pywebio.input import * 
import time

with popup("Subscribe to the page"):
    put_text("I hope you are having a great day!")

put_markdown('## Welcome to our fruit store')
put_table([
    ['Fruit', 'Price'],
    ['Blueberry', 20],
    ['Mango', 25], 
    ['Kiwi', 15]
    ])

fruit = select("Choose your favorite Fruit", ['Blueberry', 'Mango', 'Kiwi'])
put_text(f"You chose {fruit}. Please wait until it is served!")
put_processbar('bar')
for i in range(1, 11):
    set_processbar('bar', i / 10)
    time.sleep(0.05)
put_markdown(f"Here is your {fruit}! Enjoy!")
if fruit == 'Mango':
    put_image(open('mango.jpg', 'rb').read())
elif fruit == 'Blueberry':
    put_image(open('noodle.jpg', 'rb').read())
else:
    put_image(open('kiwi.jpg', 'rb').read())
