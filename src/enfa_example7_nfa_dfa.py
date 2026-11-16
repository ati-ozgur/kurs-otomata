from automata.fa.dfa import DFA
from automata.fa.nfa import NFA

# ---------------------------------------------------------------
# 1) The e-NFA  (epsilon is written as the empty string "")
# ---------------------------------------------------------------
enfa = NFA(
    states={"q0", "q1", "q2", "q3"},
    input_symbols={"a", "b"},
    transitions={
        "q0": {"a": {"q1"}, "": {"q2"}},
        "q1": {"b": {"q1"}, "": {"q3"}},
        "q2": {"a": {"q2"}, "b": {"q3"}},
        "q3": {"a": {"q3"}},
    },
    initial_state="q0",
    final_states={"q3"},
)

# ---------------------------------------------------------------
# 2) The e-free NFA (built by hand from the e-closures)
# ---------------------------------------------------------------
nfa = NFA(
    states={"q0", "q1", "q2", "q3"},
    input_symbols={"a", "b"},
    transitions={
        "q0": {"a": {"q1", "q2", "q3"}, "b": {"q3"}},
        "q1": {"a": {"q3"}, "b": {"q1", "q3"}},
        "q2": {"a": {"q2"}, "b": {"q3"}},
        "q3": {"a": {"q3"}},
    },
    initial_state="q0",
    final_states={"q1", "q3"},
)

# ---------------------------------------------------------------
# 3) The DFA from the subset construction
#    A={q0}, B={q1,q2,q3}, C={q3}, D={q2,q3}, E={q1,q3}, dead=empty set
# ---------------------------------------------------------------
dfa = DFA(
    states={"A", "B", "C", "D", "E", "dead"},
    input_symbols={"a", "b"},
    transitions={
        "A": {"a": "B", "b": "C"},
        "B": {"a": "D", "b": "E"},
        "C": {"a": "C", "b": "dead"},
        "D": {"a": "D", "b": "C"},
        "E": {"a": "C", "b": "E"},
        "dead": {"a": "dead", "b": "dead"},
    },
    initial_state="A",
    final_states={"B", "C", "D", "E"},
)

# ---------------------------------------------------------------
# Optional sanity checks: all three accept the same language
# (== on automata-lib automata compares the languages they accept)
# ---------------------------------------------------------------
assert enfa == nfa, "e-NFA and e-free NFA differ"
assert DFA.from_nfa(enfa) == dfa, "DFA differs from the e-NFA"
assert dfa.minify() == dfa and len(dfa.minify().states) == 6  # already minimal
for w in ["ab", "ba", "aab", "abbb", "aaa"]:
    assert dfa.accepts_input(w)
for w in ["", "bb", "abab", "bab"]:
    assert not dfa.accepts_input(w)
print("All checks passed.")

# ---------------------------------------------------------------
# Diagrams
# In Jupyter, just put e.g. `enfa.show_diagram()` as the last line of a
# cell to display it. The `path=` argument saves the image to a file.
# ---------------------------------------------------------------

from helper import save_files

save_files(enfa,"enfa-example7")
save_files(nfa,"enfa-example7-nfa")
save_files(dfa,"enfa-example7-dfa")

