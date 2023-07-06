#include <stdio.h>
#include <AFMotor.h>

/*
NOTES:
    - The reason some information that will only populate a couple bits uses an entire byte is because
    with most cpu architecture, it is harder to manipulate data underthing since the cpu is built to
    interact with at least a byte.


TODO:
    - Create a way to have the Motors struct and actual motor objects be called from the same parent


Data input layout:
    unsigned 16 bit (uint16_t)
        10101           00           0       00000000
    VerifyIncoming, Motor number, Direction,  Speed
*/


// Datatypes

struct Motor
{
    uint8_t motorNumber: 2; // Stores the motor number:   0-3
    uint8_t direction: 1;   // Stores the direction:      TBD
    uint8_t isOn: 1;        // Stores state of the motor: 0|1
    uint8_t speed;          // Stores the speed value:    255
};


struct Motors
{
    Motor motor1;
    Motor motor2;
    Motor motor3;
    Motor motor4;
    Motor* motorPointers[4];

    Motors()
    {
        motorPointers[0] = &motor1;
        motorPointers[1] = &motor2;
        motorPointers[2] = &motor3;
        motorPointers[3] = &motor4;

        for (uint8_t i = 0;i<4;i++){
            motorPointers[i]->motorNumber = i + 1;
            motorPointers[i]->direction = i % 2;
        }
    }
};


struct InformationBytes
{// This is a struct and union for the incoming data from the Raspberry Pi.
    uint8_t Speed;
    uint8_t Direction: 1;
    uint8_t MotorNumber: 2;
    uint8_t Verification: 5;
};

union IntUnion
{
    InformationBytes Data;
    uint16_t rawBits;
};


// Declarations

AF_DCMotor Motor1(1),Motor2(2),Motor3(3),Motor4(4);                // Objects linked to the actual motors using the AF_Motor lib
AF_DCMotor* MotorCluster[4] = {&Motor1, &Motor2,&Motor3, &Motor4}; // Array of pointers to motors for indexing the motors
Motors motorsData;                                                 // Object storing data of the motors

IntUnion receivedData;                                             // Variable used to store incoming data from Pi
byte byte1, byte2;                                                 // Declaration of the bytes being used in data transmition
byte verificationBits = 0b10101;                                   // Bits that are used to check incoming serial. ONLY 5 BITS


// Functions

void activateMotor(){
    // TODO: Add directional motor
    if (receivedData.Data.Speed)
    { // Called if speed is non-zero
        if (!motorsData.motorPointers[receivedData.Data.MotorNumber]->isOn){            // Checks if the motor is currently running
            MotorCluster[receivedData.Data.MotorNumber]->run(FORWARD);                  // Starts the motor (direction TBA)
            motorsData.motorPointers[receivedData.Data.MotorNumber]->isOn = 1;          // Declares the motor is on
        }
        MotorCluster[receivedData.Data.MotorNumber]->setSpeed(receivedData.Data.Speed); // Sets speed of motor
    } else 
    { // Called when speed is 0
        MotorCluster[receivedData.Data.MotorNumber]->run(RELEASE);         // Better way to turn off motor than setting speed to 0
        motorsData.motorPointers[receivedData.Data.MotorNumber]->isOn = 0; // Declares the motor is off
    }
};

bool validateStartingByte(byte inByte, byte searchPattern)
{
  // Mask the first 5 bits of the byte, starting from the fourth bit
  unsigned char maskedBits = (inByte >> 3);
  return maskedBits == searchPattern;
}


// Main Arduino code

void setup()
{
    Serial.begin(9600); // Begins serial for debugging. NOTE: Disable this for more performance later (tf was I on here... I literally need this for all communication xD)
}

void loop()
{
    if (Serial.available() >= 2)
    {
        byte byte1 = Serial.read();
        if (validateStartingByte(byte1, verificationBits))
        {
            Serial.println(byte1, BIN);
            receivedData.rawBits = 0x0000;
            byte byte2 = Serial.read();
            Serial.println(byte2, BIN);

            receivedData.rawBits = byte1 << 8;
            receivedData.Data.Speed = byte2;
            Serial.println(receivedData.rawBits, BIN);
            activateMotor();
        }
    }
}
