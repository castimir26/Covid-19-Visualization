from django.apps import AppConfig


class SurvivedConfig(AppConfig):
    name = 'survived'

    def ready(self):
        from updater import updater
        updater.start()
