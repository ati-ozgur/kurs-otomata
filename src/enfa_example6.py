from helper import save_files
from automata.fa.nfa import NFA


e_nfa = NFA(
    states={"1", "2", "3", "4", "5", "6", "7"},
    input_symbols={"a", "b"},
    transitions={
        "1": {"": {"2", "4"}},
        "2": {"": {"3"}},
        "3": {"": {"6"}},
        "4": {"a": {"5"}},
        "5": {"b": {"6"}, "": {"7"}},
        "6": {},
        "7": {},
    },
    initial_state="1",
    final_states={"6", "7"},
)


save_files(e_nfa,"enfa-example6")


