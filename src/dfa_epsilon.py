from automata.fa.dfa import DFA

from helper import save_files


# DFA which matches only the empty string (L = {ε})
dfa = DFA(
    states={'q0', 'q_dead'},
    input_symbols={'0', '1'},
    transitions={
        'q0':     {'0': 'q_dead', '1': 'q_dead'},
        'q_dead': {'0': 'q_dead', '1': 'q_dead'}
    },
    initial_state='q0',
    final_states={'q0'}
)

save_files(dfa,"dfa-epsilon")