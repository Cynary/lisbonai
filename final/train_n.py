from train import train_model


# train_model_n(data, n_states):
#
# Used to train models where state transitions depend on more than the previous
# state. Transforms the data into tuples of `n_states` states that represent
# the transformed state sequence and calls `train_model`
#
# Example: if `n_states` is 2, then a sequence of states [A, B, C, D, E, F, G]
# becomes the sequence [(A,B), (B,C), (C,D), (D,E), (E,F), (F,G)]
#
# For simplicity's sake ignore sequences in the data that are smaller than
# `n_states`
#
def train_model_n(data, n_states):
    final_data = []

    for sequence in data:
        if len(sequence) < n_states:
            continue
        final_data.append([tuple(sequence[i:i+n_states])
                           for i in range(len(sequence)-(n_states-1))])

    return train_model(final_data)
