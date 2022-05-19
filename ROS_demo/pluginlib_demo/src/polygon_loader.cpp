#include "pluginlib/class_loader.h"
#include "pluginlib_demo/polygon_base.h"

int main(int argc, char *argv[])
{   
    setlocale(LC_ALL, "");
    // ClassLoader(std::__cxx11::string package, 
                // std::__cxx11::string base_class, 
                // std::__cxx11::string attrib_name, 
                // ros::package::V_string plugin_xml_paths)
    //类加载器 -- 参数1:基类功能包名称 参数2:基类全限定名称
    pluginlib::ClassLoader<polygon_base::RegularPolygon> poly_loader("pluginlib_demo", "polygon_base::RegularPolygon");

    try
    {
        //创建插件类实例 -- 参数:插件类全限定名称
        boost::shared_ptr<polygon_base::RegularPolygon> triangle = poly_loader.createInstance("polygon_plugins::Triangle");
        triangle->initialize(2.0);

        boost::shared_ptr<polygon_base::RegularPolygon> square = poly_loader.createInstance("polygon_plugins::Square");
        square->initialize(10.0);

        ROS_INFO("Triangle area: %.2f, Triangle length: %.2f", triangle->area(), triangle->getlength());
        ROS_INFO("Square area: %.2f, Square length: %.2f", square->area(), square->getlength());
    }
    catch(pluginlib::PluginlibException & ex)
    {
        ROS_ERROR("The plugin failed to load for some reason. Error: %s", ex.what());
    }
    
    return 0;
}
