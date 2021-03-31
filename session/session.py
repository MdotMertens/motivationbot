import attr

from messagehandler.models.Challenge import Challenge

@attr.s
class Session(object):

    stage = attr.ib()
    context = attr.ib(default=None)
    challenge = attr.ib(default=None)
