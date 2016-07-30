#!/usr/bin/env python3

# ...

def player_won(state):

  def row_won(state):
    return check_won(state, 1)
  def col_won(state):
    return check_won(state, state['board_size'])
  def ltr_won(state):
    return check_won(state, state['board_size']+1)
  def rtl_won(state):
    return check_won(state, state['board_size']-1)

  def check_won(state, step):
    #TODO: If both dirs are false -- break
    minus_dir = True
    plus_dir = True
    in_a_row = 1
    last_move = state['last_move']
    for dist in range(1, state['to_win']-1):
     
      if minus_dir and
      #FIXME: Make out of bounds check correct
      not last_move - step < 0 and
      state['board'][last_move-step*dist] == state['active_player']:
         in_a_row +=1
        else:
          minus_dir = False
     
      if plus_dir and
      #FIXME: Make out of bounds check correct
      not last_move + step > state['board_size']**2-1 and
      state['board'][last_move+step*dist] == state['active_player']:
         in_a_row +=1
        else:
          plus_dir = False

    ####
    
    #  dirs = ((-1, lambda: last_move - step < 0,                           True),
    #          (+1, lambda: last_move + step > state['board_size']**(2-1)), True)

    #  for dist in range(1, state['to_win'] - 1):
    #    for direction in dirs:
    #      if not direction[2]:
    #        break
    #      sign           = direction[0]
    #      out_of_bounds  = direction[1]
    #      if not out_of_bounds() and state['board'][last_move + sign*(step*dist)]:
    #        in_a_row += 1
    #      else
    #        direction[2] = False
   
    #####
    
    if not in_a_row < state['to_win']:
      return True
    else:
      return False

  return ( ltr_won(state) or
           rtl_won(state) or
           row_won(state) or 
           col_won(state) )

  
 
def do_move(move, state):

  state['last_move'] = move

  def game_end(state):
    if(player_won(state['active_player'])):
      return state['active_player']
    if draw(state):
      return 'Draw'
    return 'Cont'

  state['result'] = game_end(...)
  state['player'] = (state['player'] + 1) % len(state['players'])
  return state
  
def init_game(board_size, player_num, to_win):

  def init_board(board_size):
    return ['-' for x in range(board_size ** 2)]

  state = { 'board': init_board(board_size),
            'board_size' : board_size,
            'active_player': 0,
            'last_move': (),
            'players': range(player_num),
            'to_win': to_win,
            'result': 'Cont' }

# ...

if __name__ == "__main__":
  # state = init_game()
  # while state['result'] == 'Cont':
  #   move = read_move()
  #   state = do_move(move, state)
  print("I love python")
