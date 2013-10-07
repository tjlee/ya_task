import pyhash

class CustomDictionary(dict):
    def __init__(self, *arg, **kw):
        super(CustomDictionary, self).__init__(*arg, **kw)

    def __eq__(self, other):
        return super.__eq__(other)

    def __hash__(self):
        hasher = pyhash.super_fast_hash()
        return hasher(self)




