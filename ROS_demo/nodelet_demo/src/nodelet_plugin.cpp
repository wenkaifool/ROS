# include "nodelet/nodelet.h"
# include "pluginlib/class_list_macros.h"
# include "std_msgs/Float64.h"
# include "ros/ros.h"

namespace nodelet_plugin
{
    class MyPlus: public nodelet::Nodelet
    {
        public:
        MyPlus()
        {
            In_value = 10;
        }

        void onInit()
        {   
            //获取 NodeHandle
            ros::NodeHandle nh = getPrivateNodeHandle();

            //从参数服务器获取参数
            nh.getParam("value", In_value);

            //创建发布与订阅对象
            pub = nh.advertise<std_msgs::Float64>("out", 100);
            // void (*fp)(const boost::shared_ptr<const M> &)
            sub = nh.subscribe<std_msgs::Float64>("in", 100, &MyPlus::doCb, this);
        }

        void doCb(const std_msgs::Float64::ConstPtr &p)
        {
            double num = p->data;
            double result = num + In_value;
            std_msgs::Float64 pubdata;
            pubdata.data=result;
            pub.publish(pubdata);
        }

        private:
        ros::Publisher pub;
        ros::Subscriber sub;
        double In_value;
    };
    
}

PLUGINLIB_EXPORT_CLASS(nodelet_plugin::MyPlus, nodelet::Nodelet)