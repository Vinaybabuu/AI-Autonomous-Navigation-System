class Agent:
    def __init__(self, start):
        self.position = start

    def move(self, path):
        if path:
            self.position = path.pop(0)