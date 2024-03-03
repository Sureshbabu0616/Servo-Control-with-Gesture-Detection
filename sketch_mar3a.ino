#include <Servo.h>

Servo myservo;  // Create a servo object

int servo_pin = 9;  // Adjust as needed (pin connected to servo)

void setup() {
  Serial.begin(9600);  // Start serial communication at 9600 baud rate
  myservo.attach(servo_pin);  // Attach servo to specified pin
}

void loop() {
  if (Serial.available() > 0) {
    // Read incoming servo angle from Python code
    String servo_angle_str = Serial.readStringUntil('\n');
    servo_angle_str.trim();  // Remove leading/trailing whitespace

    // Convert string to integer
    int servo_angle = servo_angle_str.toInt();

    // Set servo position
    myservo.write(servo_angle);
  }

  // Add a small delay (optional)
  delay(10);
}
