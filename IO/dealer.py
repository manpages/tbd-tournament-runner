#!/usr/bin/env python3

import pprint
from random import randint
from twisted.internet import protocol
from twisted.internet import reactor

class DealerServer(protocol.ProcessProtocol):
  def __init__(self):
    self.id = randint(1, 10000)
    self.state = { 'moves': [] }
  def connectionMade(self):
    pprint.pprint('connectionMade')
    self.transport.write(b'u\n')
  def childDataReceived(self, fd, x): 
    self.state['moves'].append((fd, x))
    self.transport.write(b'd\n')
  def childConnectionLost(self, fd):
    pprint.pprint(fd)
  def proecssExited(self, reason):
    pprint.pprint(reason)
  def processEnded(self, reason):
    pprint.pprint(self.state)

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
