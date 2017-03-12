#!/usr/bin/env/python
import sys, tty, termios
import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    pub = rospy.Publisher('keys', String, queue_size=1)
    rospy.init_node('keyboard')
    rate = rospy.Rate(100)
    tty.setcbreak(sys.stdin.fileno())
    print 'Listening. WASD to move, q to quit.'
    while not rospy.is_shutdown():
        key = sys.stdin.read(1)
        if key == 'q':
            break
        pub.publish(key)
        
