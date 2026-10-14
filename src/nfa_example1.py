from automata.fa.nfa import NFA
from helper import save_files

# NFA which matches strings beginning with "a", ending with "a", and
# containing no consecutive "b"s
nfa = NFA(
    states={"q0", "q1", "q2"},
    input_symbols={"a", "b"},
    transitions={
        "q0": {"a": {"q1"}},
        "q1": {"a": {"q1"}, "": {"q2"}},
        "q2": {"b": {"q0"}},
    },
    initial_state="q0",
    final_states={"q1"},
)

save_files(nfa,"nfa-example1")
