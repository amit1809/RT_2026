# C++ Basics
- C++ https://youtu.be/ZzaPdXTrSb8?si=ZOdrS-5PEX6RjZU3
- Arduino tutorial https://docs.arduino.cc/learn/

# Intro to Object-Oriented Programing(OOP)

## What is OOP?
OOP is a programming paradigm that uses the concept of "objects" which can contain data (attributes or properties) and functions (methods) to model real-world entities.

## Why OOP?
### 4 pillars of OPP
- Abstraction
- Encapsulation
- Inheritance
- Polymorphism

Benefits
- Modularity, Reusability, Scalability
- Reduce complexity
- Eliminate redundant code



## Compare to Procedural programming
- Procedural programing: focuses on functions and procedures that operate on data.
- OOP: focuse on organizing sfotware design around objects, rather than fuctions and logic.

## Example
```cpp
#include <iostream>
using namespace std;

// Defining a class
class Car {
    // Data members (attributes)
    private:
        string model;
        int year;

    // Member functions (methods)
    public:
        // Constructor to initialize Car object
        Car(string m, int y) {
            model = m;
            year = y;
        }

        // Method to display car details
        void displayInfo() {
            cout << "Model: " << model << ", Year: " << year << endl;
        }
};

// Main function
int main() {
    // Creating objects of Car class
    Car car1("Toyota", 2020);
    Car car2("Ford", 2018);

    // Calling methods on the objects
    car1.displayInfo();
    car2.displayInfo();

    return 0;
}
```

car.h
```cpp
#include <iostream>
using namespace std;

// Class definition
class Car {
    private:
        string model;
        int year;

    public:
        // Constructor declaration
        Car(string m, int y);

        // Method to display car details
        void displayInfo();
};
```

car.cpp
```cpp
// Constructor implementation
Car::Car(string m, int y) {
    model = m;
    year = y;
}

// Method implementation
void Car::displayInfo() {
    cout << "Model: " << model << ", Year: " << year << endl;
}
```

main.cpp
```cpp
int main() {
    // Creating objects of Car class
    Car car1("Toyota", 2020);
    Car car2("Ford", 2018);

    // Calling methods on the objects
    car1.displayInfo();
    car2.displayInfo();

    return 0;
}
```

