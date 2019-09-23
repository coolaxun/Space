import datetime

from mongoengine.document import Document
from mongoengine.fields import IntField, StringField, DateTimeField


class Post(Document):
    # post_id = StringField(primary_key=True)
    title = StringField(max_length=200, required=True)
    body = StringField()
    create_time = DateTimeField(default=datetime.datetime.now)
    author_id = IntField(required=True)
    author_name = StringField(required=True)
    meta = {'db_alias': 'default'}
