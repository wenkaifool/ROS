#include "ros/ros.h"
#include "actionlib/client/simple_action_client.h"
#include "action_demo/AddIntsAction.h"

typedef actionlib::SimpleActionClient<action_demo::AddIntsAction> Client;

void done_cb(const actionlib::SimpleClientGoalState &state, const action_demo::AddIntsResultConstPtr &result)
{
    if (state.state_ == state.SUCCEEDED)
    {
        ROS_INFO("最终结果:%d",result->result);
    } else {
        ROS_INFO("任务失败！");
    }
}

void active_cb()
{
    ROS_INFO("服务已经被激活....");
}

void feedback_cb(const action_demo::AddIntsFeedbackConstPtr &feedback)
{
    ROS_INFO("当前进度:%.2f",feedback->progress_bar);
}

int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");
    // 2.初始化ROS节点;
    ros::init(argc,argv,"AddInts_client");
    // 3.创建NodeHandle;
    ros::NodeHandle nh;
    // 4.创建action客户端对象;
    // SimpleActionClient(ros::NodeHandle & n, const std::string & name, bool spin_thread = true)
    // actionlib::SimpleActionClient<demo01_action::AddIntsAction> client(nh,"addInts");
    Client client(nh, "addInts", true);
    client.waitForServer();

    // 5.发送目标，处理反馈以及最终结果;
    /*  
        void sendGoal(const demo01_action::AddIntsGoal &goal, 
            boost::function<void (const actionlib::SimpleClientGoalState &state, const demo01_action::AddIntsResultConstPtr &result)> done_cb, 
            boost::function<void ()> active_cb, 
            boost::function<void (const demo01_action::AddIntsFeedbackConstPtr &feedback)> feedback_cb)

    */
    action_demo::AddIntsGoal goal;
    goal.num = 10;

    client.sendGoal(goal,&done_cb,&active_cb,&feedback_cb);

    ros::spin();
    return 0;
}
