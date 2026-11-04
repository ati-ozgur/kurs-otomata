from helper import save_files
from automata.fa.nfa import NFA

e_nfa = NFA(
    states={"A", "B", "C"},
    input_symbols={"a", "b", "c"},
    transitions={
        "A": {"a": {"A"}, "": {"B"}},
        "B": {"b": {"B"}, "": {"C"}},
        "C": {"c": {"C"}},
    },
    initial_state="A",
    final_states={"C"},
)


save_files(e_nfa,"enfa-example1")


