**KUMBANG JOGJA**

**WRO 2021 FUTURE ENGINEERS**

Engineering materials
====

This repository contains engineering materials of a self-driven vehicle's model participating in the WRO Future Engineers competition in the season 2021, constructed by KUMBANG JOGJA Team representing Indonesia.

## Content

* `team` contains photo of our team
* `photos` contains 6 photos of the vehicle, from 6 different angles
* `video` contains Youtube link of our vehicle running
* `schemes` contains 2 schematic diagrams of the electromechanical components used in our vehicle and how they connect to each other
* `src` contains the code we made so that the vehicle be self-driven

## Introduction

### The Code
The code for the self-driven vehicle consists of 5 different modules:
1. `ultrasonic module` which controls the two ultrasonic sensors that are attached to the vehicle, one on the right side of the vehicle's front, and the other on the left. The ultrasonic sensors are used to detect walls and/or objects around the vehicle, both facing slightly outwards as to give the vehicle more space and time to anticipate condition of the field in front of it. This module inside the code holds every command regarding object detection, which in turn will contribute greatly to the movement behaviour of the vehicle.
3. `colour sensor module` which controls the RGB colour sensor located on the back-side of the vehicle. The colour sensor is used to detect the orange and/or blue lines on each corners of the arena, and which helps the vehicle to keep track of its position relative to its starting point, and allows it to stop at where it started after doing 3 rotations around the arena.
4. `motoric module` which controls the movement of the vehicle, including speed, angle of turn, and direction. The vehicle uses one DC motor, connecting to a motor driver module which controls its velocity, and one servo motor which control its angle of turn. The speed and direction of the DC motor is held constant throughout the program, while the servo motor directly depends on the ultrasonic sensors.
5. `camera module` which controls the camera located in front of the vehicle. The camera is used to detect red and green objects on the field, and thus allowing the vehicle to avoid them accordingly.

Other than the 5 modules mentioned above, there are other functionalities contained in the main program, including the control for the push button used to start the program, and the indicator LEDs located on the vehicle. The main program also holds the math and logic for the wall-following mechanism of the vehicle and its colour detecting functionality.

### Electromechanical Components
The self-driven vehicle uses 6 different components:
1. `Raspberry PI` is a series of small single-board computers (SBCs) developed in the United Kingdom, able to be connected to a number of different outputs and inputs such as visual ouput to a computer screen or an input from a keyboard. Other than that, it has multiple General-Purpose Input/Output (GPIO) pins able to be connected to modules such as sensors and motors, receiving input and/our output, computing information, and giving commands by using Python or Scratch as its programming language.  It uses a  Broadcom BCM2837 SoC with a 1.2 GHz 64-bit quad-core ARM Cortex-A53 processor, with 512 KB shared L2 cache. 
3. `DC Motor and L298N Motor Driver Module` The L298N is a dual-channel H-Bridge motor driver capable of driving a pair of DC motors. That means it can individually drive up to two motors making it ideal for building two-wheel robot platforms. It is a commonly used component for prototypes and hobbyist projects, as it is easy to use and interface the L298 with a Raspberry Pi or an Arduino. Other than its minimal design, it also provides an onboard 5V regulator that you can use to power your 5V circuits very conveniently
5. `MG90S Servo Motor`
6. `HC-SR04 Ultrasonic Sensors`
7. `TCS Colour Sensor`
8. `Push Button`
9. `Indicator LED`
10. `Voltage Regulator`
11. `8 1,3 Volt Rechargable Batteries`

### Code Compiling Process


_This part must be filled by participants with the technical clarifications about the code: which modules the code consists of, how they are related to the electromechanical components of the vehicle, and what is the process to build/compile/upload the code to the vehicle’s controllers._



