# 🎯 Real-Time Object Tracking using OpenCV

A real-time Computer Vision application that allows users to select and track an object from a live webcam feed using OpenCV's **CSRT Tracker**. The application continuously follows the selected object, displays a bounding box around it, and monitors the tracking performance with a live FPS counter.

---

## 📌 Features

* 📹 Real-time webcam video capture
* 🎯 Manual object selection using Region of Interest (ROI)
* 📦 Accurate object tracking with the CSRT tracking algorithm
* 🟢 Live bounding box around the tracked object
* ⚡ Real-time FPS (Frames Per Second) display
* ❌ Object loss detection with status indication
* 🖥️ Lightweight and easy to run

---

## 📸 Demo

> **Sample Output**

```
+----------------------------------------+

        Webcam Feed

        ┌──────────────┐
        │    Bottle    │
        └──────────────┘

Status : Tracking

FPS : 32

Press 'Q' to Exit

+----------------------------------------+
```

---

## 🛠️ Tech Stack

* Python 3.x
* OpenCV (opencv-contrib-python)
* NumPy

---
## ▶️ Usage

Run the application:

```bash
python tracker.py
```

### Steps

1. Your webcam will open.
2. Select the object you want to track by dragging a rectangle around it.
3. Press **Enter** or **Space** to confirm the selection.
4. The application will begin tracking the selected object in real time.
5. Press **Q** to exit the application.

---

## 📖 How It Works

1. Capture live video from the webcam.
2. Allow the user to select an object using ROI (Region of Interest).
3. Initialize the **CSRT Object Tracker**.
4. Update the object's position for every incoming frame.
5. Draw a bounding box around the tracked object.
6. Display the tracking status and FPS.
7. Continue until the user exits the program.

---

## 📊 Tracking Algorithm

This project uses **CSRT (Discriminative Correlation Filter with Channel and Spatial Reliability)**.

### Why CSRT?

* High tracking accuracy
* Better handling of scale changes
* Robust against partial occlusion
* Reliable for real-time applications

---

## 📈 Future Improvements

* Multiple object tracking
* YOLOv8 object detection integration
* DeepSORT for persistent object IDs
* Object counting
* Motion trail visualization
* Speed estimation
* Video recording
* GPU acceleration (CUDA)
* Streamlit web interface
* Flask API deployment

---

## 🎯 Learning Outcomes

This project demonstrates knowledge of:

* Computer Vision
* OpenCV
* Image Processing
* Real-time Video Processing
* Object Tracking Algorithms
* ROI Selection
* Performance Monitoring (FPS)

---

## 📦 Requirements

```
opencv-contrib-python
numpy
```

---

## 🤝 Contributing

Contributions are welcome!

If you have ideas for improvements, feel free to:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Open a Pull Request.

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

---

## 👨‍💻 Author

**Prince Agarwal**

AI/ML Developer | Computer Vision Enthusiast

> *Building intelligent systems with Machine Learning, Deep Learning, and Computer Vision.*
