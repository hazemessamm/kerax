__name__ = "__init__"
__package__='kerax'
if __name__ == '__init__' and __package__ == "":
    from os import sys, path
    # __file__ should be defined in this case
    PARENT_DIR = path.dirname(path.dirname(path.abspath(__file__)))
    sys.path.append(PARENT_DIR)


