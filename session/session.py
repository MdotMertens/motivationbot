class Session(object):

    def __init__(self, stage=0):
        self.stage = stage      
        self.context = None

    def set_context(self, context: str):
        self.context = context
