class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
    def __str__(self):
        return self.name

def insert(atMe, newFrob):
    if newFrob.myName() > atMe.myName():
        next = atMe.getAfter()
        if next:
            if newFrob.myName() < next.myName():
                next.setBefore(newFrob) 
                atMe.setAfter(newFrob)
                newFrob.setBefore(atMe)
                newFrob.setAfter(next)
            else:
                insert(atMe.getAfter(), newFrob)
        else:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
    elif newFrob.myName() < atMe.myName():
        prev = atMe.getBefore()
        if prev:
            if newFrob.myName() > prev.myName():
                prev.setAfter(newFrob)
                atMe.setBefore(newFrob)
                newFrob.setAfter(atMe)
                newFrob.setBefore(prev)
            else:
                insert(atMe.getBefore(), newFrob)
        else:
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
    else:
        next = atMe.getAfter()
        if next:
            next.setBefore(newFrob)
            newFrob.setAfter(next)
        atMe.setAfter(newFrob)
        prev = atMe.getBefore()
        if prev:
            prev.setAfter(newFrob)
            newFrob.setBefore(prev)
        newFrob.setBefore(atMe)

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    if start.getBefore():
        return findFront(start.getBefore())
    else:
        return start

test_list = Frob('leonid')
a = Frob('amara')
j1 = Frob('jennifer')
j2 = Frob('jennifer')
s = Frob('scott')

insert(test_list, s)
assert test_list.getAfter() == s
assert s.getBefore() == test_list

insert(s, j1)
assert test_list.getBefore() == j1
assert findFront(s) == j1

insert(s, j1)