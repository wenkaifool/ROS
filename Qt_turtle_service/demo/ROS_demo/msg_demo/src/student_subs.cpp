// coding:utf-8

#include "ros/ros.h"
#include "msg_demo/Student.h"

void subs_callback(const msg_demo::Student::ConstPtr&people_p)
{
    ROS_INFO("订阅的人信息:%s, %d, %.2f", people_p->name.c_str(), people_p->age, people_p->height);
}

int main(int argc, char *argv[])
{
    /* code */
    setlocale(LC_ALL, "");

    ros::init(argc, argv, "people_subs");

    ros::NodeHandle nh;
    
    ros::Subscriber sub = nh.subscribe<msg_demo::Student>("people_msgs", 1000, subs_callback);

    ros::spin();


    return 0;
}
