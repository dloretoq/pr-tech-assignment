import pytest
from assignment_2 import FSM, calculate_remainder


def test_valid_fsm_init():
    states = {'S0', 'S1'}
    alphabet = {'0', '1'}
    initial_state = 'S0'
    final_states = {'S1'}
    transition_function = {
        ('S0', '1'): 'S1',
        ('S1', '0'): 'S0'
    }

    fsm = FSM(states, alphabet, initial_state,
              final_states, transition_function)

    assert fsm.states == states
    assert fsm.alphabet == alphabet
    assert fsm.initial_state == initial_state
    assert fsm.final_states == final_states
    assert fsm.transition_function == transition_function
    assert fsm.current_state == initial_state


def test_invalid_initial_state():
    states = {'S0', 'S1'}
    alphabet = {'0', '1'}
    initial_state = 'S2'
    final_states = {'S1'}
    transition_function = {
        ('S0', '1'): 'S1',
        ('S1', '0'): 'S0'
    }

    with pytest.raises(ValueError) as excinfo:
        FSM(states, alphabet, initial_state, final_states, transition_function)

    assert 'Invalid initial state' in str(excinfo.value)


def test_invalid_final_state():
    states = {'S0', 'S1'}
    alphabet = {'0', '1'}
    initial_state = 'S0'
    final_states = {'S2'}
    transition_function = {
        ('S0', '1'): 'S1',
        ('S1', '0'): 'S0'
    }

    with pytest.raises(ValueError) as excinfo:
        FSM(states, alphabet, initial_state, final_states, transition_function)

    assert 'Invalid final states' in str(excinfo.value)


def test_invalid_transition_state_in_key():
    states = {'S0', 'S1'}
    alphabet = {'0', '1'}
    initial_state = 'S0'
    final_states = {'S1'}
    transition_function = {
        ('S0', '1'): 'S1',
        ('S2', '0'): 'S0'
    }

    with pytest.raises(ValueError) as excinfo:
        FSM(states, alphabet, initial_state, final_states, transition_function)

    assert 'Invalid transition states' in str(excinfo.value)


def test_invalid_transition_state_in_value():
    states = {'S0', 'S1'}
    alphabet = {'0', '1'}
    initial_state = 'S0'
    final_states = {'S1'}
    transition_function = {
        ('S0', '1'): 'S1',
        ('S1', '0'): 'S2'
    }

    with pytest.raises(ValueError) as excinfo:
        FSM(states, alphabet, initial_state, final_states, transition_function)

    assert 'Invalid transition states' in str(excinfo.value)


def test_invalid_transition_input():
    states = {'S0', 'S1'}
    alphabet = {'0', '1'}
    initial_state = 'S0'
    final_states = {'S1'}
    transition_function = {
        ('S0', '1'): 'S1',
        ('S1', '2'): 'S0'
    }

    with pytest.raises(ValueError) as excinfo:
        FSM(states, alphabet, initial_state, final_states, transition_function)

    assert 'Invalid transition inputs' in str(excinfo.value)


def test_valid_transition():
    states = {'S0', 'S1'}
    alphabet = {'0', '1'}
    initial_state = 'S0'
    final_states = {'S1'}
    transition_function = {
        ('S0', '1'): 'S1',
        ('S1', '0'): 'S0'
    }

    fsm = FSM(states, alphabet, initial_state,
              final_states, transition_function)

    fsm.transition('1')

    assert fsm.current_state == 'S1'

    fsm.transition('0')

    assert fsm.current_state == 'S0'


def test_invalid_input_transition():
    states = {'S0', 'S1'}
    alphabet = {'0', '1'}
    initial_state = 'S0'
    final_states = {'S1'}
    transition_function = {
        ('S0', '1'): 'S1',
        ('S1', '0'): 'S0'
    }

    fsm = FSM(states, alphabet, initial_state,
              final_states, transition_function)

    with pytest.raises(ValueError) as excinfo:
        fsm.transition('2')

    assert 'Invalid input' in str(excinfo.value)


def test_calculate_remainder_valid_input():
    states = {'S0', 'S1', 'S2'}
    alphabet = {'0', '1'}
    initial_state = 'S0'
    final_states = {'S0', 'S1', 'S2'}
    transition_function = {
        ('S0', '0'): 'S0',
        ('S0', '1'): 'S1',
        ('S1', '0'): 'S2',
        ('S1', '1'): 'S0',
        ('S2', '0'): 'S1',
        ('S2', '1'): 'S2'
    }
    remainder_mapping = {'S0': 0, 'S1': 1, 'S2': 2}

    input_strings = ['1101', '1110', '1111']
    expected_remainders = [1, 2, 0]

    for input_string, expected_remainder in zip(input_strings, expected_remainders):
        actual_remainder = calculate_remainder(states, alphabet, initial_state,
                                               final_states, transition_function, remainder_mapping, input_string)

        assert expected_remainder == actual_remainder


def test_calculate_remainder_invalid_input():
    states = {'S0', 'S1', 'S2'}
    alphabet = {'0', '1'}
    initial_state = 'S0'
    final_states = {'S0', 'S1', 'S2'}
    transition_function = {
        ('S0', '0'): 'S0',
        ('S0', '1'): 'S1',
        ('S1', '0'): 'S2',
        ('S1', '1'): 'S0',
        ('S2', '0'): 'S1',
        ('S2', '1'): 'S2'
    }
    remainder_mapping = {'S0': 0, 'S1': 1, 'S2': 2}

    input_string = '120'

    with pytest.raises(ValueError) as excinfo:
        calculate_remainder(states, alphabet, initial_state,
                            final_states, transition_function, remainder_mapping, input_string)

    assert 'Invalid input' in str(excinfo.value)


def test_calculate_remainder_empty_input():
    states = {'S0', 'S1', 'S2'}
    alphabet = {'0', '1'}
    initial_state = 'S0'
    final_states = {'S0', 'S1', 'S2'}
    transition_function = {
        ('S0', '0'): 'S0',
        ('S0', '1'): 'S1',
        ('S1', '0'): 'S2',
        ('S1', '1'): 'S0',
        ('S2', '0'): 'S1',
        ('S2', '1'): 'S2'
    }
    remainder_mapping = {'S0': 0, 'S1': 1, 'S2': 2}

    input_string = ''
    remainder = calculate_remainder(states, alphabet, initial_state,
                                    final_states, transition_function, remainder_mapping, input_string)
    assert remainder == 0
