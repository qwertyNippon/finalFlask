from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from uuid import uuid4

db = SQLAlchemy()

# class Follow(db.model):
#     id = db.Column(db.Integer, primary_key=True)
#     followed_by_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     following_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# follows = db.Table(
#     'follows',
#     db.Column('followed_by_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
#     db.Column('following_id',db.Integer, db.ForeignKey('user.id'), nullable=False)
# )

# likes = db.Table(
#     'likes',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
#     db.Column('post_id', db.Integer, db.ForeignKey('post.id'), nullable=False)
# )


# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), nullable=False, unique=True)
#     email = db.Column(db.String, nullable=False, unique=True)
#     password = db.Column(db.String, nullable=False)
#     post = db.relationship('Post', backref='author', lazy=True)
#     Hopefully this helps understand the backref!!!
#     for a post:
#     p3 = Post()
#     p3.author
#     or user.post ====> [p321, p5464564, etc. . . ]

#     following = db.relationship('User',
#             primaryjoin = (follows.c.followed_by_id==id),
#             secondaryjoin = (follows.c.following_id==id),
#             secondary = follows,
#             backref = db.backref('follows', lazy = 'dynamic'),
#             lazy = 'dynamic'
#     )


#     def __init__(self,username, email, password):
#         self.username = username
#         self.email = email
#         self.password = generate_password_hash(password)

#     def save_user(self):
#         db.session.add(self)
#         db.session.commit()
 
#     # def follow(self, user):
#     #     self.following.append(user)
#     #     db.session.commit()
    
#     # def unfollow(self, user):
#     #     self.following.remove(user)
#     #     db.session.commit()

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String, nullable=False)
#     body = db.Column(db.String)
#     img_url = db.Column(db.String)
#     date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     liked = db.relationship('User',
#             secondary = 'likes',
#             backref = 'liked',
#             lazy = 'dynamic'
#                 )

#     def __init__(self, title, body, img_url, user_id):
#         self.title = title
#         self.body = body
#         self.img_url = img_url
#         self.user_id = user_id

#     def save_post(self):
#         db.session.add(self)
#         db.session.commit()

#     def save_changes(self):
#         db.session.commit()

#     def delete_post(self):
#         db.session.delete(self)
#         db.session.commit()

#     def like_post(self, user):
#         self.liked.append(user)
#         db.session.commit()

#     def unlike_post(self, user):
#         self.liked.remove(user)
#         db.session.commit()

#     def to_dict(self):
#         return {
#             'title': self.title,
#             'body': self.body,
#             'img' : self.img_url,
#             'date_created': self.date_created,
#             'user_id': self.user_id,
#             'author' : self.author.username
#         }
    
# class Movie(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String, nullable=False)
#     rating = db.Column(db.String)
#     img_url = db.Column(db.String)
#     price = db.Column(db.Numeric(8, 2))
#     genre = db.Column(db.String)
#     desc = db.Column(db.String)
#     length = db.Column(db.Integer)
#     trailer = db.Column(db.String)
#     date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

#     def __init__(self, title, rating, img_url, price, genre, desc, length, trailer):
#         self.title = title
#         self.rating = rating
#         self.img_url = img_url
#         self.price = price
#         self.genre = genre
#         self.desc = desc
#         self.length = length
#         self.trailer = trailer
    
#     def save_movie(self):
#         db.session.add(self)
#         db.session.commit()
    
#     def save_changes(self):
#         db.session.commit()

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'title': self.title,
#             'rating': self.rating,
#             'img_url': self.img_url,
#             'price':self.price, 
#             'genre':self.genre ,
#             'desc':self.desc ,
#             'length':self.length ,
#             'trailer':self.trailer,

#         }



    
# class Bikes(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String, nullable=False)
#     pic = db.Column(db.String)

#     def __init__(self, title, pic):
#         self.title = title
#         self.pic = pic

#     def save_me(self):
#         db.session.add(self)
#         db.session.commit()

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'title': self.title,
#             'pic' : self.pic
#         }
    

class Anime_models(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    new_url = db.Column(db.String)
    img = db.Column(db.String)
    trail = db.Column(db.String)
    engT = db.Column(db.String)
    japT = db.Column(db.String)
    rating = db.Column(db.String)
    syn = db.Column(db.String)
    watching = db.relationship('User',
        secondary = 'watch_list',
        backref = 'watch_list',
        lazy = 'dynamic'
        )
# creates a reference to user and can get accessed by watch_list

    def __init__(self, id, new_url, img, trail, engT, japT, rating, syn):
        self.id = id
        self.new_url = new_url
        self.img = img
        self.trail = trail
        self.engT = engT
        self.japT = japT
        self.rating = rating
        self.syn = syn

    def save_me(self):
        db.session.add(self)
        db.session.commit()

    def save_changes(self):
        db.session.commit()

    def delete_me(self):
        db.session.delete(self)
        db.session.commit()
        
    def to_dict(self):
        d = {}
        
        d['id'] = self.id 
        d['new_url'] = self.new_url 
        d['img'] = self.img 
        d['trail'] = self.trail 
        d['engT'] = self.engT 
        d['japT'] = self.japT 
        d['rating'] = self.rating 
        d['syn'] = self.syn 
        return d


watch_list = db.Table(
    'watch_list',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
    db.Column('anime_id', db.Integer, db.ForeignKey('anime_models.id'), nullable=False)
)
# connects tables, in this case watch_list to the user table.

def get_uuid():
    return uuid4().hex

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True, default=get_uuid)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)

    def __init__(self,username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def save_me(self):
        db.session.add(self)
        db.session.commit()

    def save_changes(self):
        db.session.commit()

    def delete_me(self):
        db.session.delete(self)
        db.session.commit()


# class Watch_list(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     new_url = db.Column(db.String)
#     img = db.Column(db.String)
#     trail = db.Column(db.String)
#     engT = db.Column(db.String)
#     japT = db.Column(db.String)
#     rating = db.Column(db.String)
#     syn = db.Column(db.String)

#     def __init__(self, id, new_url, img, trail, engT, japT, rating, syn):
#         self.id = id
#         self.new_url = new_url
#         self.img = img
#         self.trail = trail
#         self.engT = engT
#         self.japT = japT
#         self.rating = rating
#         self.syn = syn

#     def save_me(self):
#         db.session.add(self)
#         db.session.commit()

#     def save_changes(self):
#         db.session.commit()

#     def delete_me(self):
#         db.session.delete(self)
#         db.session.commit()