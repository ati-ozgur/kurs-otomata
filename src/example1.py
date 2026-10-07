# DFA where every odd position of w is '1' (1-indexed: 1st, 3rd, 5th, ...)
from automata.fa.dfa import DFA

my_dfa = DFA(
    states={'q_odd', 'q_even', 'q_dead'},
    input_symbols={'0', '1'},
    transitions={
        'q_odd':  {'0': 'q_dead', '1': 'q_even'}, # Expecting odd position (1st, 3rd...): MUST be '1'
        'q_even': {'0': 'q_odd',  '1': 'q_odd'},  # Expecting even position (2nd, 4th...): can be '0' or '1'
        'q_dead': {'0': 'q_dead', '1': 'q_dead'} # Dead state: trap for invalid strings
    },
    initial_state='q_odd',
    final_states={'q_odd', 'q_even'}
)
file_path="../content/images/example1"
file_path_pdf = file_path + ".pdf"
file_path_png = file_path + ".png"
my_dfa.show_diagram(path=file_path_pdf)
print("saved to",file_path_pdf)
my_dfa.show_diagram(path=file_path_png)
print("saved to",file_path_png)

