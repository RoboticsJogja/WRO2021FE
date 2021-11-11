**KUMBANG JOGJA**

**WRO 2021 FUTURE ENGINEERS**

Development Team
====

<img src="https://user-images.githubusercontent.com/94065614/141332640-ddf60e52-fb49-4c67-a330-1615acbad0d0.jpg" width="300">

* Team Name : KUMBANG JOGJA
* Country   : Indonesia

* Member 1  : Reynard Ardian Simanjuntak
* Member 2  : Adamsyah Haryo Saksono
* Coach     : Bambang Dwi Jayanto

Youtube Video URL
====
<img src="https://user-images.githubusercontent.com/94065614/141338427-e405ab0e-7892-4427-8235-a43acce31be9.jpg" width="300">

https://youtu.be/kMnmidmwntc

Engineering materials
====

This repository contains engineering materials of a self-driven vehicle's model participating in the WRO Future Engineers competition in the season 2021, constructed by KUMBANG JOGJA Team representing Indonesia.

## Content

* `team` contains photo of our team
* `photos` contains 6 photos of the vehicle, from 6 different angles
* `video` contains Youtube link of our vehicle running
* `schemes` contains 2 schematic diagrams of the electromechanical components used in our vehicle and how they connect to each other
* `src` contains the code we made so that the vehicle be self-driven
* `models` contains Lego 3D model of our vehicle

## Introduction

### The Code
The programming language used for the vehicle is Python. The code for the self-driven vehicle itself consists of 4 different modules:
1. `ultrasonic module` which controls the two ultrasonic sensors that are attached to the vehicle, one on the right side of the vehicle's front, and the other on the left. The ultrasonic sensors are used to detect walls and/or objects around the vehicle, both facing slightly outwards as to give the vehicle more space and time to anticipate condition of the field in front of it. This module inside the code holds every command regarding object detection, which in turn will contribute greatly to the movement behaviour of the vehicle.
2. `colour sensor module` which controls the RGB colour sensor located on the back-side of the vehicle. The colour sensor is used to detect the orange and/or blue lines on each corners of the arena, and which helps the vehicle to keep track of its position relative to its starting point, and allows it to stop at where it started after doing 3 rotations around the arena.
3. `motoric module` which controls the movement of the vehicle, including speed, angle of turn, and direction. The vehicle uses one DC motor, connecting to a motor driver module which controls its velocity, and one servo motor which control its angle of turn. The speed and direction of the DC motor is held constant throughout the program, while the servo motor directly depends on the ultrasonic sensors.
4. `computer vision module` which controls the camera located in front of the vehicle. The camera is used to detect red and green objects on the field, and thus allowing the vehicle to avoid them accordingly.

Other than the 4 modules mentioned above, there are other functionalities contained in the main program, including the control for the push button used to start the program, and the indicator LEDs located on the vehicle. The main program also holds the math and logic for the wall-following mechanism of the vehicle and its colour detecting functionality.

### Electromechanical Components
The self-driven vehicle uses 10 different components, with the details and connections to each parts attached to the aforementioned folders:
#### 1. Raspberry Pi 
<img src="https://user-images.githubusercontent.com/94065614/141334096-2b5bf921-4fe2-4bb0-a2e9-0b20a46d2752.jpg" width="300">
Raspberry Pi is a series of small single-board computers (SBCs) developed in the United Kingdom, able to be connected to a number of different outputs and inputs such as visual ouput to a computer screen or an input from a keyboard. Other than that, it has multiple General-Purpose Input/Output (GPIO) pins able to be connected to modules such as sensors and motors, receiving input and/our output, computing information, and giving commands by using Python or Scratch as its programming language.  It uses a  Broadcom BCM2837 SoC with a 1.2 GHz 64-bit quad-core ARM Cortex-A53 processor, with 512 KB shared L2 cache. In this vehicle, the version of Raspberry Pi used is version 3B+.

#### 2. DC Motor and L298N Motor Driver Module
<img src="https://user-images.githubusercontent.com/94065614/141335739-daf0bada-47e5-43c9-b86d-f3176c9b8b5f.jpg" width="300">
The L298N is a dual-channel H-Bridge motor driver capable of driving a pair of DC motors. That means it can individually drive up to two motors making it ideal for building two-wheel robot platforms. Other than its minimal design, it also provides an onboard 5V regulator that can be used to power 5V circuits very conveniently. The driving motor used to move the vehicle uses a differential, gearing-down mechanism in order to aid it during turns and increases its torsion.

#### 3. MG90S Servo Motor 
<img src="https://user-images.githubusercontent.com/94065614/141336083-a77e4f03-306c-475d-a0b8-13fcf00e07fe.jpg" width="300">
The MG90S is a lightweight micro servo motor with metal gear and comes with high output power. This servo motor serves as a steering mechanism as it controls the vehicle's front wheel's angle. The servo motor is attached to an ackerman steering geometrical mechanism which will aid the vehicle in turning.

#### 4. HC-SR04 Ultrasonic Sensors
<img src="https://user-images.githubusercontent.com/94065614/141336295-342c3063-1fbc-446c-a660-c61c362168b5.jpg" width="300">
At its core, the HC-SR04 Ultrasonic distance sensor consists of two ultrasonic transducers. The one acts as a transmitter which converts electrical signal into 40 KHz ultrasonic sound pulses. The receiver listens for the transmitted pulses. If it receives them it produces an output pulse whose width can be used to determine the distance the pulse travelled. The sensor is small, easy to use, and offers excellent non-contact range detection between 2 cm to 400 cm with an accuracy of 3mm. Since it operates on 5 volts, it can be hooked directly to any 5V logic microcontrollers.

#### 5. Raspberry Pi Camera Module
<img src="https://user-images.githubusercontent.com/94065614/141336705-78110bc8-f7f3-4480-9ac8-163c9bafd201.jpg" width="300">
The Raspberry Pi Camera v2 is a high quality 8 megapixel Sony IMX219 image sensor custom designed add-on board for Raspberry Pi, featuring a fixed focus lens. It's capable of 3280 x 2464 pixel static images, and also supports 1080p30, 720p60 and 640x480p60/90 video. It attaches to Pi by way of one of the small sockets on the board upper surface and uses the dedicated CSi interface, designed especially for interfacing to cameras. The board itself is tiny, at around 25mm x 23mm x 9mm. It also weighs just over 3g, making it perfect for mobile or other applications where size and weight are important. It connects to Raspberry Pi by way of a short ribbon cable. The high quality Sony IMX219 image sensor itself has a native resolution of 8 megapixel, and has a fixed focus lens on-board. In terms of still images, the camera is capable of 3280 x 2464 pixel static images, and also supports 1080p30, 720p60 and 640x480p90 video. 

#### 6. TCS3200 Colour Sensor 
<img src="https://user-images.githubusercontent.com/94065614/141336898-9d8a3ee0-30bb-44dc-8766-7492c8a4a3ec.jpg" width="300">
TCS3200 is a sensor that uses a TAOS TCS3200 RGB sensor chip to detect color. It also contains four white LEDs that light up the object in front of it. The TCS3200 has an array of photodiodes with 4 different filters, 16 photodiodes with filters sensitive to each of the three colours, Red, Green, Blue, and 16 photodiodes without a filter.  By selectively choosing the photodiode filter’s readings, you’re able to detect the intensity of the different colors. The sensor has a current-to-frequency converter that converts the photodiodes’ readings into a square wave with a frequency that is proportional to the light intensity of the chosen color. This frequency is then, read by the Raspberry Pi.


#### 7. Push Button 
a simple push button is used to start the vehicle.

#### 8. Indicator LED 
a single LED is used to indicate whether the program is running or not.

#### 9. 8, 1.5 V Rechargable Batteries 
this vehicle needs 12 volts of electrical power to run, hence 8, 1.5 V Rechargable batteries are used.

#### 10. DC Stepdown with Voltmeter 
is used to control the power input from the batteries, and as a voltmeter to indicate the remaining voltage available from the batteries.


### Code Compiling Process

As a Raspberry Pi, an SBC, is used as a controller, the coding, building, and compiling of the program is done directly within the vehicle, and is set to automatically run on boot.


