from automata.fa.dfa import DFA
from helper import save_files

# DFA representing the soda vending machine
soda_dfa = DFA(
    states={'q0', 'q5', 'q10', 'q_soda'},
    input_symbols={'5TL', 'İptal', 'Soda Ver'},
    transitions={
        'q0': {
            '5TL': 'q5',
            'İptal': 'q0',
            'Soda Ver': 'q0'
        },
        'q5': {
            '5TL': 'q10',
            'İptal': 'q0',
            'Soda Ver': 'q5'
        },
        'q10': {
            'Soda Ver': 'q_soda',
            'İptal': 'q0',
            '5TL': 'q10'
        },
        'q_soda': {
            '5TL': 'q_soda',
            'İptal': 'q_soda',
            'Soda Ver': 'q_soda'
        }
    },
    initial_state='q0',
    final_states={'q_soda'}
)

save_files(soda_dfa,"dfa-10tl-soda-otamat-iptal")