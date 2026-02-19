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


// test configuration
const double rt = 94.35;   //So I think that the kp thing applies only to IMU, at least thats what the ai said
const double lt = 95 ;
const double rh = (rt / 2);
const double lh = (lt / 2);
const double a = 0.75; //cos^-1(199.8/200) is how we determined it
const double d = 1.414; // √2, for diagonal movement

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
                                  .r(rt)
                                  .r(rt)
                                  .r(rt)
                                  .r(rt)
                                  .r(rt)
                                  .r(rt)
                                  .r(rt)
                                  .r(rt)
                                  .r(rt)
                                  .r(rt)
                                  .r(rt)
                                  .r(rt)
                                  .r(rt)
                                  .r(rt)
                                  .r(rt)
                                  .r(rt)
                                  .f(1500)
                                  .stop(3000)
                                  .r(rh)
                                  .b(1000)
                                 
                                   ;

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
                                  .f(500 - 42)
                                ;


// updated runsequence - test
// .l(a)
// .r(a)
CommandSequence runSequence = CommandSequence()
                              
                                .l(lh)
                                .f(250 * d)
                                .r(rt + rh)
                                .f(1250)
                                .r(rt)
                                .b(250)
                                .r(rt + rh)
                                .f(500 * d)
                                .r(rh)
                                .f(1000)
                                .r(rh)
                                .f(250 * d)
                                .r(rh)
                                .f(250)
                                .r(rt)
                                .f(300)
                                .b(300)
                                .r(rt)
                                .f(500)
                                .l(lt)
                                .f(250)
                                .r(rh)
                                .f(500 * d)
                                .r(rt)
                                .f(500 * d)
                                .r(rt)
                                .f(400 * d)
                                .b(400 * d)
                                .r(rt + rh)
                                .f(1100)
                                .b(1100) // adj = current here - 850
                                .l(lh)
                                .f(500 * d)
                                .r(rh)
                                .f(850)
                                .l(lh + lt)
                                .f(400 * d)
                                .b(400 * d)
                                .l(lh)
                                .f(110)
;
