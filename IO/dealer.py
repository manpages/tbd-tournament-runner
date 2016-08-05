#!/usr/bin/env python3

import pprint
from twisted.internet import protocol
from twisted.internet import reactor

class DealerServer(protocol.ProcessProtocol):
  def __init__(self):
    self.moves = []
    self.subscriptions = []
  def connectionMade(self):
    pprint.pprint("Connected!")
    return
  def childDataReceived(self, fd, x): 
    pprint.pprint("Got move:" + str(x))
    self.moves.append(x)
    for ds in self.subscriptions:
      ds.send(x)
  def childConnectionLost(self, fd):
    pprint.pprint(fd)
  def proecssExited(self, reason):
    pprint.pprint(reason)
  def processEnded(self, reason):
    pprint.pprint(self.moves)
  def subscribe(self, ds):
    self.subscriptions.append(ds)
  def send(self, x):
    self.transport.write(x)

def main():
  def cpp(x):
   return chr(ord(x) + 1) 
  dealerServers = [ DealerServer()
                  , DealerServer()
                  , DealerServer() ]
  for dsi in dealerServers:
    for dsj in dealerServers:
      if dsi != dsj:
        dsi.subscribe(dsj)
  strat = '`'
  for dsk in dealerServers:
    strat = cpp(strat)
    pprint.pprint("Spawning process with strategy " + strat)
    reactor.spawnProcess(dsk,                       # :: ProcessProtocol
                         'player.py',               # :: Executable
                         ['A', '-n 3', strat],      # :: Args
                         childFDs={0: 'w',          # :: Map FD Perm
                                   1: 'r',
                                   2: 'r'})
  reactor.run()

if __name__ == '__main__':
  main()
