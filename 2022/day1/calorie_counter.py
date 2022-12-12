IPT_FN = './day1.input'


class Elf:
    def __init__(self):
        self.calories: int = 0

    def add_calories(self, calories: int):
        if calories > 0:
            self.calories += calories

    def get_calories(self) -> int:
        return self.calories


def gather_elves() -> list[Elf]:
    elves: list[Elf] = []

    with open(IPT_FN) as f:
        curr_elf = Elf()
        line = f.readline()
        while line != '':
            if line == '\n':
                curr_elf = Elf()
                elves.append(curr_elf)
            else:
                calories = int(line)
                curr_elf.add_calories(calories)
            line = f.readline()

    return elves


def get_max_calorie_elf(elves: list[Elf]) -> Elf:
    if len(elves) == 0:
        return
    max_calorie_elf = elves[0]
    for curr_elf in elves:
        if curr_elf.get_calories() > max_calorie_elf.get_calories():
            max_calorie_elf = curr_elf

    return max_calorie_elf


def main():
    elves = gather_elves()
    max_calorie_elf = get_max_calorie_elf(elves)
    max_calories = max_calorie_elf.get_calories()

    print(f"The elf with the most calories has {max_calories} calories")


if __name__ == "__main__":
    main()
