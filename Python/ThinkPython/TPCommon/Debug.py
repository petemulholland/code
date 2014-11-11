def print_attributes(obj):
    for attr in obj.__dict__:
        print attr, getattr(obj, attr)

def find_defining_class(obj, meth_name): 
    for ty in type(obj).mro(): 
        if meth_name in ty.__dict__: 
            return ty

