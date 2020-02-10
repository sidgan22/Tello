import tello
import time

drone = tello.Tello('192.168.10.3', 8888)
drone.command('command')
time.sleep(5)
drone.takeoff()
time.sleep(5)
drone.move('forward',0.10)
time.sleep(5)
drone.command('take picture')
time.sleep(2)
drone.move_backward(50)
drone.flip('l')
time.sleep(2)
drone.land()