# Project: Extract frames (RGB and depth) from RealSense bag file

## Description
This repository explores how to extract RGB and depth frames from a bag file. You can extract frames at the recorded frequency (FPS) and a lower frequency (lower FPS).

## Required Libraries
- Cv2
- Pyrealsense2
- Numpy

Use the following command to install the required libraries:

```bash
pip install pyrealsense2 numpy opencv-python
```

## Installation

```bash
git clone https://github.com/ali-rehman-ML/extract_realsense_bag_to_frames.git
cd extract_realsense_bag_to_frames
```

## Method

```python
import extract_realsense as exb
my_bag=exb.Extract_Bag(Bag_path='/path/to/bag_file', fps=,extracting_frame_rate=)
```
#### Use bag_path=r’/path/to/bag_file’ when you have absolute path to convert it into raw string
#### Give fps of recorded bag , for fast and accurate extracting
#### Extracting frame rate should be less or equal to then recorded fps


## Functions
### 1-Extract color_frames:
```python

my_bag.extract_rgb_frames(dir='/path/to/directory/tosave/extracted_frames')
```

#### If dir_path not providence it create a new directory in current directory named color



### 2-Extract depth Frames
```python
my_bag.extract_depth_frames(dir='/path/to/directory/tosave/extracted_frames')
```
#### If dir_path not provided it create a new directory in current directory named depth



### 3-extract both color and corresponding depth frames

```python
color_path='/path/to/directory/to_save_color_frames'
depth_path='/path/to/directory/to_save_depth_frames'
my_bag.extract_rgb_and_depth_frames(dir_color=color_path,dir_depth=depth_path)
```

#### If dir_path not provided it create a new directories in current directory named depth and color 



#### Will be adding more om extracting point cluoud as pcd files and extracting imu data in future.






