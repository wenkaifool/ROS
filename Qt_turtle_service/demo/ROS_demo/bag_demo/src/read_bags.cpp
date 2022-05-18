#include "ros/ros.h"
#include "rosbag/bag.h"
#include "std_msgs/String.h"
#include "rosbag/view.h"
#include "std_msgs/Int32.h"

int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");
    ros::init(argc,argv,"read_bags");
    ros::NodeHandle nh;
    rosbag::Bag bag;
    bag.open("hello.bag", rosbag::BagMode::Read);

    for (rosbag::MessageInstance const m : rosbag::View(bag))
    {
        std::string topic = m.getTopic();
        ros::Time time = m.getTime();
        std_msgs::StringPtr p = m.instantiate<std_msgs::String>();
        if(p!=nullptr)
        {
            ROS_INFO("读取的数据:%s", p->data.c_str());
        }
    }
    bag.close();
    return 0;
}
