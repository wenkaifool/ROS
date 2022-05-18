#include "ros/ros.h"


int main(int argc, char *argv[])
{
    ros::init(argc,argv,"turtle_param");

    ros::NodeHandle nh("turtlesim");

    nh.setParam("background_r",0);
    nh.setParam("background_g",0);
    nh.setParam("background_b",0);

    //ros::NodeHandle nh;

    // ros::param::set("/turtlesim/background_r",0);
    // ros::param::set("/turtlesim/background_g",0);
    // ros::param::set("/turtlesim/background_b",0);
    
    return 0;
}