from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from database import * 



app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"
product=query_all()

@app.route("/",methods=['GET', 'POST'])
def sign():
    if request.method == 'GET':
        return render_template('sign.html')
    else:
        email = request.form["email"]
        password = request.form["psw"]
        c=check(email,password)
        print(c)

        if c == True:
            return render_template("cukur.html")
        else:
            print("opps!try again")

            return render_template('sign.html')




@app.route("/signup", methods=['GET', 'POST'])
def rahaf():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form["psw"]

        save_to_database(firstname,lastname,email,password)        
        return render_template('cukur.html',
            f = firstname,
            l = lastname,
            e = email,
            p = password

            )

@app.route("/home")
def home():
	return render_template("cukur.html")

@app.route("/wallwritings")
def wallwritings():
	return render_template("wallwritings.html")


@app.route("/cast")
def cast():
	return render_template("cast.html")


@app.route("/shop")
def shop():
	products = query_all()
	return render_template("shop.html",products=products)


@app.route("/songs")
def songs():
	return render_template("songs.html")


@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/signup")
def signup():
	return render_template("signup.html")

@app.route("/season1")
def season1():
	return render_template("season1.html")

@app.route("/season2")
def season2():
	return render_template("season2.html")

@app.route("/season3")
def season3():
	return render_template("season3.html")

if __name__ == '__main__':
	app.run(debug=True) 