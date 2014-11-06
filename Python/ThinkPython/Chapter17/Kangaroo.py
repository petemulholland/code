class Kangaroo(object):
    """description of class"""

    def __init__(self):
        self.pouch_contents = []

    def put_in_pouch(self, contents):
        self.pouch_contents.append(contents)

    def __str__(self):
        return str(self.pouch_contents)


def ex_17_7():
    kanga = Kangaroo()
    roo = Kangaroo()
    kanga.put_in_pouch(roo)

    print kanga, roo



if __name__ == '__main__':
    ex_17_7()



