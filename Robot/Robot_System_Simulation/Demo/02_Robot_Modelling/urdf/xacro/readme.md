# URDF优化方案xacro  

概念  
Xacro 是 XML Macros 的缩写，Xacro 是一种 XML 宏语言，是可编程的 XML。  

原理  
Xacro 可以声明变量，可以通过数学运算求解，使用流程控制控制执行顺序，还可以通过类似函数的实现，封装固定的逻辑，将逻辑中需要的可变的数据以参数的方式暴露出去，从而提高代码复用率以及程序的安全性。  

场景  
前面 URDF 文件构建机器人模型的过程中，存在若干问题。  
问题1:在设计关节的位置时，需要按照一定的公式计算，公式是固定的，但是在 URDF 中依赖于人工计算，存在不便，容易计算失误，且当某些参数发生改变时，还需要重新计算。  
问题2:URDF 中的部分内容是高度重复的，驱动轮与支撑轮的设计实现，不同轮子只是部分参数不同，形状、颜色、翻转量都是一致的，在实际应用中，构建复杂的机器人模型时，更是易于出现高度重复的设计，按照一般的编程涉及到重复代码应该考虑封装。  
如果在编程语言中，可以通过变量结合函数直接解决上述问题，在 ROS 中，已经给出了类似编程的优化方案，称之为:Xacro

Xacro_语法详解  
xacro 提供了可编程接口，类似于计算机语言，包括变量声明调用、函数声明与调用等语法实现。在使用 xacro 生成 urdf 时，根标签robot中必须包含命名空间声明:xmlns:xacro="http://wiki.ros.org/xacro"  
(1) 属性与算数运算  
(2) 宏定义---可调用的子函数  
(3) 文件包含  
    机器人由多部件组成，不同部件可能封装为单独的 xacro 文件，最后再将不同的文件集成，组合为完整机器人，可以使用文件包含实现。  
详细请见：http://www.autolabor.com.cn/book/ROSTutorials/di-6-zhang-ji-qi-ren-xi-tong-fang-zhen/64-fang-zhen-urdf-rviz-yu-gazebo-zong-he-ying-yong/652-xacroyu-fa-xiang-jie.html  


执行语句  
rosrun xacro xacro xxx.xacro > xxx.urdf

