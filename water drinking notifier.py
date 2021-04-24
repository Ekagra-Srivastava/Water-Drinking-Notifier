import time
from plyer import notification

if __name__ == '__main__':

 	notification.notify(
 		app_name="Water Assistant",
 		title = ":) HEY THERE, TAKE A SHORT BREAK AND DRINK SOME WATER :)",
 		message ="Adequate daily fluid intake is: "
				 "About 15.5 cups (3.7 liters) of fluids for men. "
				 "About 11.5 cups (2.7 liters) of fluids a day for women.",
 		app_icon ="F:\cup-with-straw.ico",
 		timeout=12


    )
time.sleep(60*60)