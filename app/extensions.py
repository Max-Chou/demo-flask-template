from flask_caching import Cache
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy


cache = Cache()
session = Session()
db = SQLAlchemy()
