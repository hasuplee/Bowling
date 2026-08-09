from game import Game


def test_거터_게임의_점수는_0이다():
    game = Game()
    for _ in range(20):
        game.roll(0)
    assert game.score() == 0


def test_모든_투구가_1핀이면_점수는_20이다():
    game = Game()
    for _ in range(20):
        game.roll(1)
    assert game.score() == 20


def test_한_번의_스페어는_다음_1구를_보너스로_받는다():
    game = Game()
    game.roll(5)
    game.roll(5)
    game.roll(3)
    for _ in range(17):
        game.roll(0)
    assert game.score() == 16


def test_한_번의_스트라이크는_다음_2구를_보너스로_받는다():
    game = Game()
    game.roll(10)
    game.roll(3)
    game.roll(4)
    for _ in range(16):
        game.roll(0)
    assert game.score() == 24
