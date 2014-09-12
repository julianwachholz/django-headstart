from django.contrib import messages


class UserFormKwargsMixin(object):
    """
    Set the user of a form automatically with this mixin.
    You probably want to use this together with KwargsPopMixin.

    """
    def get_form(self, *args, **kwargs):
        kwargs.update({'user': self.request.user})
        return super(UserFormKwargsMixin, self).get_form(*args, **kwargs)


class SuccessMessageMixin(object):
    """
    Add a success message on form_valid.
    Requires ``django.contrib.messages`` in your INSTALLED_APPS.

    """
    success_message = None
    message_level = messages.SUCCESS

    def get_success_message(self):
        if self.success_message is not None:
            return self.success_message
        raise NotImplementedError('Define {}.success_message or get_success_message().'.format(self.__class__.__name__))

    def form_valid(self, form):
        success_message = self.get_success_message()
        if success_message:
            messages.add_message(self.request, self.message_level, success_message)
        return super(SuccessMessageMixin, self).form_valid(form)
