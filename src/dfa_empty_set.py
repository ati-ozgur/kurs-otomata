from automata.fa.dfa import DFA

from helper import save_files

# DFA which accepts the empty set (no strings accepted)
dfa = DFA(
    states={'q0'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q0'}
    },
    initial_state='q0',
    final_states=set()  # Empty set of final states
)

save_files(dfa,"dfa-empty-set")