from game import Game


def test_거터_게임의_점수는_0이다():
    game = Game()
    for _ in range(20):
        game.roll(0)
    assert game.score() == 0
