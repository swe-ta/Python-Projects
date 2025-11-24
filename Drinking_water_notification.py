import time
from plyer import notification

if __name__ == "__main__":
    while True:
         notification.notify(
           title = "**Please Drink Water Now!!",
           message = "Women should have about 2 litres (8 cups) of fluids a day, and men about 2.6 litres (10 cups)",
           app_icon = r"E:\Python\icons.ico",
           timeout = 12
         )
         time.sleep(1800)
         # time.sleep(6)
