class MongoDBRouter(object):
    """
    Determine how to route database calls for an app's models (in this case, for an app named Example).
    All other models will be routed to the next router in the DATABASE_ROUTERS setting if applicable,
    or otherwise to the default database.
    """

    def db_for_read(self, model, **hints):
        """Send all read operations on Example app models to `example_db`."""
        if model._meta.app_label == 'mongoDBwork':
            return 'mongo'
        return None

    def db_for_write(self, model, **hints):
        """Send all write operations on Example app models to `example_db`."""
        if model._meta.app_label == 'mongoDBwork':
            return 'mongo'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Determine if relationship is allowed between two objects."""
        if obj1._meta.app_label == 'auth' or obj2._meta.app_label == 'auth':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that the Example app's models get created on the right database."""
        if app_label == 'mongoDBwork':
            # The Example app should be migrated only on the example_db database.
            return db == 'mongo'
        elif db == 'mongo':
            # Ensure that all other apps don't get migrated on the example_db database.
            return False

        # No opinion for all other scenarios
        return None