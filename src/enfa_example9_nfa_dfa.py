"""
Hand working (summary)
----------------------
e-closures:  q0 = {q0},  q1 = {q1},  q2 = {q0, q2}

e-free NFA:  d'(q, x) = e-closure( d( e-closure(q), x ) )
             q0: a -> {q1}          b -> {}
             q1: a -> {q0, q2}      b -> {q0, q1}
             q2: a -> {q1}          b -> {}
             final: q2 only (only q2's closure contains q2)

DFA (subset construction from {q0}):
             A = {q0}          a -> B   b -> dead
             B = {q1}          a -> C   b -> D

             C = {q0, q2}  *   a -> B   b -> dead
             D = {q0, q1}      a -> E   b -> D
             E = {q0, q1, q2} *  a -> E   b -> D
             dead = {}         a -> dead  b -> dead
"""
from automata.fa.dfa import DFA
from automata.fa.nfa import NFA

# ---------------------------------------------------------------
# 1) The e-NFA  (epsilon is written as the empty string "")
# ---------------------------------------------------------------
enfa = NFA(
    states={"q0", "q1", "q2"},
    input_symbols={"a", "b"},
    transitions={
        "q0": {"a": {"q1"}},
        "q1": {"a": {"q2"}, "b": {"q0", "q1"}},
        "q2": {"": {"q0"}},
    },
    initial_state="q0",
    final_states={"q2"},
)

# ---------------------------------------------------------------
# 2) The e-free NFA (built by hand from the e-closures)
# ---------------------------------------------------------------
nfa = NFA(
    states={"q0", "q1", "q2"},
    input_symbols={"a", "b"},
    transitions={
        "q0": {"a": {"q1"}},
        "q1": {"a": {"q0", "q2"}, "b": {"q0", "q1"}},
        "q2": {"a": {"q1"}},
    },
    initial_state="q0",
    final_states={"q2"},
)

# ---------------------------------------------------------------
# 3) The DFA from the subset construction
# ---------------------------------------------------------------
dfa = DFA(
    states={"A", "B", "C", "D", "E", "dead"},
    input_symbols={"a", "b"},
    transitions={
        "A": {"a": "B", "b": "dead"},
        "B": {"a": "C", "b": "D"},
        "C": {"a": "B", "b": "dead"},
        "D": {"a": "E", "b": "D"},
        "E": {"a": "E", "b": "D"},
        "dead": {"a": "dead", "b": "dead"},
    },
    initial_state="A",
    final_states={"C", "E"},
)

# ---------------------------------------------------------------
# Optional sanity checks: all three accept the same language
# (== on automata-lib automata compares the languages they accept)
# ---------------------------------------------------------------
assert enfa == nfa, "e-NFA and e-free NFA differ"
assert DFA.from_nfa(enfa) == dfa, "DFA differs from the e-NFA"
assert len(dfa.minify().states) == 6  # already minimal
for w in ["aa", "aaaa", "aba", "abaa"]:
    assert dfa.accepts_input(w) and enfa.accepts_input(w)
for w in ["", "a", "b", "ab", "aab"]:
    assert not dfa.accepts_input(w) and not enfa.accepts_input(w)
print("All checks passed.")

from helper import save_files

save_files(enfa,"enfa-example9")
save_files(nfa,"enfa-example9-nfa")
save_files(dfa,"enfa-example9-dfa")
