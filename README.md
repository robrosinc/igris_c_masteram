# IGRIS_C_MASTERARM

ROS2 node for MasterArm teleoperation control of the IGRIS-C robot. Controls robot arms through Dynamixel-based master arm devices.

## Overview

This package reads joint positions from MasterArm devices using the MasterArm SDK, and converts them into control commands for both arms (left/right) and fingers of the IGRIS-C robot.

## Requirements

Hardware
- MasterArm device (Dynamixel-based)
- USB-2-Serial adapter (/dev/ttyUSB0)

## Installation
0. submodules
``` bash
git submodule update --init --recursive
```

1. Initialize Submodules

```bash
cd ~/ros2_ws/src/igris_c_masteram
git submodule update --init --recursive
```

2. Install DynamixelSDK

```bash
sudo apt-get install ros-${ROS_DISTRO}-dynamixel-sdk
# Or build from source:
cd ~/ros2_ws/src
git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git
cd ~/ros2_ws
colcon build --packages-select dynamixel_sdk
```

3. Install OpenSSL
``` bash
sudo apt install libssl-dev
```

### 4. Build Package

```bash
cd ~/ros2_ws
colcon build --packages-select igris_c_masterarm
source install/setup.bash
```

## Usage
Basic Execution
```bash
ros2 run igris_c_masterarm igris_c_masterarm_node
```

Launch with parameters
```bash
ros2 launch igris_c_masterarm igris_c_masterarm.launch.py port:="/dev/ttyUSB0" baud:=1000000
```

Pre-execution Checklist

1. Verify MasterArm device is connected to `/dev/ttyUSB0`
2. Verify IGRIS-C robot is running
3. Verify Low-Level control mode is activated

## DDS Topics

> This node does not publish finger commands on standard ROS2 topics. It uses CycloneDDS-style custom DDS topics for IGRIS communication.

Published Topics

- `rt/lowcmd`: Robot motor control commands (`LowCmd`)
- `rt/handcmd`: Hand motor control commands (`HandCmd`)

Subscribed Topics

- `rt/lowstate`: Robot current state (`LowState`)
- `rt/controlmodestate`: Control mode state (`ControlModeState`)

## ROS2 Launch Parameters
| **parameter name** | **default**  | **description**                                   |
|--------------------|--------------|---------------------------------------------------|
| **port**           | /dev/ttyUSB0 | USB-serial port to communicate with the masterarm |
| **baud**           | 1000000      | USB-serial port baudrate                          |

## Control Modes

The node operates only in IGRIS-C's **Low-Level control mode**:

- **High-Level Mode**: Standby state (no commands sent)
- **Low-Level Mode**: Send master arm joint positions to robot


## Trouble Shooting

Serial Port Permissions

```bash
sudo chmod 666 /dev/ttyUSB0
# or add user to dialout group
sudo usermod -aG dialout $USER
```