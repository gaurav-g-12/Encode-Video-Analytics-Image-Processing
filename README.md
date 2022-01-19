# Encode-Video-Analytics-Image-Processing

the depthmap model is avaliable at : 
https://github.com/isl-org/MiDaS/releases/download/v2_1/model-f6b98070.onnx


 

Anti-pinch Technology using Computer Vision 
19-12-2021

Av Team 18
KLE Technological University,
Hubli
Team Members:
Gaurav Talebailkar
Sheetal Puranikmath
Divyajyoti C Morabad
Sushmita Shivashimpi
Overview
In this modern era everything around us is getting automated drastically, and with this arises the safety concerns.  Nowadays cars come with  power windows that use an electric motor to operate. So we need a technology that detects and  prevents the accidental winding up of the power window. If the system senses any obstacle in the path of the glass, it should prevent the window glass from moving further up. Thus, it prevents possible injuries to the occupants.
Goals
To develop a Model to detect the obstacle (hand/finger) in the closing movement path of window/sunroof using image processing.
To develop a Model that is both time and space efficient.
Methodology 
Initially we thought of mounting a camera near the window of the car and then use an object detection algorithm to detect any obstacle in between the window. 
                                                         
But the limitation with this approach is that as windows are transparent we  won't be able to tell if the object is outside the window (in this case the window must continue to roll up) or is the object in between(in this case the object is an obstacle so the window must roll down). So this approach might lead to false detection. 
So we came up with an idea in which a continuous line of tape of any color  (hereon we will refer to it as a red tape) will be applied on the edge of the glass, and with the help of the camera we will detect if the line is continuous or not.
If the line is continuous then there is no obstacle in between the windows.
                                          


But when an obstacle is in between the window, the continuity of the line will be disturbed and the camera will capture a discontinuous line.  


Thus we will be able to detect the obstacle. 
Instead of using a red tape/radium along the edge of the window we can use Infrared Strips that are not visible to human eyes whereas can be detected by a camera thus keeping the aesthetics of the car.
But even this approach has some limitations i.e any random movement inside the car (eg  - the passenger waving his hand) that obstructs the camera will lead to false detection. 
Both these approaches combined would make a great algorithm but still we were missing out on something. Ohh yeah, the distance of the object from the window. But we are not supposed to use any sensors to measure the distance. So we can use a depth map.
We will fix the distance between the window and camera predefined and all the calculations will be with respect to this distance.
If an object detected has a distance less than the fixed distance between the window and camera then that object has crossed the glass of the window and is an obstacle or else not.
                          
                                           
All these algorithms implemented individually have some limitations but when combined they address the limitations of each other and work very accurately.
And finally we came up with an algorithm that would answer all the limitations.
Final Solution
In this approach we use the potential of a simple camera to the fullest, i.e by combining object detection algorithm with the line continuity algorithm as we would like to call it and also a depth map algorithm to calculate the depth of the object from the window. 
Algorithm 
Initially take an image frame from the live video camera installed near the window.
Use Object detection algorithm to detect for any obstacle like hand, finger etc
If obstacle detected then check if the red tape on the edge of the glass is continuous 
If continuous then that means the object detected is outside the window 
But if the red line is not continuous then use depth map to calculate the depth of the object
If the depth of the object is less than the fixed distance of the window from the camera that means the object detected is an obstacle and the windows will roll down.

Time Complexity of the Algorithm 
As this is a safety system, time plays a crucial role. Such a system must be able to respond within a fraction of seconds. 
As we are using 3 Algorithms here, if we nest them it will increase the time dramatically. But to avoid this we can use multithreading i.e running each algorithm on different cores of a CPU.
In this case the current task will have no dependency on the output from the previous algorithm. 
Block diagram 

Conclusion
Thus by implementing this we would be able to achieve our goals and also replace the cost of all the sensors with a camera thus reducing the cost.

