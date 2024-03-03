# Hand Detection and Control with Arduino

This project combines hand detection using OpenCV and MediaPipe with servo motor control using Arduino. It allows you to control a servo motor based on the position of your hand detected by a webcam.

## Getting Started

### Prerequisites

- Python (with OpenCV and Mediapipe libraries installed)
- Arduino IDE

### Installation

1. Clone this repository to your local machine:

git clone https://github.com/your-username/hand-detection-and-control.git

markdown
Copy code

2. Install the required Python libraries:

pip install opencv-python mediapipe

markdown
Copy code

3. Upload the Arduino code (`arduino_servo_control.ino`) to your Arduino board.

## Usage

1. Connect your Arduino board to your computer via USB.

2. Run the Python script `main.py` to start hand detection and control:

python main.py

less
Copy code

3. Place your hand in front of the webcam. The program will detect your hand and draw a bounding box around it.

4. Move your hand horizontally to control the servo motor position. The servo motor will follow the movement of your hand.

5. Press 'q' to exit the program.

## Arduino Code

The Arduino code (`arduino_servo_control.ino`) reads incoming servo angles from the Python script via serial communication and sets the position of the servo motor accordingly.

## Contributing

Contributions are welcome! If you have any suggestions, bug fixes, or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or need further assistance, feel free to contact me.
