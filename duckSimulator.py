# An example for strategy pattern
from abc import ABCMeta, abstractmethod


class Flybehavior(object):
    __metaclass__ = ABCMeta

    def fly(self): pass


class Flywithwing(Flybehavior):
    def fly(self):
        print "Duck: I'm flying, woohoo \m/"


class Flynoway(Flybehavior):
    def fly(self):
        print "Duck: I can't fly :("


class Duck():
    def __init__(self):
        self.flybehavior = Flybehavior()

    def performfly(self):
        self.flybehavior.fly()

    def howToFly(self, flymethod):
        self.flybehavior = flymethod

class Mypetduck(Duck):
    def __init__(self):
        self.flybehavior = Flynoway()


littleDuck = Mypetduck()
littleDuck.performfly();
print "Duck: Master, teach me how to fly pleaseeeee"
print "The Master: Ok then"
littleDuck.howToFly(Flywithwing())
littleDuck.performfly()
print "Duck:My master is awesome"