#if (ARDUINO >= 100)
#include <Arduino.h>
#else
#include <WProgram.h>
#endif

#include <ros.h>
#include <geometry_msgs/Twist.h>
// Pin variables for motors.
const int ENA = 9;
const int ENB = 11;
const int IN1 = 5;
const int IN2 = 6;
const int IN3 = 8;
const int IN4 = 10;
int SPEED = 150;



ros::NodeHandle  nh;

void MoveFwd() {
  analogWrite (ENA,SPEED);
  analogWrite (ENB,SPEED);
  digitalWrite(IN1,HIGH);
  digitalWrite(IN2,HIGH );
  digitalWrite(IN3,LOW);
  digitalWrite( IN4,LOW);
}

void MoveStop() {
  analogWrite (ENA,SPEED);
  analogWrite (ENB,SPEED);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3,LOW);
  digitalWrite(IN4, LOW);
}
void MoveLeft() {
  analogWrite (ENA,SPEED);
  analogWrite (ENB,SPEED);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3,HIGH);
  digitalWrite(IN4, LOW);
}
void MoveRight() {
  analogWrite (ENA,SPEED);
  analogWrite (ENB,SPEED);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3,LOW);
  digitalWrite(IN4, HIGH);
}
void MoveBack() {
  analogWrite (ENA,SPEED);
  analogWrite (ENB,SPEED);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3,HIGH);
  digitalWrite(IN4, LOW);
}

void cmd_vel_cb(const geometry_msgs::Twist & msg) {
  // Read the message. Act accordingly.
  // We only care about the linear x, and the rotational z.
  const float x = msg.linear.x;
  const float z_rotation = msg.angular.z;

  // Decide on the morot state we need, according to command.
  if (x > 0 && z_rotation == 0) {
    MoveBack();
  }
  else if (x == 0 && z_rotation == 0) {
   MoveLeft();
  }
else if (x == 0 && z_rotation < 1) {
   MoveRight();
}
else if (x < 0 && z_rotation == 0) {
    MoveFwd();
  }
else{
    MoveStop();
  }
}
ros::Subscriber<geometry_msgs::Twist> sub("cmd_vel", cmd_vel_cb);
void setup() {
  pinMode(ENA,OUTPUT);
  pinMode(ENB,OUTPUT);
  pinMode(IN1, OUTPUT);    
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
//  Serial.begin(57600);
  
  
  nh.initNode();
  nh.subscribe(sub);
}

void loop() {
  nh.spinOnce();
  delay(1);
}
