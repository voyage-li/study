from operator import add
from dice import six_sided, four_sided, make_test_dice
from ucb import main, trace, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    sum = 0
    flag = 0
    for i in range(num_rolls):
        temp = dice()
        if temp == 1:
            flag = 1
        else:
            sum += temp
    if flag == 1:
        return flag
    return sum
    "*** YOUR CODE HERE ***"
    # END PROBLEM 1


def free_bacon(score):
    """Return the points scored from rolling 0 dice (Free Bacon).

    score:  The opponent's current score.
    """
    assert score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    return 10 - score % 10+score//10
    "*** YOUR CODE HERE ***"
    # END PROBLEM 2


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 3
    if num_rolls == 0:
        return free_bacon(opponent_score)
    else:
        return roll_dice(num_rolls, dice)

    "*** YOUR CODE HERE ***"
    # END PROBLEM 3


def is_swap(player_score, opponent_score):
    """
    Return whether the two scores should be swapped
    """
    # BEGIN PROBLEM 4
    print('is_swap', player_score, opponent_score)
    if abs(player_score % 10-opponent_score % 10) == opponent_score//10 - opponent_score//100*10:
        return True
    else:
        return False
    "*** YOUR CODE HERE ***"
    # END PROBLEM 4


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who


def silence(score0, score1):
    """Announce nothing (see Phase 2)."""
    return silence


def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence, feral_hogs=True):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.
    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.
    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    say:        The commentary function to call at the end of the first turn.
    feral_hogs: A boolean indicating whether the feral hogs rule should be active.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    last_0, last_1 = 0, 0
    turn = 0
    while score0 < goal and score1 < goal:
        if who == 0:
            num_rolls = strategy0(score0, score1)
            this_turn_score = take_turn(num_rolls, score1, dice)
            score0 += this_turn_score
            if feral_hogs and abs(last_0 - num_rolls) == 2:
                score0 += 3
            if is_swap(score0, score1):
                score0, score1 = score1, score0
            last_0 = this_turn_score
        else:
            num_rolls = strategy1(score1, score0)
            this_turn_score = take_turn(num_rolls, score0, dice)
            score1 += this_turn_score
            if feral_hogs and abs(last_1 - num_rolls) == 2:
                score1 += 3
            if is_swap(score1, score0):
                score0, score1 = score1, score0
            last_1 = this_turn_score
        who = other(who)
    # END PROBLEM 5
    # (note that the indentation for the problem 6 prompt (***YOUR CODE HERE***) might be misleading)
    # BEGIN PROBLEM 6
        "*** YOUR CODE HERE ***"
        if turn == 0:
            comment = say(score0, score1)
        else:
            comment = comment(score0, score1)
        turn += 1
    # END PROBLEM 6
    return score0, score1


def fun(a, b):
    print('score', a, b)
    return fun


if __name__ == '__main__':
    import hog
    always_one = hog.make_test_dice(1)
    always_two = hog.make_test_dice(2)
    always_three = hog.make_test_dice(3)
    always = hog.always_roll
    # swap after feral hogs
    s0, s1 = play(always(2), always(1), score0=17, score1=6, goal=21, say=fun, dice=hog.make_test_dice(1, 2))
