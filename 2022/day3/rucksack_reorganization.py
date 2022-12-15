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
    Holds compartments of items. Each compartment is expected to share exactly one item
    """
    def __init__(self, items_str: str):
        self.compartments = Rucksack.items_str_to_compartments(items_str)

    def get_duplicated_item(self) -> str:
        """
        Iterates over each compartment and returns the item that is duplicated by all compartments
        :return: The duplicated item as a string
        """
        for item in self.compartments[0]:
            for compare_item in self.compartments[1]:
                if item == compare_item:
                    return item
        raise ValueError("No duplicated items found")

    def get_all_items(self) -> str:
        return ''.join(self.compartments)

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
    Container class for Rucksack objects which can also act as a group of Elf rucksacks
    """
    def __init__(self):
        self.rucksacks: list[Rucksack] = []

    def get_num_rucksacks(self):
        return len(self.rucksacks)

    def add_rucksack_by_str(self, rucksack_str: str):
        """
        Adds a Rucksack object to the container by accepting a string
        :param rucksack_str: A string representing a whole rucksack
        """
        added_rucksack = Rucksack(rucksack_str)
        self.rucksacks.append(added_rucksack)

    def calculate_duplicated_item_priority_sum(self) -> int:
        """
        Provides the sum of priorities of duplicated items in compartments of Rucksacks contained by this object
        :return: Item priority sum as an int
        """
        priority_sum = 0
        for rucksack in self.rucksacks:
            priority_sum += Item.get_priority(rucksack.get_duplicated_item())

        return priority_sum

    def find_shared_badge_item(self) -> str:
        """
        Finds the single shared badge item across a group of Rucksacks
        :return: Shared item as a string (single character)
        """
        if len(self.rucksacks) == 0:
            return ''

        # Retrieves a list of items that are shared among all Rucksacks in this RucksackContainer using set methods
        shared_items: list[str] = list(set.intersection(*[set(rucksack.get_all_items()) for rucksack in self.rucksacks]))

        if len(shared_items) != 1:
            raise ValueError("Number of shared items within group must be exactly 1")

        shared_badge_item: str = shared_items[0]
        return shared_badge_item


def generate_rucksack_container_from_file(filename: str) -> RucksackContainer:
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


def generate_groups_from_file(filename: str, group_size: int) -> list[RucksackContainer]:
    """
    Iterates over lines of the provided file, creating a RucksackContainer for each group of group_size lines,
    adding each group to the list
    :param filename: Name of the data input file
    :param group_size: Number of Rucksacks in each group
    :return: List of RucksackContainers, each element representing an elf group
    """
    all_groups: list[RucksackContainer] = []
    with open(filename) as f:
        curr_rs_container = RucksackContainer()
        all_groups.append(curr_rs_container)
        for line in f:
            if curr_rs_container.get_num_rucksacks() >= group_size:
                # A new group is created every time the group_size limit is met
                curr_rs_container = RucksackContainer()
                all_groups.append(curr_rs_container)
            curr_rs_container.add_rucksack_by_str(line.rstrip('\n'))

    return all_groups


def calculate_badge_priority_sum(all_groups: list[RucksackContainer]) -> int:
    """
    Traverses the groups in all_groups and adds the priority of the shared badge item of that group to a sum
    :param all_groups: A list of RucksackContainers, each representing a group
    :return: The sum of priorities of the shared badge items for all groups
    """
    priority_sum: int = 0
    for group in all_groups:
        group_badge_item = group.find_shared_badge_item()
        priority_sum += Item.get_priority(group_badge_item)

    return priority_sum


def main():
    rs_container = generate_rucksack_container_from_file(IPT_FN)
    total_shared_item_priority = rs_container.calculate_duplicated_item_priority_sum()

    elf_groups = generate_groups_from_file(IPT_FN, group_size=3)
    group_badge_priority_sum = calculate_badge_priority_sum(elf_groups)

    print(f"The sum of the priorities for shared items in the given file is: {total_shared_item_priority}")
    print(f"The sum of the priorities for badge items for all elf groups in the given file is: {group_badge_priority_sum}")


if __name__ == "__main__":
    main()
