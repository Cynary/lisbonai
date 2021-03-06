#!/usr/bin/python
from markov import MarkovModel
import dist as d


# train_model(data)
#
#  Trains a markov model by generating an initial probability distribution and
#  transition model. Also generates an end_condition function based on the
#  sequences.
#
#  `data` - array of state sequences.
#
#  Returns:
#
#   (MarkovModel, end_condition) tuple
#
def train_model(data):
    # EndState()
    #
    #  Helper, instances of this class can't be equal to states.
    #
    class EndState:
        pass

    END_STATE = EndState()

    def end_condition(state):
        return state == END_STATE

    #
    # Your code here
    #

    return (MarkovModel(d.Dist({END_STATE: 1}),
                        {END_STATE: d.Dist({END_STATE: 1})}),
            end_condition)


def test():
    data = [
        ['heads', 'heads'],
        ['heads', 'tails'],
        ['tails', 'heads'],
        ['tails', 'tails']
    ]
    mm, end_condition = train_model(data)

    epsilon = 0.1
    n = 10000
    avgLen = 0
    countHeads = 0
    countTails = 0
    for _ in range(n):
        seq = mm.random_sequence(end_condition)
        assert seq[-1] not in ('heads', 'tails')  # should be END_STATE
        avgLen += (len(seq)-1)/n
        countHeads += sum(int(s == 'heads') for s in seq)
        countTails += sum(int(s == 'tails') for s in seq)

    assert -epsilon < (avgLen-2) < epsilon
    total = countHeads + countTails
    assert -epsilon < (countHeads-countTails)/total < epsilon


if __name__ == "__main__":
    test()
