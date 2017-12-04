from flask import Flask, request, render_template, redirect
import os
import re
 
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("template.html")

@app.route("/", methods=["POST"])
def sign_up():
    username= request.form['username']
    password= request.form['password']
    verify_password= request.form['verify_password']
    email= request.form['email'] 
    user_error= ""
    pass_error= ""
    email_error = ""


    if username == "":
        user_error = ("Please enter username") 
        
    elif len(username) < 3:
        user_error = ("Username needs to be longer")

    if password == "":
        pass_error = ("Please enter password")
        
    elif password != verify_password:
        pass_error = ("Password does not match")
    
    if email != "" and len(email) < 3 and len(email) > 20:
        email_error = ("Email not valid") 

    if user_error == "" and pass_error == "" and email_error == "":
        return redirect("/welcome?username={}".format(username))
    
    #if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
     #   email_error = ("Email not valid")

    

    
    return render_template("template.html", username=username, email=email, user_error=user_error, pass_error=pass_error, email_error=email_error)
    

@app.route("/welcome")
def welcome():
    username = request.args['username'] 
    return render_template("welcome.html", username=username)


app.run()