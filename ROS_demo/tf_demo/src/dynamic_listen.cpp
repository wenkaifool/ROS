#include "ros/ros.h"
#include "tf2_ros/buffer.h"
#include "tf2_ros/transform_listener.h"
#include "geometry_msgs/PointStamped.h"
#include "tf2_geometry_msgs/tf2_geometry_msgs.h"

int main(int argc, char *argv[])
{
    setlocale(LC_ALL, "");
    ros::init(argc, argv, "dynamic_tf_sub");
    ros::NodeHandle nh;
    

    tf2_ros::Buffer buffer;
    tf2_ros::TransformListener listener(buffer);

    ros::Rate r(1);

    while (ros::ok())
    {
        geometry_msgs::PointStamped absolute_points;
        absolute_points.header.frame_id = "turtle1";
        absolute_points.header.stamp = ros::Time();
        absolute_points.point.x = 1;
        absolute_points.point.y = 1;
        absolute_points.point.z = 0;

        try
        {
            geometry_msgs::PointStamped point_base;
            point_base = buffer.transform(absolute_points, "world");

            ROS_INFO("转换后的数据:(%.2f,%.2f,%.2f),参考的坐标系是:%s",
                        point_base.point.x,
                        point_base.point.y,
                        point_base.point.z,
                        point_base.header.frame_id.c_str());
        }
        catch(const std::exception& e)
        {
            // std::cerr << e.what() << '\n';
            ROS_INFO("程序异常.....");
        }
        r.sleep();
        ros::spinOnce();
        
    }
    


    return 0;
}