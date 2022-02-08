from composition import o
class Functor:
    def __init__(self, functor: object, function: object):
        self.F = functor
        self.f = function
    def __call__(self, object):
        return self.F(object)
    def Fof(self, object):
        return o([self.F, self.f])(object)
