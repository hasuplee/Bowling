class Game:
    def __init__(self):
        self._rolls = []

    def roll(self, pins):
        self._rolls.append(pins)

    def score(self):
        total = 0
        roll_index = 0
        for _ in range(10):
            if self._rolls[roll_index] + self._rolls[roll_index + 1] == 10:
                total += 10 + self._rolls[roll_index + 2]
            else:
                total += self._rolls[roll_index] + self._rolls[roll_index + 1]
            roll_index += 2
        return total
