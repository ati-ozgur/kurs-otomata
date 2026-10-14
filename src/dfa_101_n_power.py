from automata.fa.dfa import DFA
from helper import save_files

dfa = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q_D'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'1': 'q1', '0': 'q_D'},
        'q1': {'0': 'q2', '1': 'q_D'},
        'q2': {'1': 'q3', '0': 'q_D'},
        'q3': {'1': 'q1', '0': 'q_D'},   # 101'den sonra yeni bir 101 bloğu için q1'e döner
        'q_D': {'0': 'q_D', '1': 'q_D'}  # Trap / Dead State
    },
    initial_state='q0',
    final_states={'q3'}
)

save_files(dfa,"dfa-101-n-power")