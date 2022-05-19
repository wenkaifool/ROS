#include "ros/ros.h"
#include "msg_srv_demo/FindTeam.h"


int main(int argc, char *argv[])
{
    setlocale(LC_ALL, "");
    ros::init(argc, argv, "srv_client");
    ros::NodeHandle nh;
    ros::ServiceClient client = nh.serviceClient<msg_srv_demo::FindTeam>("srv_msg");

    client.waitForExistence();
    // ros::service::waitForService("srv_msg");

    msg_srv_demo::FindTeam req;
    req.request.stu.age=27;
    req.request.stu.name="Ciao";
    req.request.stu.height=172;

    bool flag = client.call(req);

    if (flag)
    {
        ROS_INFO("请求正常处理,响应结果:%d", req.response.team.leader.age);
    }
    else
    {
        ROS_ERROR("请求处理失败....");
        return 1;
    }

    return 0;
}
