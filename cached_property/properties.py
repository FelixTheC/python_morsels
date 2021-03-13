EMPTY = object()


class cached_property:
    result = {}
    del_func = EMPTY

    def __init__(self, func, *args, **kwargs):
        self.func = func

    def __get__(self, instance=None, owner=None):
        if instance:
            if str(instance) not in self.result:
                self.result[str(instance)] = self.func(instance)
            return self.result[str(instance)]
        return self

    def __set__(self, instance, value):
        self.result[str(instance)] = value

    def __delete__(self, instance):
        if self.del_func is not EMPTY:
            self.del_func(instance)
            self.result[str(instance)] = self.func(instance)
            return self
        del self.result[str(instance)]

    def setter(self, func):
        # self.func = func
        return self

    def deleter(self, func):
        self.del_func = func
        return self
