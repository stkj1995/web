from flask import Flask, render_template, request

from icecream import ic
ic.configureOutput(prefix=f'----- | ', includeContext=True)

import x 

app = Flask(__name__)

########################
@app.get("/")
def view_index():
    pass

########################
@app.get("/signup")
def view_signup():
    pass

########################
@app.get("/home")
def view_home():
    pass

########################
@app.get("/explore")
def view_explore():
    pass

########################
@app.get("/notifications")
def view_notifications():
    pass

########################
@app.get("/messages")
def view_messages():
    pass

########################
@app.get("/bookmarks")
def view_bookmarks():
    pass

########################
@app.get("/list")
def view_list():
    pass

########################
@app.get("/profile")
def view_profile():
    pass

########################
@app.get("/more")
def view_more():
    pass


# GET       is to get HTML
# POST      used for saving data in the system
# PUT       is used to update all the row except the id
# PATCH     is used to update one or more cells
# DELETE    is used to delete a resource

########################
########################
########################

#A post gets data from the form
#The URL doesn't change
@app.post("/tweet")
def post_tweet():
    pass

########################
########################
########################

@app.post("/search")
def post_search():
    pass

########################
########################
########################

@app.delete("/")
def delete_like_tweet():
    pass

########################
########################
########################

@app.put("/profile")
def update_profile():
    pass



# main page
# friendly URL inspired on x.com
# http://127.0.0.1/cph

# @app.get("/<username>")
# def view_index(username):
#     db, cursor = x.db()
#     q = "SELECT * FROM users WHERE user_username = %s"
#     cursor.execute(q, (username,))
#     user = cursor.fetchone()
#     ic(user)
#     return render_template("index.html", user=user)
    

#######################################
# The url usually contains -
# 127.0.0.1/search?first-name
# In flask args is everything after the question mark
 
 
# @app.get("/search")
# def view_search():
#     name = request.args.get("first-name", "")
#     last_name = request.args.get("last-name", "")
#     year = request.args.get("year", "")
#     color = request.args.get("color", "")
#     return f"Hi {name} {last_name}, the year is {2025}. My favorite color is {color}"


    # Pass the name, last name and year
    # show this in the website:
    # Hi Sophie Teinvig, the year is 2025. My favorite color is xxxx


