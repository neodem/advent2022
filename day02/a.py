from enum import Enum


class Play(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Wld(Enum):
    WIN = 6
    LOOSE = 0
    DRAW = 3


def score_game(me, them):
    if me == them:
        return Wld.DRAW

    if me == Play.ROCK:
        if them == Play.PAPER:
            return Wld.LOOSE
        if them == Play.SCISSORS:
            return Wld.WIN

    if me == Play.PAPER:
        if them == Play.ROCK:
            return Wld.WIN
        if them == Play.SCISSORS:
            return Wld.LOOSE

    if me == Play.SCISSORS:
        if them == Play.ROCK:
            return Wld.LOOSE
        if them == Play.PAPER:
            return Wld.WIN


def convert(letter):
    if letter == "A" or letter == "X":
        return Play.ROCK
    if letter == "B" or letter == "Y":
        return Play.PAPER
    if letter == "C" or letter == "Z":
        return Play.SCISSORS


score_total = 0
with open("rps.dat") as file:
    for line in file:
        line = line.strip()
        if len(line) > 0:
            me = convert(line[2])
            them = convert(line[0])
            game_result = score_game(me, them)
            score = game_result.value + me.value
            score_total = score_total + score
            print("me: {}, them: {}, result {}, score: {}, total_score: {}".format(me, them, game_result, score,
                                                                                   score_total))

print("total score: {}".format(score_total))
