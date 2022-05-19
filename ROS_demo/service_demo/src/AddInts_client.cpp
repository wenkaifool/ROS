#include "ros/ros.h"
#include "roscpp_tutorials/TwoInts.h"

int main(int argc, char *argv[])
{
    /* code */
    setlocale(LC_ALL, "");

    // 调用时动态传值,如果通过 launch 的 args 传参，需要传递的参数个数 +3
    if (argc != 3)
    // if (argc != 5)//launch 传参(0-文件路径 1传入的参数 2传入的参数 3节点名称 4日志路径)
    {
        ROS_ERROR("请提交两个整数");
        return 1;
    }

    // 2.初始化 ROS 节点
    ros::init(argc,argv,"add_client");
    // 3.创建 ROS 句柄
    ros::NodeHandle nh;
    // 4.创建 客户端 对象
    ros::ServiceClient client = nh.serviceClient<roscpp_tutorials::TwoInts>("TwoInts_sum");
    //等待服务启动成功
    //方式1
    ros::service::waitForService("TwoInts_sum");
    //方式2
    // client.waitForExistence();
    // 5.组织请求数据
    roscpp_tutorials::TwoInts ai;
    ai.request.a = atoi(argv[1]);
    ai.request.b = atoi(argv[2]);
    // 6.发送请求,返回 bool 值，标记是否成功
    bool flag = client.call(ai);

    if (flag)
    {
        ROS_INFO("请求正常处理,响应结果:%d",ai.response.sum);
    }
    else
    {
        ROS_ERROR("请求处理失败....");
        return 1;
    }

    return 0;
}