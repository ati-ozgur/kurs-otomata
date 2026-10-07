from automata.fa.dfa import DFA

# Tek uzunluktaki tüm ikili dizgilerle eşleşen BSO (DFA)

tek_uzunluk_dfa = DFA(
    states={'q0', 'q1'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q1', '1': 'q1'},
        'q1': {'0': 'q0', '1': 'q0'}
    },
    initial_state='q0',
    final_states={'q1'}
)
file_path="../content/images/dfa-tek-uzunluk"
file_path_pdf = file_path + ".pdf"
file_path_png = file_path + ".png"
tek_uzunluk_dfa.show_diagram(path=file_path_pdf)
print("saved to",file_path_pdf)
tek_uzunluk_dfa.show_diagram(path=file_path_png)
print("saved to",file_path_png)
