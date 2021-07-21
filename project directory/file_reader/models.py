from ..app.app import db


class Cities(db.Model):
    __tablename__ = "cities"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __repr__(self):
        return self.name


def create_routes_tables(tablename: str):
    class Routes(db.Model):
        __tablename__ = tablename
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(15), unique=True)
        desc = db.Column(db.String(150))

        def __init__(self, id: int, name: str, desc: str):
            self.id = id
            self.name = name
            self.desc = desc

        def __repr__(self):
            return self.name

    return Routes


def to_json():
    pass
