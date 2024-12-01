
# **Scientific Experimentation and Evaluation (SEE)**

This repository contains experiments and evaluations in robotics, focusing on motion observation and data analysis.
We cover practical experimentation and (statistical) data evaluation and data
 visualisation. This manual deals with practical experimentation, measurement and data analysis,
 using the experimental analysis of the characteristics of a differential drive as a running example.
---

## **Table of Contents**
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Authors](#authors)

---

## **Overview**

- Robotics experimentations.
- Tracking and evaluating robotic motion behavior.
- Visualizing real-world outcomes.

---

## **Features**
- **Data Analysis**: Scripts to process, reshape, and visualize sensor data.
- **CSV Outputs**: Save processed data for tracking paths and motor positions.

---

## **Installation**

### **Prerequisites**
- Python 3.8+
- Libraries: `numpy`, `pandas`, `scipy`, `matplotlib`, `ev3dev2`.
- Clone the repository:
   ```bash
   git clone https://github.com/username/SEE_Experiments.git
   ```


---

## **Usage**

- Jupyter Notebook**
Explore the experimental notebook for detailed steps:
```bash
jupyter notebook SEE_Experiments.ipynb
```

---

## **Project Structure**
```plaintext
SEE/
├── manual_motion/               # Manual motion experiments data "Experiment 1"
│   ├── images/                  # Images captured during manual motion
│   ├── manual_data_with_centroid.txt          # Centroid-based data file
│   ├── Manual_data_with_centroid_TeamA.txt    # Team A's manual motion data
│   ├── Manual_data_with_centroid_TeamC.txt    # Team C's manual motion data
│   └── robot_path.csv           # Robot trajectory data
│
├── camera_calibration/          # Camera calibration data "Experiment 2"
│   ├── images/                  # Calibration images
│   ├── test_images/             # Test images for validation
│   └── calibration_setup.webp   # Setup image for calibration
│
│
├── YouBot/                      # Data related to YouBot experiments
│   ├── end_effector_data/       # End-effector position data
│   │   ├── rosbag_data/         # Raw ROS bag data
│   │   ├── endpose_large.csv    # End pose data for large configurations
│   │   ├── endpose_medium.csv   # End pose data for medium configurations
│   │   ├── endpose_small.csv    # End pose data for small configurations
│   │   ├── startpose_large.csv  # Start pose data for large configurations
│   │   ├── startpose_medium.csv # Start pose data for medium configurations
│   │   └── startpose_small.csv  # Start pose data for small configurations
│   │
│   ├── images/
│   │           
│   ├── opti_track_data/         # OptiTrack motion capture data
│   │   ├── opti_track_path/     # Processed tracking paths
│   │   │   ├── LL/              # Large-left configurations
│   │   │   ├── LR/              # Large-right configurations
│   │   │   ├── LS/              # Large-straight configurations
│   │   │   ├── ML/              # Medium-left configurations
│   │   │   ├── MR/              # Medium-right configurations
│   │   │   ├── MS/              # Medium-straight configurations
│   │   │   ├── SL/              # Small-left configurations
│   │   │   ├── SR/              # Small-right configurations
│   │   │   └── SS/              # Small-straight configurations
│   │   ├── opti_track_raw_data/ # Raw data from OptiTrack
│   └── start_end_pose_xz/       # Start and end poses in XZ plane
│
├── SEE_Experiments.ipynb    # Main experimental notebook
└── README.md                    # Project documentation

```

---

## **Authors**
- **Amol Tatkari**
- **Behrouz Ghamkhar**
- **Ujjwal Patil**

--- 
