#!/usr/bin/python
import dist as d


class MarkovModel:
    # MarkovModel(initial, transitions)
    #
    #  `initial` - probability distribution on the initial state distribution.
    #
    #  `transitions` - map from state to probability distribution, which is a
    #                  distribution on how likely each state is to follow the
    #                  key state.
    #
    def __init__(self, initial, transitions):
        assert all(e in transitions for e in initial.events())
        self.initial = initial
        self.transitions = transitions

    # random_sequence(end_condition)
    #
    #  `end_condition` - function that takes a state and returns `True` /
    #                    `False` indicating whether that state ends the
    #                    sequence.
    #
    def random_sequence(self, end_condition):
        seq = [self.initial.sample()]
        while not end_condition(seq[-1]):
            seq.append(self.transitions[seq[-1]].sample())
        return seq


def test():
    initial = d.Dist({'a': 0.9, 'b': 0.1, 'c': 0})

    def end_after_n(n):
        i = 0

        def end_condition(ignored_state):
            nonlocal i
            i += 1
            return i == n
        return end_condition

    transitions = {
        'a': d.Dist({'a': 0, 'b': 0.1, 'c': 0.9}),
        'b': d.Dist({'a': 0.1, 'b': 0, 'c': 0.9}),
        'c': d.Dist({'a': 0, 'b': 0, 'c': 1})
    }

    mm = MarkovModel(initial, transitions)

    # Four checks:
    #
    # 1. First state in sequence should not be 'c' (prob = 0);
    # 2. [... 'a', 'a' ...] and [... 'b', 'b', ...] are impossible;
    # 3. The moment 'c' is reached, all following states are 'c';
    # 4. Large sequences should end in 'c'.
    #
    tries = 100
    n = 100
    for _ in range(tries):
        seq = mm.random_sequence(end_after_n(n))
        assert seq[0] != 'c'
        assert len(seq) == n
        for i in range(1, n):
            assert seq[i] == 'c' if seq[i-1] == 'c' else seq[i] != seq[i-1]
        assert seq[-1] == 'c'


if __name__ == "__main__":
    test()
