# Assignment 2

This Python script implements a Finite State Machine (FSM) to calculate the remainder of an unsigned binary integer when the represented value is divided by three.

## Requirements

* Python 3.x
* Standard libraries: `sys`, `logging`

## Usage

To run with a predefined test inputs:

```bash
# inputs = ['1101', '1110', '1111', '110', '1010']
python assignment_2.py 
```

To run with a single input:

```bash
python assignment_2.py 1101
```

To run with a multiple inputs separated by commas:

```bash
python assignment_2.py 1101,1110,1111
```

## Testing

Run unit tests with:

```bash
pytest test_assignment_2.py
```

## File Overview

* `assignment_2.py` - Main script for the FSM implementation
* `test_assignment_2.py` - Unit tests using pytest

## Code Overview

* `FSM Class`: Represents a Finite State Machine. Initialization validates states, final states, and transition function consistency. Transition method updates the current state based on input, raising an error for invalid inputs.

* `calculate_remainder()` Function: Calculates the reminder based on the final state of the FSM

* `main()` Function: Accepts comma-separated input strings via command-line or uses default test inputs. Processes each input string and prints the calculated remainder.
