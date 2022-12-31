from collections.abc import Sequence


class SliceView(Sequence):
    def __init__(self, sequence, start=None, stop=None, step=None):
        start, stop, step = slice(start, stop, step).indices(len(sequence))
        self.range = range(start, stop, step)
        self.sequence = sequence

    def __len__(self):
        return len(self.range)

    def __getitem__(self, index):
        if not isinstance(index, slice):
            return self.sequence[self.range[index]]
        else:
            return SliceView(self, index.start, index.stop, index.step)


class ChainSequence(Sequence):
    def __init__(self, *sequences):
        self.sequences = list(sequences)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return SliceView(self, index.start, index.stop, index.step)
        if index < 0:
            index += len(self)
        if not (0 <= index < len(self)):
            raise IndexError(f"Index {index} out of range.")
        for sequence in self.sequences:
            if index < len(sequence):
                return sequence[index]
            index -= len(sequence)

    def __len__(self):
        return sum(len(sequence) for sequence in self.sequences)

    def __repr__(self):
        values = f"({str(self.sequences)[1:-1]})"
        return f"ChainSequence{values}"

    def __add__(self, other):
        return ChainSequence(*self.sequences, other)

    def __iadd__(self, other):
        self.sequences.append(other)
        return self


if __name__ == '__main__':
    chain = ChainSequence('hi', [2, 1, 3, 4, 7])
    view = chain[:4]
    print(list(view), ['h', 'i', 2, 1])
    chain.sequences[1] = 'ya!'
    print(chain.sequences)
    print(list(view))
