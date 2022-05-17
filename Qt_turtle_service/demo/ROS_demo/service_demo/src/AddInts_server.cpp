#include "ros/ros.h"
#include "roscpp_tutorials/TwoInts.h"


bool server_callback(roscpp_tutorials::TwoInts::Request &req, roscpp_tutorials::TwoInts::Response &resp)
{
    int num1 = req.a;
    int num2 = req.b;

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
    ros::init(argc, argv, "AddInts_server");
    ros::NodeHandle nh;
    ros::ServiceServer server = nh.advertiseService("TwoInts_sum", server_callback);

    ros::spin();

    return 0;
}