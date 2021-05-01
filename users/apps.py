from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        # by django documentation - import the signals 
        import users.signals
