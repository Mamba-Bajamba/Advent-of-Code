IPT_FN = './day2.input'


class Shape:
    ROCK: int = 0
    PAPER: int = 1
    SCISSORS: int = 2

    SHAPE_SYMB_MAP: dict[str: int] = {
        'A': ROCK,
        'B': PAPER,
        'C': SCISSORS
    }

    SHAPE_POINTS_MAP: dict[int: int] = {
        ROCK: 1,
        PAPER: 2,
        SCISSORS: 3
    }

    SHAPE_VICTORY_MAP: dict[int: int] = {
        ROCK: SCISSORS,
        PAPER: ROCK,
        SCISSORS: PAPER
    }

    @staticmethod
    def str_to_shape(shape_str: str) -> int:
        """
        Converts a shape string to a shape enum
        :return: A shape enum
        """
        return Shape.SHAPE_SYMB_MAP[shape_str]

    @staticmethod
    def get_shape_points(shape_enum: int) -> int:
        """
        Provides the points given for playing a certain shape
        :return: Points in integers
        """
        return Shape.SHAPE_POINTS_MAP[shape_enum]

    @staticmethod
    def get_shape_victory_map() -> dict[int: int]:
        """
        :return: Victory map for shapes as a dictionary
        """
        return Shape.SHAPE_VICTORY_MAP


class GameRound:
    POINTS_VICTORY = 6
    POINTS_DRAW = 3
    POINTS_LOSS = 0

    ROUND_STRATEGY_MAP: dict[dict[int: int]] = {
        'X': {
            Shape.ROCK: Shape.SCISSORS,
            Shape.PAPER: Shape.ROCK,
            Shape.SCISSORS: Shape.PAPER
        },
        'Y': {
            Shape.ROCK: Shape.ROCK,
            Shape.PAPER: Shape.PAPER,
            Shape.SCISSORS: Shape.SCISSORS
        },
        'Z': {
            Shape.ROCK: Shape.PAPER,
            Shape.PAPER: Shape.SCISSORS,
            Shape.SCISSORS: Shape.ROCK
        }
    }

    def __init__(self, opponent_shape_symb: str, player_strategy_symb: str):
        """
        Accepts strings representing play shapes and response shapes and stores them as Shape enums
        :param opponent_shape_symb: The shape played by the opponent
        :param player_strategy_symb: The shape played in response by the player
        """
        try:
            self.opponent_shape = Shape.str_to_shape(opponent_shape_symb)
            self.player_shape = GameRound.ROUND_STRATEGY_MAP[player_strategy_symb][self.opponent_shape]
        except KeyError:
            raise ValueError("A symbol provided did not match any shape")

    def get_round_points(self) -> int:
        """
        Implements game rules to produce the points won by the player for the given game round
        :return: Points won as integers
        """
        # Player acquires points from their shape played
        points_won = Shape.SHAPE_POINTS_MAP[self.player_shape]
        shape_victory_map = Shape.get_shape_victory_map()
        round_victory = shape_victory_map[self.player_shape] == self.opponent_shape

        if round_victory:
            points_won += GameRound.POINTS_VICTORY
        if self.opponent_shape == self.player_shape:
            # Represents a draw
            points_won += GameRound.POINTS_DRAW
        else:
            # Represents a loss
            points_won += GameRound.POINTS_LOSS

        return points_won


class Game:
    """
    Container class for GameRound objects
    """

    def __init__(self):
        self.game_rounds: list[GameRound] = []

    def add_round_as_str(self, game_round_str: str):
        game_round_str = game_round_str.rstrip('\n')
        if len(game_round_str) != 3:
            raise ValueError("Shape line is formatted incorrectly")

        shape_symbols = game_round_str.split(' ')
        if len(shape_symbols) != 2:
            raise ValueError("Shape line does not contain a space")

        game_round = GameRound(opponent_shape_symb=shape_symbols[0], player_strategy_symb=shape_symbols[1])
        self.game_rounds.append(game_round)

    def calculate_total_points(self) -> int:
        total_points: int = 0
        for game_round in self.game_rounds:
            total_points += game_round.get_round_points()

        return total_points


def create_game(filename: str) -> Game:
    game = Game()
    with open(filename) as f:
        for line in f:
            game.add_round_as_str(line)

    return game


def main():
    game = create_game(IPT_FN)
    total_points = game.calculate_total_points()

    print(f"The total points for the provided strategy guide are: {total_points}")


if __name__ == "__main__":
    main()
