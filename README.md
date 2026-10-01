# coorbot description (ROS 2)

URDF/xacro description and Gazebo simulation of a small differential-drive robot with a LiDAR and an IMU (ROS 2 Humble, January 2024).

- `coorbot_body.xacro`: chassis, two drive wheels and a front wheel, using the CAD meshes in `meshes/`
- `gazebo_control.xacro`: Gazebo differential-drive plugin
- `lidar.xacro`, `imu.xacro`: simulated ray sensor and IMU, published as ROS topics
- `launch/display.launch.py`: robot state publisher, Gazebo and RViz with the config in `config/`

The inertia macros in `inertial_macros.xacro` are by Josh Newans (articubot_one).

```bash
colcon build --symlink-install
source install/setup.bash
ros2 launch coorbot_description display.launch.py
```
