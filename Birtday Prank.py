import pyautogui
import random
import time

birthday_messages_for_krishna = [
    "Happy birthday, dear Krishna! May this special day bring you immense joy, laughter, and unforgettable moments.",
    "Wishing my wonderful friend Krishna a very happy birthday! May the coming year be filled with success and happiness.",
    "Happy birthday to the coolest person I know, Krishna! May your day be as awesome as you are!",
    "Sending you warmest birthday wishes, Krishna! May this new year of your life be filled with love, prosperity, and great adventures.",
    "Happy birthday, Krishna! May you continue to spread positivity and brighten the lives of everyone around you.",
    "To my dearest friend Krishna, wishing you a year full of accomplishments, good health, and happiness. Happy birthday!",
    "Happy birthday, Krishna! May your dreams take flight and may you achieve everything you've ever desired.",
    "On your special day, Krishna, I wish you love, laughter, and all the beautiful things life has to offer. Happy birthday!",
    "To my incredible friend Krishna, may your birthday be as extraordinary as you are. Have a fantastic day!",
    "Happy birthday, Krishna! Your friendship has been a blessing in my life, and I'm grateful for every moment we've shared.",
    "Wishing a very happy birthday to the most amazing friend, Krishna! May you be surrounded by love and cherished by those who matter most.",
    "Happy birthday, Krishna! May your birthday be as bright and colorful as your wonderful personality.",
    "Warmest birthday wishes to my dear friend Krishna! May this year be a stepping stone towards your dreams.",
    "Happy birthday, Krishna! May the happiness you bring to others come back to you tenfold on your special day.",
    "To my dear friend Krishna, may this birthday be the beginning of a new chapter filled with love, success, and endless blessings."
]


def send_random_message():
    time.sleep(0.5)
    message = random.choice(birthday_messages_for_krishna)
    pyautogui.typewrite(message)
    pyautogui.press('enter')


while True:
    send_random_message()


