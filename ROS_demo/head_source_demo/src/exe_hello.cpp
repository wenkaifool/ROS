# include "ros/ros.h"
# include "head_source_demo/head_hello.h"

namespace hello_ns
{
    void HelloPub::run()
    {
        ROS_INFO("自定义头文件的使用....");
    }
}


int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");
    ros::init(argc,argv,"header_file");
    hello_ns::HelloPub hello_head;
    hello_head.run();
    return 0;
}