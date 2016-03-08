#!/usr/bin/env python

import sys
import rospy
from rtabmap_ros.srv import *

def usage():
    return "%s []"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print usage()
        sys.exit(1)

    print "Waiting for service to become ready..."
    rospy.wait_for_service('publish_map')

    try:
        print "Requesting map publication from RTAB"
        rtab_publish_map = rospy.ServiceProxy('publish_map', PublishMap)
        return rtab_publish_map(True, True, False)
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e