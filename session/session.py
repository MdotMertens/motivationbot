class Session(object):

    def __init__(self):
        self.stage = 0
        self.context = None

    def set_context(self, context: str):
        self.context = context
