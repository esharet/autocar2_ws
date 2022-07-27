# Roadmap 

## camera-map fusion 
fusing map data and camera data together. 

### GOAL:
1. selecting a point in the camera feed and navigating to it using using the navigation stack
2. selecting a point on the map and navigating to it using using a visual tracker

### MID-GOALS:
1. selecting a point in the camera feed and viewing it on the map 
2. selecting a point in the map and viewing it on the camera feed 

### STEPS: 
- [x] odom -> base_footprint 
- [x] enable localization in dorothy robot 
- [x] selecting a point in the camera feed 
- [x] placing a point in the map 
- [] placing a point in the camera feed 
- [] recieving published point in the map 

## slam revive 
revive a "broken" slam and loading the robot into a not finished slam.
### GOAL: 
1. reload slam from a known position in a reliable way 
2. reload the last good slam from an unknown position and fix the position using the camera-map fusion
### MID-GOALS:
1. reload slam from a known position in a reliable way 
2. save the slam data periodically with it's relevant positions, keep a refernce to the last one.
3. load at request the robot from the last good state 
4. allow calibration matching of points from images to 
5. display all video streams/easy stream changing 