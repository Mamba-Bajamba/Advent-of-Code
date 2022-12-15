IPT_FN = './day4.input'


class RangePair:
    """
    Stores a tuple for two ranges of integers
    """

    def __init__(self, pair_str: str):
        self.range_a, self.range_b = RangePair.pair_str_to_tuples(pair_str)

    def one_contains(self) -> bool:
        """
        Determines if either pair is entirely within the range of the other pair, including if they overlap exactly
        :return: True if either pair contains the other, False otherwise
        """
        return ((self.range_a[0] >= self.range_b[0]) and (self.range_a[1] <= self.range_b[1])) \
               or ((self.range_a[0] <= self.range_b[0]) and (self.range_a[1] >= self.range_b[1]))

    def one_overlaps(self) -> bool:
        """
        Determines if either pair overlaps the other pair
        :return: True if either pair overlaps the other, False otherwise
        """
        return ((self.range_a[0] >= self.range_b[0]) and (self.range_a[0] <= self.range_b[1])) \
               or ((self.range_b[0] >= self.range_a[0]) and (self.range_b[0] <= self.range_a[1]))

    @staticmethod
    def pair_str_to_tuples(pair_str: str) -> tuple[tuple[int, int], tuple[int, int]]:
        """
        Converts a pair_str to nested tuples to be unpacked
        :param pair_str: Represents a pair in the format: <int>-<int>,<int>-<int>
        :return: A nested tuple to be unpacked
        """
        try:
            range_a_start, range_a_end = pair_str.split(',')[0].split('-')
            range_b_start, range_b_end = pair_str.split(',')[1].split('-')
            range_a = (int(range_a_start), int(range_a_end))
            range_b = (int(range_b_start), int(range_b_end))
        except ValueError or IndexError:
            raise ValueError("Pair str is incorrectly formatted")

        return range_a, range_b


class RangePairContainer:
    """
    Container class for RangePair
    """
    def __init__(self):
        self.pairs = []

    def add_pair(self, pair_str: str):
        """
        Creates a RangePair from the provided argument and adds it to the pairs list
        :param pair_str: Represents a pair in the format: <int>-<int>,<int>-<int>
        """
        added_pair = RangePair(pair_str)
        self.pairs.append(added_pair)

    def count_contains(self) -> int:
        """
        Counts the number of RangePairs in the collection that have one range containing the other
        :return: The number of contained pairs as an integer
        """
        count = 0
        for pair in self.pairs:
            if pair.one_contains():
                count += 1
        return count

    def count_overlaps(self) -> int:
        """
        Counts the number of RangePairs in the collection that have one range overlapping the other
        :return: The number of overlapping pairs as an integer
        """
        count = 0
        for pair in self.pairs:
            if pair.one_overlaps():
                count += 1
        return count


def create_pair_container_from_file(filename: str) -> RangePairContainer:
    """
    Creates a RangePairContainer and adds each line of the given file as a pair
    :param filename: Name of the data input file
    :return: The RangePairContainer holding all RangePairs
    """
    pair_container = RangePairContainer()
    with open(filename) as f:
        for line in f:
            pair_container.add_pair(line.rstrip('\n'))

    return pair_container


def main():
    pair_container = create_pair_container_from_file(IPT_FN)
    contains_count = pair_container.count_contains()
    overlaps_count = pair_container.count_overlaps()

    print(f"The number of assignment pairs in which one range fully contains the other is: {contains_count}")
    print(f"The number of assignment pairs in which one range overlaps the other is: {overlaps_count}")


if __name__ == "__main__":
    main()
