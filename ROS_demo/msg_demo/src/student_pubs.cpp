#include "ros/ros.h"
#include "msg_demo/Student.h"

int main(int argc, char *argv[])
{
    /* code */
    setlocale(LC_ALL,"");
    ros::init(argc, argv, "people_pubs");

    ros::NodeHandle nh;

    ros::Publisher pub = nh.advertise<msg_demo::Student>("people_msgs", 1000);

    msg_demo::Student p;
    p.name = "Qiao";
    p.age = 27;
    p.height = 1.71;

    ros::Rate r(1);

    while (ros::ok())
    {
        /* code */
        pub.publish(p);
        p.age += 1;

        ROS_INFO("我叫:%s,今年%d岁,高%.2f米", p.name.c_str(), p.age, p.height);

        r.sleep();

        ros::spinOnce();
    }
    

    return 0;
}
