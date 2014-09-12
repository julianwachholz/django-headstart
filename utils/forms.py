
class KwargsPopMixin(object):
    """
    Pop a given set of keyword arguments off the __init__ call
    and store them on the instance for later use.

    You might want to use this together with either of the classes below.

    """
    pop_kwargs = ('user',)

    def __init__(self, *args, **kwargs):
        if self.pop_kwargs is None:
            # TODO Maybe only raise a warning.
            raise ValueError('KwargsPopFormMixin.pop_kwargs needs to be set.')

        if isinstance(self.pop_kwargs, str):
            self.pop_kwargs = (self.pop_kwargs,)

        for kwarg in self.pop_kwargs:
            setattr(self, kwarg, kwargs.pop(kwarg))
        super(KwargsPopMixin, self).__init__(*args, **kwargs)


class SaveKwargsPopMixin(object):
    """
    Standard modelform save() behaviour with the addition of
    setting the previously popped kwargs after instance creation.

    """
    def save(self, commit=True):
        obj = super(SaveKwargsPopMixin, self).save(commit=False)
        for kwarg in self.pop_kwargs:
            setattr(obj, kwarg, getattr(self, kwarg))
        if commit:
            obj.save()
        return obj


class ManagerKwargsMixin(object):
    """
    Modelform mixin that overwrites the save method
    to actually use the model's manager.

    """
    def save(self, commit=True):
        if not commit:
            raise ValueError('Cannot call ManagerKwargsMixin.save with commit=False.')

        kwargs = self.cleaned_data
        for kwarg in self.pop_kwargs:
            kwargs[kwarg] = getattr(self, kwarg)
        return self._meta.model.objects.create(**kwargs)
