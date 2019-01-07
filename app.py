#!/usr/bin/python

from rivescript import RiveScript
import time
import random

rs = RiveScript()
rs.load_directory("./brain")
rs.sort_replies()

print """
Welcome back, user.
"""

while True:
  msg = raw_input("You: ")
  if msg == 'exit':
    quit()

  # reload the brain without having to restart the program
  # so you can work on the brain, save, and just 'reload'
  if msg == 'reload':
    rs = RiveScript()
    rs.load_directory("./brain")
    rs.sort_replies()
    continue

  # wait for a random amount of time, max two seconds (intermittent reinforcing)
  time.sleep(random.uniform(0, 2))

  reply = rs.reply("localuser", msg)
  print "Anima: ", reply
