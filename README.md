# PARC 2023 Introduction to Robotics Workshop Repository

## Instructions:

### Clone the repository
Place in same workspace as the original PARC Engineers League repository
```
cd ~/catkin_ws/src
git clone https://github.com/PARC-Robotics/intro-to-robotics-workshops.git
```

### Compile

```
cd ~/catkin_ws
catkin_make
```

### Run
In a terminal, run the commands
```
source ~/catkin_ws/devel/setup.bash
roslaunch intro-to-robotics-workshops example1.launch
```

Open another terminal and run the following commands
```
source ~/catkin_ws/devel/setup.bash
roscd intro-to-robotics-workshops
chmod +x scripts/example1_basic.py

rosrun intro-to-robotics-workshops example1_basic.py
```