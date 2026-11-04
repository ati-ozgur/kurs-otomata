from helper import save_files
from automata.fa.nfa import NFA


e_nfa = NFA(
    states={"q0", "q1", "q2"},
    input_symbols={"a", "b", "c"},
    transitions={
        "q0": {"a": {"q0"}, "b": {"q1"}, "c": {"q2"}},
        "q1": {"a": {"q1"}, "b": {"q2"}, "": {"q0"}},
        "q2": {"a": {"q2"}, "c": {"q0"}, "": {"q1"}},
    },
    initial_state="q0",
    final_states={"q2"},
)


save_files(e_nfa,"enfa-example5")


