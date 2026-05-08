# FormGuard AI — Gym Form Analysis

### **The Project**
FormGuard AI is a real-time computer vision pipeline I built to help with proper lifting form. Instead of just counting reps, it uses 3D pose estimation to catch "momentum cheating," making sure the user is actually isolating muscles for hypertrophy.

### **Technical Philosophy**
I built this using a minimal architecture to keep it efficient:
*   **Modular Design:** The geometry engine is decoupled from the CV pipeline for easy testing and scaling.
*   **Vectorized Math:** Used NumPy for 3D vector operations to maintain 30 FPS on my local system.
*   **Scale Invariance:** Used normalized coordinates so it works regardless of body type or camera distance.

### **The Math**
To detect shoulder "swing" during curls, I used the dot product of the **Shoulder (A)**, **Elbow (B)**, and **Hip (C)** vectors to find the joint angle:

$$ \theta = \arccos\left(\frac{\vec{BA} \cdot \vec{BC}}{\|\vec{BA}\| \|\vec{BC}\|}\right) $$

If the swing angle exceeds 15°, the system flags it as momentum cheating.

### **Tech Stack**
*   **Language:** Python 3.11
*   **Vision:** MediaPipe (BlazePose)
*   **Math:** NumPy
*   **Display:** OpenCV
