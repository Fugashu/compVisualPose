#for our dataset publish necessary tf
#!/usr/bin/env python
import rospy
import sys
import tf
import tf2_ros
import geometry_msgs.msg

if __name__ == '__main__':
        rospy.init_node('my_static_tf2_broadcaster')
        broadcaster = tf2_ros.StaticTransformBroadcaster()              
        static_transformStamped2 = geometry_msgs.msg.TransformStamped()
        static_transformStamped2.header.stamp = rospy.Time.now()
        static_transformStamped2.header.frame_id = "camera_link" 
        static_transformStamped2.child_frame_id = "camera_color_optical_frame"
        static_transformStamped2.transform.translation.x = 0.0
        static_transformStamped2.transform.translation.y = 0.015
        static_transformStamped2.transform.translation.z = 0.0
        quat = tf.transformations.quaternion_from_euler(-3.1415926535897931/2, 0, -3.1415926535897931/2)
        static_transformStamped2.transform.rotation.x = quat[0]
        static_transformStamped2.transform.rotation.y = quat[1]
        static_transformStamped2.transform.rotation.z = quat[2]
        static_transformStamped2.transform.rotation.w = quat[3]
        static_transformStamped5 = geometry_msgs.msg.TransformStamped()
        static_transformStamped5.header.stamp = rospy.Time.now()
        static_transformStamped5.header.frame_id = "camera_link" 
        static_transformStamped5.child_frame_id = "camera_imu_optical_frame"
        static_transformStamped5.transform.translation.x = 0.0117399999872
        static_transformStamped5.transform.translation.y = 0.00552000012249
        static_transformStamped5.transform.translation.z = -0.00510000018403        
        static_transformStamped5.transform.rotation.x = -0.5
        static_transformStamped5.transform.rotation.y = 0.5
        static_transformStamped5.transform.rotation.z = -0.5
        static_transformStamped5.transform.rotation.w = 0.5
		static_transformStamped4 = geometry_msgs.msg.TransformStamped()
        static_transformStamped4.header.stamp = rospy.Time.now()
        static_transformStamped4.header.frame_id = "base_footprint"
        #odom2 here because this is gonna be the startpoint of viso for ccny
        static_transformStamped4.child_frame_id = "camera_link" 
        #for evo including the transform from mount to camera_link which is 0.0 0.0175 0.0125
        static_transformStamped4.transform.translation.x = 0.325+0.0
        static_transformStamped4.transform.translation.y = 0.0+0.0175
        static_transformStamped4.transform.translation.z = 0.2125+0.0125
        quat = tf.transformations.quaternion_from_euler(0,0,0)
        static_transformStamped4.transform.rotation.x = quat[0]
        static_transformStamped4.transform.rotation.y = quat[1]
        static_transformStamped4.transform.rotation.z = quat[2]
        static_transformStamped4.transform.rotation.w = quat[3]
		
        
        broadcaster.sendTransform([static_transformStamped2,static_transformStamped4,static_transformStamped5])
        
        rospy.spin()
		'''some algorithms required other names for the child frame id you find them below
		static_transformStamped3 = geometry_msgs.msg.TransformStamped()
        static_transformStamped3.header.stamp = rospy.Time.now()        
        static_transformStamped3.header.frame_id = "base_footprint"
        #odom2 here because this is gonna be the startpoint of viso for ccny
        static_transformStamped3.child_frame_id = "odom2" 
        static_transformStamped3.transform.translation.x = 0.078
        static_transformStamped3.transform.translation.y = 0.0175
        static_transformStamped3.transform.translation.z = 0.715
        quat = tf.transformations.quaternion_from_euler(0,0,0)
        static_transformStamped3.transform.rotation.x = quat[0]
        static_transformStamped3.transform.rotation.y = quat[1]
        static_transformStamped3.transform.rotation.z = quat[2]
        static_transformStamped3.transform.rotation.w = quat[3]             
		static_transformStamped = geometry_msgs.msg.TransformStamped()
        static_transformStamped.header.stamp = rospy.Time.now()
        static_transformStamped.header.frame_id = "camera_link"
        static_transformStamped.child_frame_id = "asus"
        static_transformStamped.transform.translation.x = 0.0
        static_transformStamped.transform.translation.y = 0.0 #0.015
        static_transformStamped.transform.translation.z = 0.0
        quat = tf.transformations.quaternion_from_euler(-3.1415926535897931/2,0,-3.1415926535897931/2)
        static_transformStamped.transform.rotation.x = quat[0]
        static_transformStamped.transform.rotation.y = quat[1]
        static_transformStamped.transform.rotation.z = quat[2]
        static_transformStamped.transform.rotation.w = quat[3]'''		
		#rosrun tf static_transform_publisher 0.0929 0.0325 0.0705 1.5707963 0 -1.5707963 base_footprint Opencv 100
		#for turtlebot
        '''static_transformStamped4.transform.translation.x = 0.078
        static_transformStamped4.transform.translation.y = 0.0175
        static_transformStamped4.transform.translation.z = 0.715
        quat = tf.transformations.quaternion_from_euler(0,0,0)
        static_transformStamped4.transform.rotation.x = quat[0]
        static_transformStamped4.transform.rotation.y = quat[1]
        static_transformStamped4.transform.rotation.z = quat[2]
        static_transformStamped4.transform.rotation.w = quat[3]'''
