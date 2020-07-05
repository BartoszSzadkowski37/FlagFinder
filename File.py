from pathlib import Path


class File:
    def __init__(self, path):
        self.path = Path(path)
        self.name = self.path.name



