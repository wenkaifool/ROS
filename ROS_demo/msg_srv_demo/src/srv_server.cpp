#include "ros/ros.h"
#include "msg_demo/Team.h"
#include "msg_demo/Student.h"
#include "msg_srv_demo/FindTeam.h"


bool server_callback(msg_srv_demo::FindTeam::Request &req, msg_srv_demo::FindTeam::Response &reps)
{
    reps.team.name = "ByeBye";
    reps.team.leader.age=req.stu.age;
    reps.team.leader.name=req.stu.name;
    reps.team.leader.height=req.stu.height;

    ROS_INFO("服务器接收到请求数据");

    return true;
}


int main(int argc, char *argv[])
{
    setlocale(LC_ALL, "");
    ros::init(argc, argv, "srv_server");
    ros::NodeHandle nh;

    ros::ServiceServer server = nh.advertiseService("srv_msg",server_callback);
    ROS_INFO("The show begins......");
    ros::spin();
    return 0;
}