import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist


def callback(msg, cmd_pub):
    if len(msg.data) == 0:
        return
    key_map = {'w':[0,1], 's':[0,0], 'a':[-1,0], 'd':[1,0]}
    key = msg.data[0]
    if key not in key_map:
        return
    v = key_map[key]
    tw = Twist()
    tw.linear.x = v[1]
    tw.angular.z = v[0]
    cmd_pub.publish(tw)

if __name__ == '__main__':
    rospy.init_node('key_command_translator')
    cmd_pub = rospy.Publisher('command', Twist, queue_size=1)
    rospy.Subscriber('keys', String, callback, cmd_pub)
    rospy.spin()
