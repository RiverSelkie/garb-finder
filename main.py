from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://garb-finder:garb-finder@localhost:8889/garb-finder'
<<<<<<< HEAD
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "Your_secret_string"

=======
app.config['SQLALCHEMY_ECHO'] = True 
app.config['SECRET_KEY'] = "Your_secret_string"
>>>>>>> bbc1385268388352940a65c7f8a834a14699ac5c
db = SQLAlchemy(app)

class User (db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    password = db.Column(db.String(120))
    #saved_item = db.relationship("Item", backref = "user")


    def __init__(self, username, password):
        self.username = username
        self.password = password
        

class Item (db.Model):
<<<<<<< HEAD

 #   saved_item = db.relationship("Item", backref = "user")
=======
    
>>>>>>> bbc1385268388352940a65c7f8a834a14699ac5c
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    culture = db.Column(db.String(120))
    climate = db.Column(db.String(120))
    gender = db.Column(db.String(120))
    item_type = db.Column(db.String(120))
    time_period_start = db.Column(db.Integer)
    time_period_end = db.Column(db.Integer)
    description = db.Column(db.String(2000))
<<<<<<< HEAD
 #   user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


=======
   # user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    
>>>>>>> bbc1385268388352940a65c7f8a834a14699ac5c
    def __init__(self, name, description, user):
        self.name = name
        self.description = description
        self.culture = culture
        self.climate = climate
        self.item_type = item_type
        self.gender = gender
        self.user = user

 
class Climate (db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, name):
        self.name


@app.route("/login", methods=['GET', 'POST'])
def login():
    incorrect_info=""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        incorrect_info=""
        q_user = User.query.filter_by(username=username).first()
        error_bool=False
        if q_user:
            if password != q_user.password:
                incorrect_info = "Incorrect username or password"
                error_bool=True
        else:
            incorrect_info = "Incorrect username or password"
            error_bool=True    
        if error_bool == False:
            session['user'] = username 
            return redirect('/home')
        else:
            return render_template("login.html", incorrect_info=incorrect_info)    
    return render_template("login.html")
    
@app.route('/logout')
def logout():
    if "user" in session:
        del session['user']
    return redirect('/blog')


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    mismatch=""
    bad_password=""
    bad_username=""
    other_username=""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        taken_username=User.query.filter_by(username=username).count()
        error_bool=False
        if verify != password:
            mismatch="These passwords do not match."
            error_bool=True
        if len(password) <3:
            bad_password="Please enter a password that is at least 3 characters long"
            error_bool=True
        if len(username) <3:
            bad_username="Please enter a username that is at least 3 characters long"    
            error_bool=True
        if taken_username > 0:
            other_username="This username has already been taken.  Please pick another one."
            error_bool=True
        if error_bool == False:  
            user = User(username, password)
            db.session.add(user)
            db.session.commit()
            session["user"] = username
            return redirect('/home')
        else:
            return render_template("signup.html", mismatch=mismatch, bad_password=bad_password, bad_username=bad_username, other_username=other_username)
    else: 
        return render_template("signup.html")

@app.route('/home')
def avocado():
  return render_template("home.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route("/welcome")
def welcome_in():
    username = request.args.get("username")  
    return render_template("welcome.html", username=username)

@app.route("/")
def default():
    return redirect("/home")
 
if __name__ == "__main__":
    app.run()
