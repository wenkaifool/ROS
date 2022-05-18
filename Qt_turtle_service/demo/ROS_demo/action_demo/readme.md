action 是一种类似于服务通信的实现，其实现模型也包含请求和响应，但是不同的是，在请求和响应的过程中，服务端还可以连续的反馈当前任务进度，客户端可以接收连续反馈并且还可以取消任务，如下图所描述：  
![image]()  

应用场景  
一般适用于耗时的请求响应场景,用以获取连续的状态反馈。  

功能包依赖  
roscpp rospy std_msgs actionlib actionlib_msgs  

定义action文件  
#目标值  
int32 num  
---  
#最终结果  
int32 result  
---  
#连续反馈  
float64 progress_bar  




