#!/usr/bin/env python3

import argparse
import pprint
from random import randint
from enum import Enum, unique
from sys import stdin, stdout

# Protocol components should be encoded as Enums
@unique
class Move(Enum):
  up    = 'u'
  down  = 'd'
  left  = 'l'
  right = 'r'

def parse(x):
  return Move(x[0])

def format(x):
  return x.value + '\n'

def dump(x, y=666):
  with open('/tmp/python-log' + str(y), 'a') as f:
    f.write(x + '\n')

def strategy_a(move):
  if   move == Move.up:
    return Move.down
  elif move == Move.down:
    return Move.up
  elif move == Move.left:
    return Move.right
  else:
    return Move.left

def strategy_b(move):
  if   move == Move.up:
    return Move.right
  elif move == Move.down:
    return Move.left
  elif move == Move.left:
    return Move.up
  else:
    return Move.down

def strategy_c(move):
  if   move == Move.up:
    return Move.up
  elif move == Move.down:
    return Move.up
  elif move == Move.left:
    return Move.right
  else:
    return Move.right

def pick_strategy(x):
  if x == 'a':
    return strategy_a
  elif x == 'b':
    return strategy_b
  elif x == 'c':
    return strategy_c

def run_game(strategy, player_num):
  huyesh = randint(1, 10000)
  dump('Starting a game with strategy ' + strategy + '!', huyesh)
  my_moves = 0
  while(my_moves < 10):
    dump('Waiting to make a move', huyesh)
    # Pondering ( https://chessprogramming.wikispaces.com/Pondering ) is up to player implementation
    # this demo doesn't show how to do pondering in python. In fact, most likely it's not even needed,
    # see https://icfpc-tbd.slack.com/archives/general/p1469908998000046

    got = []
    for player in range(1, player_num):
      dump('... now waiting for player ' + str(player), huyesh)
      stdout.writelines('GO\n')
      got.append(parse(stdin.readline()))

    tba = ()
    for move in got:
      tba = pick_strategy(strategy)(move)
    my_moves += 1
    dump('... now making a move:', huyesh)
    dump(tba, huyesh)
    stdout.writelines(format(tba))

def main():
  parser = argparse.ArgumentParser(description='Three player pipes demo')
  parser.add_argument(dest='strategy')
  parser.add_argument('-n', type=int, dest='player_num', default=2)
  args = parser.parse_args()
  run_game(args.strategy, args.player_num)

if __name__ == '__main__':
  main()
