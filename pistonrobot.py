from piston import Piston
from time import sleep

mot = Piston(32, 33)

while True:
    try:
        speed = int(input("Enter speed (-100 to 100): "))
        mot.motgo(speed)
        sleep(1)
    except ValueError:
        print("Invalid input.")

