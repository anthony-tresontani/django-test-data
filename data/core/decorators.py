import inspect
from decorator import decorator

def get_maker_function(obj):
    list_fnc = []
    for attr in obj.__dict__:
        if inspect.ismethod(attr):
	    list_fnc.append(attr)
    return list_fnc


def with_data(maker):

    def inner(f):
        def _inner(f, self, *args, **kwargs):
  	    import pdb;pdb.set_trace()
	    maker_obj = maker()
            makers = get_maker_function(maker)
	    self.my_int = maker_obj.data()
            return f(self, *args, **kwargs)

        return decorator(_inner)(f)

    return inner
