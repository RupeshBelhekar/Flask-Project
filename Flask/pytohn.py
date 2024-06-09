from flaskblog import db
from flaskblog.models import Post
import json

file = open('D:/Flask/flaskblog/static/posts.json')
data = json.load(file)

for x in data:
     post = Post(title = x.get('title'), content = x.get('content'), user_id = x.get('user_id'))
     db.session.add(post)

db.session.commit()