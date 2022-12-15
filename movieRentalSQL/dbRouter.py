class movieRentalSQLDBRouter(object):

    def db_for_read(self, model, **hints):
        from django.conf import settings
        if 'default' not in settings.DATABASES:
            return None
        if model._meta.app_label == 'movieRentalSQL':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        from django.conf import settings
        if 'default' not in settings.DATABASES:
            return None
        if model._meta.app_label == 'movieRentalSQL':
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        from django.conf import settings
        if 'default' not in settings.DATABASES:
            return None
        if obj1._meta.app_label == 'movieRentalSQL' or obj2._meta.app_label == 'movieRentalSQL':
            return True
        return None

    def allow_syncdb(self, db, model):
        from django.conf import settings
        if 'default' not in settings.DATABASES:
            return None
        if db == 'default':
            return model._meta.app_label == 'movieRentalSQL'
        elif model._meta.app_label == 'movieRentalSQL':
            return False
        return None