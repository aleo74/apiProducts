from app.db import db


class Product(db.Model):

    __tablename__ = "Products"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    inventoryStatus = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255))
    rating = db.Column(db.Float)

    def __init__(self, code, name, description, price, quantity, inventoryStatus, category, image, rating):
        self.code = code
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.inventoryStatus = inventoryStatus
        self.category = category
        self.image = image
        self.rating = rating

    def to_dict(self):
        return {
            'id': self.id,
            'code': self.code,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'quantity': self.quantity,
            'inventoryStatus': self.inventoryStatus,
            'category': self.category,
            'image': self.image,
            'rating': self.rating
        }

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
