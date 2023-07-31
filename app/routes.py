from app import app
from .myfunc import Anime
from flask import render_template, Flask, request, jsonify, session
from .models import User, Anime_models
from flask_login import current_user, login_required, logout_user
from flask_bcrypt import Bcrypt
from flask_session import Session

bcrypt = Bcrypt(app)
server_session = Session(app)

# @app.route('/')
# def land():
#     user_list = User.query.all()
#     follow_set = set()

#     if current_user.is_authenticated:
#         users_following = current_user.following.all()
#         for u in users_following:
#             follow_set.add(u.id)
#         for x in user_list:
#             if x.id in follow_set:
#                 x.flag = True
    
#     print(user_list, '\n', follow_set)
        
        

#     return render_template('index.html', u_list=user_list)


# @app.route('/Login')
# @login_required
# def explore():
#     user = 
#     product.add_it(current_user)
#     return redirect(url_for('/Explore'))
# @app.route('/Login')
# def login():
#     return {}
# @app.route('/Signup')
# def signUp():
#     return {}
# @app.route('/Subscribe')
# def subscribe():
#     return {}
# @app.route('/Myanime')
# def myAnime():
#     return {} 

@app.route("/@me")
def get_current_user():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error" : "Security Clearance Needed"}), 401

    user = User.query.filter_by(id=user_id).first()
    return jsonify({
    "id" : user.id,
    "email" : user.email
})

@app.route('/add-anime')
# @login_required
def qwertyadd_product():
    k = 0
    j = 0
    for i in range(101,150):
    ### increment count of chosen product in cart
        anime = Anime(i)
        data = anime.request()
        # print(len(data))
        j+=1
        if len(data) < 4:
            d = anime.get_deets()
            id = anime.id
            new_url = anime.new_url
            img = anime.img
            trail = anime.trail
            engT = anime.engT
            japT = anime.japT
            rating = anime.rating
            syn = anime.syn
            a = Anime_models(id, new_url, img, trail, engT, japT, rating, syn)
            print(a.id, a.new_url, a.img, a.trail, a.engT, a.japT, a.rating, a.syn)
            k+=1
            print(k)
            print(j, 'this is how many anime')
            a.save_me()
        else:
            print('sorry')
            print(j, 'this is how many anime')
    return 'yes, yes, yes'

@app.route('/Signup', methods=["POST"])
# @login_required
def qwertyadd_user():
    # a = User(username, email, password)
    email = request.json['email']
    password = request.json['password']
    user_exists = User.query.filter_by(email=email).first() is not None
    
    if user_exists:
        return jsonify ({
            "error" : "User already exists"
        }), 409
    hashed_password = bcrypt.generate_password_hash(password)
    new_user = User(email=email, password=hashed_password)
    new_user.save_me

    return jsonify({
        "id" : new_user.id,
        "email" : new_user.email
    })

@app.route('/Login', methods=["POST"])
def qwertylogin_user():
    email = request.json['email']
    password = request.json['password']

    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({"error" : "Security Clearance Needed"}), 401

    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error" : "Security Clearance Needed"}), 401
    
    session["user_id"] = user.id

    return jsonify({
        "id" : user.id,
        "email" : user.email
    })


# @app.route('/WatchList')
# # @login_required
# def qwertyadd_list():
#     anime = Anime()
#     data = anime.request()
#     a = Watch_list(id, new_url, img, trail, engT, japT, rating, syn)
#     d = anime.get_deets()
#     id = anime.id
#     new_url = anime.new_url
#     img = anime.img
#     trail = anime.trail
#     engT = anime.engT
#     japT = anime.japT
#     rating = anime.rating
#     syn = anime.syn
#     a.save_me
#     return 'added, wish'