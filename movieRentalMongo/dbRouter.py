class movieRentalMongoDBRouter(object):

    def db_for_read(self, model, **hints):
        from django.conf import settings
        if 'mongodb' not in settings.DATABASES:
            return None
        if model._meta.app_label == 'movieRentalMongo':
            return 'mongodb'
        return None

    def db_for_write(self, model, **hints):
        from django.conf import settings
        if 'mongodb' not in settings.DATABASES:
            return None
        if model._meta.app_label == 'movieRentalMongo':
            return 'mongodb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        from django.conf import settings
        if 'mongodb' not in settings.DATABASES:
            return None
        if obj1._meta.app_label == 'movieRentalMongo' or obj2._meta.app_label == 'movieRentalMongo':
            return True
        return None

    def allow_syncdb(self, db, model):
        from django.conf import settings
        if 'mongodb' not in settings.DATABASES:
            return None
        if db == 'mongodb':
            return model._meta.app_label == 'movieRentalMongo'
        elif model._meta.app_label == 'movieRentalMongo':
            return False
        return None