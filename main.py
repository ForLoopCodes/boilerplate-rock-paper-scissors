from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player
from unittest import main
from collections import Counter
import random

def ai_player(prev_opponent_play,
              opponent_history=[],
              play_order=[{
                  ''.join([a, b, c, d]): 0 
                  for a in 'RPS' for b in 'RPS' for c in 'RPS' for d in 'RPS'
              }]):
    if not prev_opponent_play:
        prev_opponent_play = 'P'
    opponent_history.append(prev_opponent_play)
    last_four = "".join(opponent_history[-4:])
    if len(last_four) == 4:
        play_order[0][last_four] += 1
    potential_plays = [
        last_four[1:] + "R",
        last_four[1:] + "P",
        last_four[1:] + "S",
    ] 
    sub_order = {k: play_order[0][k] for k in potential_plays if k in play_order[0]}
    if sub_order:
        prediction = max(sub_order, key=sub_order.get)[-1:]
    else:
        prediction = random.choice(['R', 'P', 'S'])
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]

x = play(ai_player, quincy, 1000)
a = play(ai_player, abbey, 1000)
b = play(ai_player, kris, 1000)
c = play(ai_player, mrugesh, 1000)

