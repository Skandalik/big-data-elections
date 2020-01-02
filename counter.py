import os, printer


def create():
    return Counter()


class Counter:
    total = 0

    def scan(self, path: str):
        if os.path.isdir(path):
            for single_dir in os.listdir(path):
                self.scan('%s\\%s' % (path, single_dir))

        if not path.endswith('.bz2'):
            return

        printer.print("Scanned %s files." % self.total)
        self.total += 1

        return self

    def success(self):
        print("Successfully scanned %s files." % self.total)
