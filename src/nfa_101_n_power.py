
from helper import save_files
from automata.fa.nfa import NFA

# 1. NFA Tanımlama (caleb531/automata yapısında)
nfa = NFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'1': {'q1'}},
        'q1': {'0': {'q2'}},
        'q2': {'1': {'q3'}},
        'q3': {'': {'q0'}}  # Epsilon transition (boş geçiş)
    },
    initial_state='q0',
    final_states={'q3'}
)


save_files(nfa,"nfa-101-n-power")