#include <ros/ros.h>
#include <tf/transform_broadcaster.h>

int main(int argc, char** argv){
    ros::init(argc, argv, "rover_tf_pub");
    ros::NodeHandle nh;

    ros::Rate r(100);

    tf::TransformBroadcaster broadcaster;

    while (nh.ok()){
        broadcaster.sendTransform(
            tf::StampedTransform(
                //tf::Transform(tf::Quaternion(0, 0, 0, 1), tf::Vector3(0.5, 0, 0)),
                tf::Transform(tf::Quaternion(0, 0, 0, 1), tf::Vector3(0.5, -0.85, 0.5)),
                ros::Time::now(), "base_rover_1", "base_depth"));
        r.sleep();
    }
}