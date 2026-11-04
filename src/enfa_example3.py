from helper import save_files
from automata.fa.nfa import NFA



e_nfa = NFA(
    states={"q0", "q2", "q3", "q1"},
    input_symbols={"0", "1"},
    transitions={
        "q0": {"0": {"q2"}, "1": {"q1"}, "": {"q3"}},
        "q1": {"1": {"q1"}, "0": {"q3"}, "1": {"q3"}, "": {"q0"}},
        "q2": {},
        "q3": {},
    },
    initial_state="q0",
    final_states={"q2", "q3"},
)


save_files(e_nfa,"enfa-example3")


