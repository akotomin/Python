class FileAcceptor:
    def __init__(self, *extensions):
        self.extensions = set(extensions)

    def __call__(self, filename):
        ext = filename.split('.')[-1]
        return ext in self.extensions

    def __add__(self, other):
        new_extensions = self.extensions.union(other.extensions)
        return FileAcceptor(*new_extensions)
