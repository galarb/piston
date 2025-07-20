from piston import Piston
from time import sleep
mot = Piston(33, 32)

try:
    mot.motgo(100)
    sleep(1)
    mot.motgo(-100)
    sleep(10)
    mot.motgo(0)
except Exception as e:
    print("Error in motgo:", e)
