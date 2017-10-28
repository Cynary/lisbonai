#!/usr/bin/python
import random


class Dist:
    # Dist(pr_map):
    #
    #  `pr_map` - map from events to their probability. Probabilities must sum
    #             to 1. All unlisted events are assumed to have probability 0
    #
    def __init__(self, pr_map):
        epsilon = 1e-9
        assert -epsilon < sum(pr_map.values())-1 < epsilon
        self.probabilities = {key: val for key, val in pr_map.items()
                              if val != 0}

    # sample:
    #
    # Returns a random sample based on the underlying probability distribution.
    #
    def sample(self):
        r = random.random()
        for e in self.events():
            r -= self.prob(e)
            if r < 0:
                return e

        return e

    # prob:
    #
    # Returns the probability of `event`
    #
    def prob(self, event):
        return self.probabilities.get(event, 0)

    # events:
    #
    # Returns the list of possible events (prob > 0)
    #
    def events(self):
        return self.probabilities.keys()


def test():
    try:
        Dist({1: 0, 2: 0.5})
        assert False
    except Exception:
        pass

    a = Dist({'a': 0, 'b': 0.1, 'c': 0, 'd': 0.9})
    assert a.prob('a') == 0
    assert a.prob('e') == 0
    assert 'a' not in a.events()
    a = Dist({'a': 0.1, 'b': 0.2, 'c': 0.7})
    epsilon = 0.1
    res = {}
    for i in range(1000):
        c = a.sample()
        res[c] = res.get(c, 0)+1
    assert all(-epsilon < res[e]/1000 - a.prob(e) < epsilon
               for e in a.events())
    print("Event:\tCount\tProbability")
    print('\n'.join('%s:\t%d\t%f' % (e, res[e], a.prob(e))
                    for e in a.events()))


if __name__ == "__main__":
    test()
