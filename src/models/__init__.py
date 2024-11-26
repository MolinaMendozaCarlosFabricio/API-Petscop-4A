#from models import user
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .user_normally import UserNormally
from .repost import Repost
# from .comment import Comment
# from .commentPost import Response_post
# from .commentLocal import Response_local
# from .responseComment import Response_comment