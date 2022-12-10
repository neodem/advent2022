from enum import Enum


class Play(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Wld(Enum):
    WIN = 6
    LOOSE = 0
    DRAW = 3


def compute_play(them, expected_result):
    if expected_result == Wld.DRAW:
        return them

    if expected_result == Wld.WIN:
        if them == Play.ROCK:
            return Play.PAPER
        if them == Play.PAPER:
            return Play.SCISSORS
        if them == Play.SCISSORS:
            return Play.ROCK

    if expected_result == Wld.LOOSE:
        if them == Play.ROCK:
            return Play.SCISSORS
        if them == Play.PAPER:
            return Play.ROCK
        if them == Play.SCISSORS:
            return Play.PAPER


def convert_letter(letter):
    if letter == "A":
        return Play.ROCK
    if letter == "B":
        return Play.PAPER
    if letter == "C":
        return Play.SCISSORS


def convert_result(letter):
    if letter == "X":
        return Wld.LOOSE
    if letter == "Y":
        return Wld.DRAW
    if letter == "Z":
        return Wld.WIN


score_total = 0
with open("rps.dat") as file:
    for line in file:
        line = line.strip()
        if len(line) > 0:
            them = convert_letter(line[0])
            expected_result = convert_result(line[2])
            me = compute_play(them, expected_result)
            score = expected_result.value + me.value
            score_total = score_total + score
            print("expected_result {}, them: {}, me: {}, score: {}, total_score: {}".format(expected_result, them, me, score,
                                                                                   score_total))

print("total score: {}".format(score_total))
