from helper import save_files
from automata.fa.nfa import NFA


e_nfa = NFA(
    states={"A", "B", "C", "D"},
    input_symbols={"0", "1"},
    transitions={
        "A": {"0": {"A"}, "": {"B"}},
        "B": {"0": {"C"}, "": {"D"}},
        "C": {"1": {"B"}},
        "D": {"0": {"D"}, "1": {"D"}},
    },
    initial_state="A",
    final_states={"D"},
)


save_files(e_nfa,"enfa-example2")


