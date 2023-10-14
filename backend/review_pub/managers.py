from django.db.models import Manager


class DomainManager(Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class LanguageManager(Manager):
    def get_by_natural_key(self, code):
        return self.get(code=code)