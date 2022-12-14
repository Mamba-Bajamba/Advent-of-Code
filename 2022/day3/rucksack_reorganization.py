IPT_FN = './day3.input'


class Item:
    ITEM_SYMB: list[str] = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    SYMB_PRIORITY_MAP: dict[str: int] = {elem: i+1 for i, elem in enumerate(ITEM_SYMB)}

    @staticmethod
    def get_priority(item_str: str) -> int:
        """
        Gets the priority of an item string
        :param item_str: Single character representing an item
        :return: The priority associated with the item as an int
        """
        try:
            return Item.SYMB_PRIORITY_MAP[item_str]
        except KeyError:
            raise ValueError("Provided symbol does not match an Item symbol")


class Rucksack:
    """
    Holds compartments of items. Each compartment is expected to share only one item
    """
    def __init__(self, items_str: str):
        self.compartments = Rucksack.items_str_to_compartments(items_str)

    def get_shared_item(self) -> str:
        """
        Iterates over each compartment and returns the item that is shared by all compartments
        :return: The shared item as a string
        """
        for item in self.compartments[0]:
            for compare_item in self.compartments[1]:
                if item == compare_item:
                    return item
        raise ValueError("No differing items found")

    @staticmethod
    def items_str_to_compartments(items_str: str) -> list[str, str]:
        """
        Helper method to split item strings in half into a list of compartments
        :param items_str: Single string of items
        :return: A list of compartments, each compartment a string
        """
        items_str = items_str.rstrip('\n')
        mid = len(items_str) // 2
        compartments = [items_str[:mid], items_str[mid:]]

        return compartments


class RucksackContainer:
    """
    Container class for Rucksack objects
    """
    def __init__(self):
        self.rucksacks: list[Rucksack] = []

    def add_rucksack_by_str(self, rucksack_str: str):
        """
        Adds a Rucksack object to the container by accepting a string
        :param rucksack_str: A string representing a whole rucksack
        """
        added_rucksack = Rucksack(rucksack_str)
        self.rucksacks.append(added_rucksack)

    def calculate_shared_item_priority_sum(self) -> int:
        """
        Provides the sum of priorities of shared items in compartments of Rucksacks contained by this object
        :return: Item priority sum as an int
        """
        priority_sum = 0
        for rucksack in self.rucksacks:
            priority_sum += Item.get_priority(rucksack.get_shared_item())

        return priority_sum


def generate_rucksack_container(filename: str) -> RucksackContainer:
    """
    Iterates over lines of the provided file, adding each line to the RucksackContainer as a Rucksack object
    :param filename: Name of the data input file
    :return: The RucksackContainer holding all generated Rucksacks
    """
    rs_container = RucksackContainer()
    with open(filename) as f:
        for line in f:
            rs_container.add_rucksack_by_str(line.rstrip('\n'))

    return rs_container


def main():
    rs_container = generate_rucksack_container(IPT_FN)
    total_priority = rs_container.calculate_shared_item_priority_sum()

    print(f"The sum of the priorities for the given file is: {total_priority}")


if __name__ == "__main__":
    main()
