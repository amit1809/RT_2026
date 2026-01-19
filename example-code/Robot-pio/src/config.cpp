#include "config.h"

// IMU Configuration, set to false to disable IMU
const bool useIMU = false;

// Dry run configuration - angle to stop time mapping (values in milliseconds)
const std::unordered_map<double, unsigned long> DRY_RUN_STOP_TIMES = {
    {45, 1250},  // 45°
    {90, 1600},  // 90°
    {135, 1900}, // 135°
    {180, 2200}  // 180°
};

// Robot physical parameters
const double WHEEL_DISTANCE = 155.8; // Distance between wheels in mm

// Turn compensation factors
const double LEFT_TURN_COMPENSATION = 90.01 / 90.0;  // Correction for left turns
const double RIGHT_TURN_COMPENSATION = 90.00 / 90.0; // Correction for right turns

// PID control parameters
const double TURN_PID_KP = 160.0;
const double TURN_PID_KI = 0.0;
const double TURN_PID_KD = 0.0;

// test configuration
CommandSequence origtestSequence = CommandSequence()
                                   .l()
                                   .l()
                                   .l()
                                   .l()
                                   .stop(3000)
                                   .l()
                                   .l()
                                   .l()
                                   .l()
                                   .stop(5000)
                                   .r()
                                   .r()
                                   .r()
                                   .r()
                                   .stop(3000)
                                   .r()
                                   .r()
                                   .r()
                                   .r();
// updated test sequence
CommandSequence testSequence = CommandSequence()
                                   .l()
                                   .l()
                                   .l()
                                   .l()
                                   .l()
                                   .l()
                                   .l()
                                   .l();

// competition configuration
// Define total stop time
const unsigned long totalStopTime = 0; // ms
// example run - gullso
CommandSequence OrigrunSequence = CommandSequence()
                                  .f(250 + 42 + 500 + 300)
                                  .b(300 + 500)
                                  .r()
                                  .f(1000)
                                  .l()
                                  .f()
                                  .r()
                                  .f()
                                  .l()
                                  .f(1000 + 300)
                                  .b(300 + 500)
                                  .l()
                                  .f()
                                  .r()
                                  .f(1000)
                                  .l()
                                  .f(500 + 300)
                                  .b(300 + 500)
                                  .l()
                                  .f(1000)
                                  .r()
                                  .f()
                                  .l()
                                  .f(1000)
                                  .l()
                                  .f(500 + 300)
                                  .b(300 + 500)
                                  .l()
                                  .f(1500)
                                  .l()
                                  .f(500 - 42);

// updated runsequence - test
CommandSequence runSequence = CommandSequence()
                                  .f(2000)
                                  .b(2000);
