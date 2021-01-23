from django.contrib.auth.mixins import UserPassesTestMixin


class IsOwnerTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.object.user == self.request.user