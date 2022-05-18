This demo mainly shows how to use header files and source files to encapsulate code in the C++ implementation of ROS.  
The details are as follows:  
(1) Set header files and executable files as source files;  
(2) Set up header files, source files and executable files, respectively.  

Regarding the use of header files in ROS, the core content lies in the configuration of the CMakeLists.txt file. Different packaging methods have different configurations.  
Header file configuration:  
1. Create a new header file in the directory "include": hello.h  
2. Add the include path in the file "c_cpp_properties.json" includepath.  
3. Create a executable file in the src directory: hello.cpp.  
4. Configure the CMakeLists.txt file