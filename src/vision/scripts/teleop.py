#!/usr/bin/python

from pynput import keyboard
import rospy
from geometry_msgs.msg import Twist
import threading

class controller:
    def __init__(self) -> None:
        self.vel = Twist()
        self.pressed_keys = set()
        self.exit = 0
        rospy.init_node("controller")  # Initialize the ROS node
        main_thread = threading.Thread(target=self.threadPublish)
        main_thread.start()

        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()
        self.listener.join()

    def threadPublish(self):
        rate = rospy.Rate(10)
        pub = rospy.Publisher("/Diff_Drive/diff_drive_controller/cmd_vel", Twist, queue_size=10)

        while not rospy.is_shutdown() and not self.exit:
            pub.publish(self.vel)
            rate.sleep()

    def do_it(self):
        vel = Twist()
        for i in self.pressed_keys:
            if i == keyboard.KeyCode.from_char('w'):
                vel.linear.x += 1
            if i == keyboard.KeyCode.from_char('s'):
                vel.linear.x -= 1
            if i == keyboard.KeyCode.from_char('a'):
                vel.angular.z += 1
            if i == keyboard.KeyCode.from_char('d'):
                vel.angular.z -= 1
        self.vel = vel

    def on_press(self, key):
        self.pressed_keys.add(key)
        self.do_it()

    def on_release(self, key):
        try:
            self.pressed_keys.remove(key)
        except KeyError:
            pass
        
        self.do_it()

        if key == keyboard.KeyCode.from_char('q'):
            print('Escaped!')
            self.stop()
    
    def stop(self):
        self.exit = 1
        self.listener.stop()

if __name__ == "__main__":
    cont = controller()