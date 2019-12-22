from app import db

class Model(db.Model):

    def setAttribute(self, key, value):
        setattr(self, key, value)
        return self
