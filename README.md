# Emilija's Calculator Package

## Description
The package is an implementation of a calculator that performs basic math tasks written in Python. The actions implementd:

* Addition / Subtraction (adds new value to an existing in the memory)
    - ```calculator.add(2)```
* Multiplication / Division.
    - ```calculator.mul(2)```
    - ```calculator.div(2)```
* Take nth root of a number.
    - ```calculator.root(2)```
* Reset memory to ```0```
    - ```calculator.reset()```
* View current value in the memory
    - ```calculator.get_current_val()```

## Install
```
pip install -i https://test.pypi.org/simple/ calculator-package-emilijab==0.0.1
```

## Import
* Importing calculator object:
```
from calculator import calculator
```
* Importing Calculator class:
```
from calculator.calc_mod import Calculator
```