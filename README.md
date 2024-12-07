# Rover-Master-Logs
The actual codes and PCB designs are maintained [here](https://github.com/Rover-Master).   
Purpose of this repo is to keep weekly logs and design drafts.

## Models
### Monocular Depth Estimation
[Marigold: Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation](https://github.com/prs-eth/Marigold?tab=readme-ov-file#marigold-repurposing-diffusion-based-image-generators-for-monocular-depth-estimation)
### Object Detection
[Ultralytics YOLO 11](https://github.com/ultralytics/ultralytics)    
### KiCAD Library Scrapper   
[easyeda-scrapper](https://github.com/zhangyx1998/easyeda-scraper)    
### PCB Design   
[Rover-Master-PCB](https://github.com/Rover-Master/RoverMaster-PCB)     
### LTspice Simulation
[LTspice Projects](https://github.com/haoyuanxu430/Rover-Master-Logs/tree/main/LTspice) 


## Documentations
[Design Draft](https://docs.google.com/document/d/1-bQ3We8AJNHLamSISemeE2tlZ7m4HuL1uXl8B1t9hPI/edit?usp=sharing), 
[Pre-Alpha Build](https://docs.google.com/document/d/10EeRpl8bRQmmqYDzDo8KQ3iPeUJWZ84ysIDSt7VRHq8/edit?usp=sharing),
[Design Prototype](https://github.com/haoyuanxu430/Rover-Master-Logs/blob/main/Reports/Design_1_Prototype.pdf)


## Videos    
[Pre-Alpha Build](https://youtu.be/6k8LeupdFZE)   

## Milestone Overview

### Work Completed
The following tasks were completed as part of this milestone:

- **Object Detection Implementation**:
  - Developed and integrated an object detection module using YOLOv11.
  - Created a custom ROS node for real-time object detection on the robot.
  - Published detected object data using ROS topics for seamless communication.
 
- **Depth Estimation Testing with Marigold**:
  - Tested the Marigold depth estimation model using pictures of varying quality and resolution.
  - Measured the model's processing time for each image to evaluate efficiency.
  - Observed the model's performance consistency across different image types.

- **Main Control Board Schematic**:
   - Integration of Inertia Measurement Unit.
   - Design of power supply system.
   - Power Delivery circuit.

- **Capacitor Battery Balancer**:
   - Oscillator for MOSFETs driver is fully experimented.
   - Battery balancing circuit is under simulation.


## Known Bugs

### Bug Description
The following bug is a known issue at the end of this milestone:

| **Bug ID** | **Description**                              | **Impact**                                           | **Planned Fix**                      | **Status**   |
|------------|----------------------------------------------|-----------------------------------------------------|--------------------------------------|--------------|
| 001        | Incompatibility between ROS version and Nav 2 | Limits functionality when running specific tasks   | Upgrade ROS version or refactor the code to ensure compatibility | Open         |   
| 002 | Unexpected Behavior of Balancer in LTspice | The battery voltage will drop to close to 0V at first 60ns of simulation | Use a battery model instead of large capacitor | Open |   

## Run Object Detection in ROS2 Workspace

This project requires access to a private remote host. Since the host is private, the steps to SSH into it and run the project are specific to the environment and cannot be replicated externally.

If you have access to the remote host:

1. **SSH into the Host**  
   e.g. `ssh <username>@<remote_host>`
2. **Navigate to ROS2 Workspace**
   `cd /home/robotuser/ros2_ws`
3. **Run the Build Shell**
   `make shell`
4. **Lauch Camera**
   `launch camera`
   the frame with bounding boxes will be saved to `ROS2WS/var`
   
## Run LTspice Simulation
1. The required library LM358 is inside `LTspice` folder.    
2. Put it under the same directory as the LTspice project.   
3. Run the simulation from LTspice.

## KiCAD schematic and Layout   
1. The repositor can be directly clone to local computer with  ```git clone git@github.com:Rover-Master/RoverMaster-PCB.git```   
2. Then the project can be directly opened with KiCAD.