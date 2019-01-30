from datetime import datetime, timedelta

NOW = datetime.now()


class Promo:

    def __init__(self, name, expires):
        self.name = name
        self.expires = expires

    @property
    def expired(self):
        return self.expires < NOW
