---
layout: post
title: "Virtual Pet Bird"
author: "Denise Bischof"
categories: Projects
tags: CC1 WS1920 FinalProject

cover-image: /assets/img/projects/2020-05-20-Virtual_Pet_Bird/VPB_Example.png
cover-image-title: Pet Bird Hungry
---

## Abstract
I tried to create a virtual pet which can be tried out on:
https://cc-final-vb.herokuapp.com/

## Project description
My intention on this project was to create a tiny ecosystem with a small animal that the user can interact with. The animal was supposed react randomly.


## Implementation
I used JavaScript and CSS for the implementation. The behaviour of the bird is determined by a finite state machine. 
The bird either reacts to the users input or changes behaviour randomly, 
according to its current mood. After a certain amount of time, the code checks if the state of the bird can change, 
then a random function determines if it will change. The probability of the bird staying in the same mood is 75%, 
except if they are hungry, then it is 100% and can only be changed by the users input.

## Lessons learned
I learned, that p5 is great, but not for everything. P5 can be amazing for creating visual experiences, but for simple basic functions it can be quite the challenge. I had to drop p5 because it caused a lot of bugs. Gifs are not played natively by p5 and it would mess up my css layers. The audioplayer I added via html also kept breaking down, but since I have disabled p5 there were no issues.

A lot of the animations and visuals were created via CSS which was quite helpful. I tried to create the fog animation via p5 and then with javascript, which were both choppy and very performance heavy. Making the animation with CSS was surprisingly simple and runs very smooth.

A thing I also learned was to keep an eye on responsive design. Since I mainly tested the application on my high resolution gaming pc, I was surprised to find out, that the resolution wouldn't adapt for my lower resolution macbook, even though I added what I supposed were the necessary adjustements.
