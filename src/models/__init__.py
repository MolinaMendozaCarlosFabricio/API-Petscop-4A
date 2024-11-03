#from models import user
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .repost import Repost
from .comment import Comment
from .commentPost import Response_post
from .commentLocal import Response_local
from .commentService import Response_service
from .responseComment import Response_comment