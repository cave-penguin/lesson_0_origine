import inspect
import sys


class InspectObject:
    def __init__(self, obj):

        self.obj = obj

    def get_type(self):
        return type(self.obj).__name__

    def get_attributes(self):
        return [attr for attr in dir(self.obj) if not callable(getattr(self.obj, attr))]

    def get_methods(self):
        return [
            method for method in dir(self.obj) if callable(getattr(self.obj, method))
        ]

    def get_module_name(self):
        if inspect.getmodule(self.obj):
            return inspect.getmodule(self.obj).__name__
        else:
            return self.obj.__class__.__module__

    def get_size(self):
        return sys.getsizeof(self.obj)

    def get_docs(self):
        if self.obj.__doc__:
            return self.obj.__doc__
        else:
            return "This object does not have a docstring"


def introspection_info(obj):
    object = InspectObject(obj)

    return {
        "type": object.get_type(),
        "attributes": object.get_attributes(),
        "methods": object.get_methods(),
        "module": object.get_module_name(),
        "size": object.get_size(),
        "docs": object.get_docs(),
    }


number_info = introspection_info(42)
print(number_info)
