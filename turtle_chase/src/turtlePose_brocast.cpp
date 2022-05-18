#include "ros/ros.h"
#include "turtlesim/Pose.h"
#include "tf2_ros/transform_broadcaster.h"
#include "geometry_msgs/TransformStamped.h"
#include "tf/LinearMath/Quaternion.h"

std::string turtle_name;

void doMsg(const turtlesim::Pose::ConstPtr & pose)
{
    static tf2_ros::TransformBroadcaster broadcaster;
    geometry_msgs::TransformStamped tfs;

    tfs.header.frame_id = "world";
    tfs.header.stamp = ros::Time::now();
    tfs.child_frame_id = turtle_name;
    tfs.transform.translation.x = pose->x;
    tfs.transform.translation.y = pose->y;
    tfs.transform.translation.z = 0.0;

    tf::Quaternion qtn;
    qtn.setRPY(0,0, pose->theta);
    tfs.transform.rotation.x = qtn.getX();
    tfs.transform.rotation.y = qtn.getY();
    tfs.transform.rotation.z = qtn.getZ();
    tfs.transform.rotation.w = qtn.getW();

    broadcaster.sendTransform(tfs);    

}

int main(int argc, char *argv[])
{
    setlocale(LC_ALL, "");
    ros::init(argc, argv, "turtlePose_brocast");
    ros::NodeHandle nh;

    if (argc!=2)
    {
        ROS_ERROR("请传入正确的参数");
    }
    else
    {
        turtle_name = argv[1];
        ROS_INFO("乌龟 %s 坐标发送启动",turtle_name.c_str());
    }

    ros::Subscriber sub = nh.subscribe<turtlesim::Pose>(turtle_name + "/pose",1000, doMsg);

    ros::spin();

    return 0;
}
