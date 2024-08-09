class MarkdownProcessor:

    def __init__(self):
        self.data = None
        self.chunks = []

    def load(self, filename):
        with open(filename, 'r') as f:
            data = f.read()
        self.chunks = data.split("\n\n")
        self.data = data
