import xacro
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import SetEnvironmentVariable

def generate_launch_description():
    pkg_share = get_package_share_directory('coorbot_description')
    xacro_path = os.path.join(pkg_share, 'urdf', 'coorbot.urdf.xacro')
    urdf_doc = xacro.process_file(xacro_path)
    robot_description = urdf_doc.toxml()

    rviz = Node (
                    package='rviz2',
                    executable='rviz2',
                    output='screen',
                    parameters=[{'use_sim_time': True }],
                    # arguments=['-d', os.path.join(get_package_share_directory('coorbot_description'), 'urdf', 'Robot.urdf')]
                )
    
    
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')])
            )
    spawner = Node(
                package='gazebo_ros', executable='spawn_entity.py',
                arguments=['-topic', 'robot_description', '-entity', 'coorbot'],
                output='screen'
            )
        
    rsp =   Node(
                name='robot_state_publisher',
                package='robot_state_publisher',
                executable='robot_state_publisher',
                output='screen',
                parameters=[
                    {'use_sim_time': True},
                    {'robot_description': robot_description}
                ]
            )
    
    jsp =   Node(
            name='joint_state_publisher_gui',
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            output='screen',
            parameters=[
                {'use_sim_time': True},
                {'robot_description': robot_description}
            ]
        )
        
        
    
    ld = LaunchDescription()
    ld.add_action(rviz)
    ld.add_action(gazebo)
    ld.add_action(spawner)
    ld.add_action(jsp)
    ld.add_action(rsp)
    


    return ld
