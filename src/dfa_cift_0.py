#dfa_example1.py
from automata.fa.dfa import DFA

# DFA which matches all binary strings ending in an odd number of '1's
my_dfa = DFA(
    states={'q_cift', 'q_tek'},
    input_symbols={'0','1'},
    transitions={
        'q_cift': {'0': 'q_tek','1': 'q_cift'},
        'q_tek': {'0': 'q_cift','1': 'q_tek'}
    },
    initial_state='q_cift',
    final_states={'q_cift'}
)
file_path="../content/images/dfa-cift-0-otomat1"
file_path_pdf = file_path + ".pdf"
file_path_png = file_path + ".png"
my_dfa.show_diagram(path=file_path_pdf)
print("saved to",file_path_pdf)
my_dfa.show_diagram(path=file_path_png)
print("saved to",file_path_png)
