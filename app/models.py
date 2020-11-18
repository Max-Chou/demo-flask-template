from app.extensions import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128))


    def get_user_by_id():
        pass

    def get_user_by_username():
        pass

    def get_users():
        pass

    def create_user():
        pass

    def update_user():
        pass

    def delete_user():
        pass