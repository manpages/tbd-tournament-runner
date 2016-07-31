#!/usr/bin/env python3

import pprint
from random import randint
from twisted.internet import protocol
from twisted.internet import reactor

class DealerServer(protocol.ProcessProtocol):
  def __init__(self):
    self.id = randint(1, 10000)
    self.state = { 'ready': False
                 , 'moves': [] }
  def connectionMade(self):
    pprint.pprint('connectionMade')
  def childDataReceived(self, fd, x): 
    self.state['moves'].append((fd, x))
    if not self.state['ready'] and x == b'GO\n':
      pprint.pprint('Got go!')
      self.state['ready'] = True
      self.transport.write(b'u\n')
    else:
      pprint.pprint('Atari!')
      self.transport.write(b'd\n')
    pprint.pprint(self.state)
  def childConnectionLost(self, fd):
    pprint.pprint(str(fd) + ' stalo huyoovo')
  def proecssExited(self, reason):
    pprint.pprint('stalo sovsem huyoovo: ')
    pprint.pprint(reason)
  def processEnded(self, reason):
    pprint.pprint('RIP.')
    pprint.pprint(reason)

def main():
  dealerServer = DealerServer()
  reactor.spawnProcess(dealerServer,              # :: ProcessProtocol
                       'player.py',               # :: Executable
                       ['A', '-n 2', 'b'],        # :: Args
                       childFDs={0: 'w',          # :: Map FD Perm
                                 1: 'r',
                                 2: 'r'})
  reactor.run()

if __name__ == '__main__':
  main()
