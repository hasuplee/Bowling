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
