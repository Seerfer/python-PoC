from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Cities(db.Model):
    __tablename__ = "cities"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"City: {self.id}"

    def serialize(self):
        return {"id": self.id, "name": self.name}


def create_routes_tables(tablename: str):
    class Routes(db.Model):
        __tablename__ = tablename
        id = db.Column(db.String(3), primary_key=True)
        name = db.Column(db.String(15), unique=True)
        desc = db.Column(db.Text)

        def __init__(self, id: str, name: str, desc: str):
            self.id = id
            self.name = name
            self.desc = desc

        def __repr__(self):
            return f"Route: {self.id}"

        def serialize(self):
            return {"id": self.id, "name": self.name, "desc": self.desc}

    return Routes


def get_class_by_tablename(tablename: str):
    for c in db.Model._decl_class_registry.values():
        if hasattr(c, "__tablename__") and c.__tablename__ == tablename:
            return c
