---
layout: post
title: "MIDI Mircrocontroller"
author: "Franziska Pätzold"
categories: OP

cover-image: 2019-10-02-midi_micro_controller_banner.png
cover-image-title: midi_micro_controller_banner
---

<h2> Abstract </h2>
Musicians use the effect of novelty and change to yield creative output. It is a reliable way to support the process of composing
reaching its productive plateau. So playing new instruments in uncommon ways, as for instance, the Roli Seaboard does by
making music through Five Dimensions of Touch, can be a creativity trigger. To offer an inexpensive alternative, the MIDI
Microcontroller is a tool that produces sounds without the need to touch any hardware, just by moving a hand in the air around
the device. It can be build by combining an Arduino board, some wires and a couple of ultrasonic sensors.

Project description:
A MIDI Microcontroller prototype can be made by hand by combining ultrasonic sensors with an Arduino board and having the Arduino connected to a PC. The controller is played by an obstacle in front of the ultrasonic sensors adjusted to the range from one up to 50cm. The user can decide if they want to use one hand, both hands or any other own chosen medium to control the MIDI device. Value changes are recognized in two dimensions. The basis to create a sound are five different modes. They interpret the movements in the trigger zone as a single tone, multiple individual tones or linear interpolation between pitches. 

![usecase](https://user-images.githubusercontent.com/22836416/66075508-10049b00-e55c-11e9-9dde-f1b8d1917a24.jpg)


<h2> Implementation </h2>
To generate a sound the data goes through different parts of the system. Starting at the Controller, the ultrasonic sensors are continuously checking for objects in the trigger. Therefore the ultrasonic transmitter generates a pressure wave, that propagates through the air. When it hits an object, the wave gets reflected towards the sensor. A receiver module recognizes it after an amount of time. The period of time is decisive for the calculation of the distance between the sensor and the object. The range (s) is the result of propagation speed (v) multiplied by half of the full measured time (t).
	
The calculated distance will be send to the serial port. A running Processing script reads the data, processes it and defines the pitches. It also transfers this information into MIDI messages. These messages have to be send to a virtual port. The port is needed because the controller is in case of the data processing process not directly communicating with the DAW. Through the virtual port, DAWs are able to receive the MIDI messages. 
	
After choosing a Synthesizer in the DAW, that interprets the MIDI messages, connected speakers will create a sound event, that listeners perceive as audio.

<h2> Lessons learned </h2>
- testing different sensors with Arduino
- MIDI
- sending MIDI trough a virtual port