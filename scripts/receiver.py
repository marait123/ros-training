#!/usr/bin/env python2
import rospy
from std_msgs.msg import String, Float64
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan

def subscriberCallBack(data):
    rospy.loginfo("\n============================================================\n")
    rospy.loginfo(rospy.get_caller_id() + " I recieved the following --  %s", data) #prints on terminal
    rospy.loginfo("\n============================================================\n")
    
def listener():
    rospy.init_node('subscriberNode', anonymous=True)
    rospy.Subscriber("scan", LaserScan, subscriberCallBack)
    rospy.spin() # the python file does not exit

if __name__ == '__main__':
    listener()