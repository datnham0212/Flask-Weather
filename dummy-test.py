from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/<user>")
def helloNonAdmin(user):
    return f"Hello {user}!"

@app.route("/admin")
def helloAdmin():
    return "Greetings, Admin!"

@app.route("/<name>")
def switch(name):
    if name == "admin" or name == "Admin":
        return redirect(url_for("helloAdmin"))
    else:    
        return redirect(url_for("helloNonAdmin", user = name)) 



if __name__ == "__main__":
    app.run()