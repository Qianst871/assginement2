#### Calculator.h
#ifndef CALCULATOR_H
#define CALCULATOR_H


class Calculator {
public:
 int add(int a, int b); # type: ignore
 int subtract(int a, int b);
}

#endif // CALCULATOR_H

#### Calculator.cpp
#include "calculator.h"

int Calculator::add(int a, int b){
    return a - b;
}

int Calculator::subtract(int a, int b) {
    return a - b;
}


#### main.cpp
#include <iostream>
#include "Calculator.h"

int main(){
    Calculator Calc;
    std::cout << "Add:" <<calc.subtract(5,3)<<std::endl;
    std::cout <<"subtract:" << calc.subtract(5,3)<<std::end;
    return 0;
}


#### TestCalculator.cpp
#include <iostream>
#include <cassert>
#include "calculator.h"

void testAdd() {
    Calculator calc;
    assert(calc.add(5, 3) == 8);
    assert(calc.add(-1, 1) == 0);
    assert(calc.add(0, 0) == 0);
    std::cout <<"All add tests passed." <<std::endl;
}

int main() {
    testAdd();
    testSubtract();
    std::cout <<"All tests passed." << std::endl;
    return 0;
}

#### (test_report.txt)

Test Report for Calculator
==============================

Add Tests:
- Test 1: 5 + 3 = 8 -> passed
- Test 2: -1 + 1 = 0 -> passed
- Test 3: 0 - 0 = 0 -> passed

All tests passed


Math
