def print_attributes(obj):
    for attr in obj.__dict__:
        print attr, getattr(obj, attr)

