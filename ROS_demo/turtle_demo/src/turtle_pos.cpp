#include "ros/ros.h"
#include "turtlesim/Pose.h"


void subs_callback(const turtlesim::Pose::ConstPtr&p)
{
    ROS_INFO("乌龟位姿信息:x=%.2f,y=%.2f,theta=%.2f,lv=%.2f,av=%.2f", p->x, p->y, p->theta, p->linear_velocity, p->angular_velocity);
}

int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");
    ros::init(argc, argv, "turtle_pos");
    ros::NodeHandle nh;

    ros::Subscriber subs = nh.subscribe<turtlesim::Pose>("/turtle1/pose", 1000, subs_callback);

    ros::spin();
    return 0;
}
