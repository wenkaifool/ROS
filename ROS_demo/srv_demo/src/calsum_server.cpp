#include "ros/ros.h"
#include "srv_demo/AddInts.h"


bool server_callback(srv_demo::AddInts::Request& req, srv_demo::AddInts::Response&resp)
{
    int num1 = req.num1;
    int num2 = req.num2;

    ROS_INFO("服务器接收到的请求数据为:num1 = %d, num2 = %d",num1, num2);

    if (num1 < 0 || num2 < 0)
    {
        ROS_ERROR("提交的数据异常:数据不可以为负数");
        return false;
    }

    resp.sum = num1 + num2;
    return true;
}

int main(int argc, char *argv[])
{
    setlocale(LC_ALL, "");
    ros::init(argc,argv, "add_server");
    ros::NodeHandle nh;

    ros::ServiceServer server = nh.advertiseService("AddInts", server_callback);
    ROS_INFO("The show begins......");
    ros::spin();
    return 0;
}
