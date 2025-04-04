import sys
import logging

logging.basicConfig(level=logging.ERROR)


class FSM:
    """
    Attributes
    ----------
    states: set
        finite set of states
    alphabet: set
        finite input alphabet set
    initial_state: str
        the initial state
    final_states: set
        set of accepting/final states
    transition_function: dict
        state x input -> state transition function.
    """

    def __init__(self, states: set, alphabet: set, initial_state: str, final_states: set, transition_function: dict):
        if initial_state not in states:
            raise ValueError(f'Invalid initial state: {initial_state}')

        if not final_states.issubset(states):
            raise ValueError(f'Invalid final states: {final_states}')

        transition_states = {state for state, _ in transition_function.keys()}
        transition_states.update(
            {state for state in transition_function.values()})

        if not transition_states.issubset(states):
            raise ValueError(f'Invalid transition states: {transition_states}')

        transition_inputs = {input for _, input in transition_function.keys()}

        if not transition_inputs.issubset(alphabet):
            raise ValueError(f'Invalid transition inputs: {transition_inputs}')

        self.states = states
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.final_states = final_states
        self.transition_function = transition_function
        self.current_state = initial_state

    def transition(self, input):
        if input not in self.alphabet:
            raise ValueError(f'Invalid input: {input}')

        self.current_state = self.transition_function[(
            self.current_state, input)]


def calculate_remainder(states, alphabet, initial_state, final_states, transition_function, remainder_mapping, input_string):
    """Calculates the reminder based on the final state of the FSM"""
    fsm = FSM(states, alphabet, initial_state,
              final_states, transition_function)

    for input in input_string:
        fsm.transition(input)

    logging.debug(
        f'Input string: {input_string} - Final state: {fsm.current_state}')

    return remainder_mapping[fsm.current_state]


def main():
    if len(sys.argv) == 2:
        input_strings = sys.argv[1].split(',')
    else:        
        input_strings = ['1101', '1110', '1111', '110', '1010']
        print(f'using test inputs {input_strings}')

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

    for input_string in input_strings:
        logging.info(f'Processing input string: {input_string}')

        remainder = calculate_remainder(
            states, alphabet, initial_state, final_states, transition_function, remainder_mapping, input_string)

        logging.info(f'Input string: {input_string} - remainder: {remainder}')
        print(remainder)


if __name__ == "__main__":
    main()
