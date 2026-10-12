# dfa_1_basla_0_bit.py

from automata.fa.dfa import DFA
from helper import save_files

dfa = DFA(
    states={'q_s', 'q1', 'q2', 'q_tuzak'},
    input_symbols={'0', '1'},
    transitions={
        'q_s': {
            '1': 'q1',        # '1' ile başlarsa devam et
            '0': 'q_tuzak'   # '0' ile başlarsa reddet (tuzağa git)
        },
        'q1': {
            '0': 'q2',        # '0' gelirse sonu '0' olduğu için kabul durumuna geç
            '1': 'q1'         # '1' gelirse sonu '1' kalmaya devam eder
        },
        'q2': {
            '0': 'q2',        # '0' gelmeye devam ederse kabul durumunda kal
            '1': 'q1'         # '1' gelirse sonu tekrar '1' olduğu için q1'e dön
        },
        'q_tuzak': {
            '0': 'q_tuzak',  # Yanlış başlayan kelimeler hiçbir zaman kabul edilmez
            '1': 'q_tuzak'
        }
    },
    initial_state='q_s',
    final_states={'q2'}
)

save_files(dfa,"dfa_1_basla_0_bit")