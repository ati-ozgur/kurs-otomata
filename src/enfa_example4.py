from helper import save_files
from automata.fa.nfa import NFA



e_nfa = NFA(
    states={"q0", "q1", "q2"},
    input_symbols={"x", "y", "z"},
    transitions={
        "q0": {"x": {"q0"}, "": {"q1"}},
        "q1": {"y": {"q1"}, "": {"q2"}},
        "q2": {"z": {"q2"}},
    },
    initial_state="q0",
    final_states={"q2"},
)


save_files(e_nfa,"enfa-example4")


