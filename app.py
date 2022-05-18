from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)
@app.route("/robots.txt")
def robots_dot_txt():
    return "User-Agent: * \n Allow: / \n Disallow: /static"

@app.route('/')
@app.route('/index/')
@app.route('/home/')
def index():
   return render_template("index.html")

@app.route('/about/')
def about():
   return render_template("about.html")  

@app.route('/contact/')
def info():
   return render_template("contact.html")  

@app.route('/projects/')
def prj():
   return render_template("projects.html")  

@app.route('/credits/')
def credit():
   return render_template("credits.html")  

# i mean if you're trying to "login" into a static website
# you kinda deserve to be rickroll'd lol
@app.route('/test/')
@app.route('/admin/')
@app.route('/wp-login.php') #fuck you, especially, bots
@app.route('/adminLogin/')
def rick():
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
if __name__ == "__main__":
    app.run()
