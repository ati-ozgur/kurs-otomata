from automata.fa.dfa import DFA
from automata.fa.nfa import NFA

# ---------------------------------------------------------------
# 1) The e-NFA  (epsilon is written as the empty string "")
# ---------------------------------------------------------------
enfa = NFA(
    states={"q0", "q1", "q2", "q3"},
    input_symbols={"0", "1"},
    transitions={
        "q0": {"0": {"q0", "q2"}, "": {"q1"}},
        "q1": {"0": {"q3"}},
        "q2": {"1": {"q1"}, "": {"q0"}},
        "q3": {"1": {"q2"}},
    },
    initial_state="q0",
    final_states={"q3"},
)

# ---------------------------------------------------------------
# 2) The e-free NFA (built by hand from the e-closures)
#    e-closure: q0={q0,q1}, q1={q1}, q2={q0,q1,q2}, q3={q3}
# ---------------------------------------------------------------
nfa = NFA(
    states={"q0", "q1", "q2", "q3"},
    input_symbols={"0", "1"},
    transitions={
        "q0": {"0": {"q0", "q1", "q2", "q3"}},
        "q1": {"0": {"q3"}},
        "q2": {"0": {"q0", "q1", "q2", "q3"}, "1": {"q1"}},
        "q3": {"1": {"q0", "q1", "q2"}},
    },
    initial_state="q0",
    final_states={"q3"},
)

# ---------------------------------------------------------------
# 3) The DFA from the subset construction
#    A={q0}, B={q0,q1,q2,q3}, C={q0,q1,q2}, D={q1}, E={q3}, dead=empty set
# ---------------------------------------------------------------
dfa = DFA(
    states={"A", "B", "C", "D", "E", "dead"},
    input_symbols={"0", "1"},
    transitions={
        "A": {"0": "B", "1": "dead"},
        "B": {"0": "B", "1": "C"},
        "C": {"0": "B", "1": "D"},
        "D": {"0": "E", "1": "dead"},
        "E": {"0": "dead", "1": "C"},
        "dead": {"0": "dead", "1": "dead"},
    },
    initial_state="A",
    final_states={"B", "E"},
)

# ---------------------------------------------------------------
# Optional sanity checks: all three accept the same language
# (== on automata-lib automata compares the languages they accept)
# ---------------------------------------------------------------
assert enfa == nfa, "e-NFA and e-free NFA differ"
assert DFA.from_nfa(enfa) == dfa, "DFA differs from the e-NFA"
assert len(dfa.minify().states) == 6  # already minimal
for w in ["0", "00", "010", "0110"]:
    assert dfa.accepts_input(w) and enfa.accepts_input(w)
for w in ["", "1", "01", "011"]:
    assert not dfa.accepts_input(w) and not enfa.accepts_input(w)
print("All checks passed.")

from helper import save_files

save_files(enfa,"enfa-example8")
save_files(nfa,"enfa-example8-nfa")
save_files(dfa,"enfa-example8-dfa")

