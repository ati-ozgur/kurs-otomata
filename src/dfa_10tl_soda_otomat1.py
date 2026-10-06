#dfa_example1.py
from automata.fa.dfa import DFA

# DFA which matches all binary strings ending in an odd number of '1's
my_dfa = DFA(
    states={'q0', 'q5', 'q_soda'},
    input_symbols={'5'},
    transitions={
        'q0': {'5': 'q5'},
        'q5': {'5': 'q_soda'},
        'q_soda': {'5': 'q_soda'}
    },
    initial_state='q0',
    final_states={'q_soda'}
)
file_path="../content/images/dfa-10tl-soda-otomat1"
file_path_pdf = file_path + ".pdf"
file_path_png = file_path + ".png"
my_dfa.show_diagram(path=file_path_pdf)
print("saved to",file_path_pdf)
my_dfa.show_diagram(path=file_path_png)
print("saved to",file_path_png)
