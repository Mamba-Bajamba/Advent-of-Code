IPT_FN = './day1.input'


class Elf:
    """
    Represents an Elf that holds calories
    """
    def __init__(self):
        self.calories: int = 0

    def add_calories(self, calories: int):
        self.calories += calories

    def get_calories(self) -> int:
        return self.calories


class ElfContainer:
    """
    Container class for Elf. Holds a list of Elf objects that is sorted by calories and has relevant helper methods
    """
    def __init__(self):
        """
        elves is a sorted list (highest calories first) of elves and assumes the Elf objects have unchanging calories
        """
        self.elves: list[Elf] = []

    def add_elf(self, new_elf: Elf):
        """
        Adds the Elf to the list while maintaining a sorted order
        :param new_elf: Elf object to be added
        """
        for i, elf in enumerate(self.elves):
            if elf.get_calories() < new_elf.get_calories():
                self.elves = self.elves[:i] + [new_elf] + self.elves[i:]
                return

        # If no elves have fewer calories, then the current elf has the fewest and is positioned at the end
        self.elves.append(new_elf)

    def get_elves(self) -> list[Elf]:
        return self.elves

    def get_top_calorie_elves(self, num_top_elves: int) -> list[Elf]:
        """
        :param num_top_elves: Number of highest-calorie elves to be retrieved
        :return: A sublist of top-calorie elves
        """
        return self.elves[:num_top_elves]

    def get_top_calorie_elves_sum(self, num_top_elves: int) -> int:
        """
        :param num_top_elves: Number of highest-calorie elves to be retrieved
        :return: The sum of all calories held by highest-calorie elves
        """
        calories_sum = 0
        for elf in self.get_top_calorie_elves(num_top_elves):
            calories_sum += elf.get_calories()
        return calories_sum


def gather_elves(filename: str) -> ElfContainer:
    """
    Reads a specified input file, creates a new Elf object for each block of calories, and adds all calories
    in the block to the relevant Elf
    :param filename: input file containing Elf calorie information
    :return: A list of Elf objects corresponding to the input file
    """
    all_elves: ElfContainer = ElfContainer()

    with open(filename) as f:
        curr_elf = None
        line = f.readline()
        while line != '':
            if line == '\n':
                # When a blank line is encountered, it represents the end of an elf's cargo
                all_elves.add_elf(curr_elf)
                curr_elf = None
            else:
                if curr_elf is None:
                    curr_elf = Elf()
                calories = int(line)
                curr_elf.add_calories(calories)
            line = f.readline()
        # Capture last Elf
        if curr_elf is not None:
            all_elves.add_elf(curr_elf)

    return all_elves


def main():
    """
    Creates an ElfContainer from a specified input file then retrieves and prints the top calorie-holding Elf's calories
    and then the top three calorie-holding Elf objects' calories
    """
    elves = gather_elves(IPT_FN)
    max_calories = elves.get_top_calorie_elves_sum(1)
    top_three_calories = elves.get_top_calorie_elves_sum(3)

    print(f"The elf with the most calories is carrying {max_calories} calories")
    print(f"The top three elves are carrying a total of {top_three_calories} calories")


if __name__ == "__main__":
    main()
