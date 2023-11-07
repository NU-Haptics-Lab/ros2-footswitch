cmake_minimum_required(VERSION 3.8)
project(footswitch)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

include_directories(/src)

FILE(GLOB src_files 
      ./src/*.cpp
      ./src/*.hpp
      ./src/*.h
    )


#set(NAME test_api)
#add_executable(${NAME} src/test.cpp)
#target_link_libraries(${NAME} -lhidapi-libusb)
#install(TARGETS
#  ${NAME}
#  DESTINATION lib/${PROJECT_NAME}
#)

# Install Python modules
ament_python_install_package(${PROJECT_NAME})

# Install Python executables
install(PROGRAMS scripts/footswitch.py DESTINATION lib/${PROJECT_NAME}
)


ament_package()