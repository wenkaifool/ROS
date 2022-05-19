There are a couple of demo for using of launching files. Its usages could be summarized as follows:  
1. Load parameters in two ways.  
   (1) <param name="" value="" type="" />   
   (2) <rosparam command="" file="$(find pkg_name)/path to the .yaml file" />  
   (3) Delete parameters: <rosparam command="" param="" />  
   Note that the .yaml file is like---rgb_r: 20, there is a space between ":" and "20".  
2. Run ros nodes.  
   <node pkg="" type="" name="" required="" args="">  
       <!-- change the topic name. Once this is applied in the turtlegame, the keycontrol will become invalid because of changed topic name. -->  
       <remap from="" to="">  
   </node>  
3. Run muilti-files simultaneously  
   <include file="$(find launch_demo)/launch/start_turtlesim.launch" />  
4. Run gourp, where mutil nodes with same pkgs and same nodes and same topics.  
   <launch>  
        <group> 
            <node /> 
        </group>  
   </launch>  
5. Define macro variables  
   <!--也可以在命令窗口手动修改宏值 roslaunch launch_demo args.launch length:=1.0 -->  
   <arg name="" default=""/>  
   <param name="" value="$(find arg arg_name)" />
   