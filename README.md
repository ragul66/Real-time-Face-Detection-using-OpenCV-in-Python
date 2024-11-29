Real-Time Face Detection using OpenCV in Python
This repository demonstrates a real-time face detection system using Python, leveraging powerful libraries like OpenCV, cvzone, and face recognition models. The system captures live video from a webcam, detects faces, and performs optional recognition tasks.

Features
Real-Time Face Detection using OpenCV and cvzone.
Face Recognition using face_recognition models.
Modular, well-documented code for easy customization.
Dependencies for compatibility and enhanced functionality.

Table of Contents
Installation
Usage
Dependencies
Project Workflow
Screenshots
License
Installation
Clone the Repository

bash
Copy code
git clone https://github.com/your-username/real-time-face-detection.git
cd real-time-face-detection
Set up a Virtual Environment (Optional but Recommended)

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies
Use the following command to install all required Python packages:

bash
Copy code
pip install -r requirements.txt
Install Additional Tools (if not already installed):

Make sure you have cmake installed. If not, install it using the package manager for your OS.
Usage
Run the Application
To start face detection, run:

bash
Copy code
python app.py
Optional Configurations

Modify config.py to set parameters like webcam index, detection thresholds, and model configurations.
Face Recognition (Optional)
Ensure you have a folder containing known face images for the recognition module. Update the path in the script to match your directory.

Dependencies
The project relies on the following libraries and tools:

Library	Version (Recommended)	Purpose
OpenCV	>=4.5.0	Computer Vision tasks (detection, drawing, etc.)
cvzone	>=1.5.6	Simplifies OpenCV-based tasks
face_recognition	>=1.3.0	Face recognition and encoding models
opencv-python	>=4.5.0	OpenCV's Python bindings
numpy	>=1.20.0	Matrix operations and data handling
pillow	>=8.0.0	Image processing library
wheel	>=0.37.0	Python wheels for package installation
zipp	>=3.5.0	Archive utilities for Python packages
cmake	Latest	Required for face_recognition
Install the exact versions listed in the requirements.txt file.

Project Workflow
Capture Frames
The application uses OpenCV to capture frames from the webcam.

Face Detection

Haar Cascades or DNN models detect faces in real time.
Bounding boxes are drawn around detected faces.
Face Recognition
If enabled, the script matches detected faces with pre-encoded data of known faces.

Screenshots
Add screenshots or GIFs of the application in action here.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
OpenCV for making Computer Vision accessible.
The creators of cvzone and face_recognition for simplifying development.
Contributors and testers for their support!
Contribute
Feel free to fork this repository and contribute enhancements or fixes. Create a pull request, and let’s improve it together!

Contact
For questions, suggestions, or issues, please open an issue or reach out to ragulvasanth24@gmail.com.

requirements.txt
plaintext
Copy code
opencv-python>=4.5.0
cvzone>=1.5.6
face_recognition>=1.3.0
numpy>=1.20.0
pillow>=8.0.0
wheel>=0.37.0
zipp>=3.5.0
cmake
