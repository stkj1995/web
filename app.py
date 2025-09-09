from flask import Flask, render_template, request
 
from icecream import ic
ic.configureOutput(prefix=f'----- | ', includeContext=True)
 
import x

 
app = Flask(__name__)
 
##############################
@app.get("/")
def view_index():
    try:
        return render_template("view_login.html")
    except:
        # wrong
        pass
    finally:
        # happens after the try or except
        pass
 
##############################
@app.get("/signup")
def view_signup():
    try:
       return render_template("signup.html")
    except:
        pass
    finally:
        pass


##############################
@app.get("/home")
def view_home():
    pass
 
##############################
@app.get("/explore")
def view_explore():
    pass
 
##############################
@app.get("/notifications")
def view_notifications():
    pass
 
##############################
@app.get("/messages")
def view_messages():
    pass
 
##############################
@app.get("/bookmarks")
def view_bookmarks():
    pass
 
##############################
@app.get("/lists")
def view_lists():
    pass
 
##############################
@app.get("/profile")
def view_profile():
    pass
 
##############################
@app.get("/more")
def view_more():
    pass
 
##############################
##############################
##############################
# A post gets data from the form
# The URL doesn't change
@app.post("/tweet")
def post_tweet():
    pass
 
 
##############################
@app.post("/search")
def post_search():
    pass
 
##############################
@app.post("/login")
def post_login():
    try:
        user_email = request.form.get("user_email", "")
        user_password = request.form.get("user_password", "")
        return f"{user_email} {user_password}"
    except:
        pass
    finally:
        pass
 
##############################
##############################
##############################
 
@app.delete("/like-tweet")
def delete_like_tweet():
    pass
 
##############################
##############################
##############################
 
@app.put("/profile")
def update_profile():
    pass
 
 
 
 
 
 
# GET       is to get HTML
# POST      used for saving data in the system
# PUT       used to update all the row except the id
# PATCH     used to update one or more cells
# DELETE    used to delete a resource
 


 
 ##############################

@app.post("/signup")
def post_signup():
    try:
        user_email = request.form.get("user_email", "")
        user_password = request.form.get("user_password", "")
        hashed_password = x.hash_password(user_password)
        db, cursor = x.db()
        # INSERT INTO users VALUES(NULL, "@b", "secret")
        q = 'INSERT INTO users VALUES(NULL, %s, %s)'
        # In Python you have tuples. If there is only
        # 1 argument, you must have a comma at the end
        # If there are 2 or more comments 
        cursor.execute(q, (user_email, hashed_password))
        db.commit()
        return f"{user_email} {hashed_password}"
   
    except Exception as ex:
        ic(ex) #see exception in the terminal
        return str(ex) # show in the browser
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"""
@app.get("/<username>")
def view_index(username):
    db, cursor = x.db()
    q = "SELECT * FROM users WHERE user_username = %s"
    cursor.execute(q, (username,))
    user = cursor.fetchone()
    ic(user)
    return render_template("index.html", user=user)
"""
 
 
 
 
 
 
 
 
 
 
 
 
 
##############################
# The url usually contains -
# 127.0.0.1/search?first-name=a
# in flask args is everything after the question mark
"""
@app.get("/search")
def view_search():
    name = request.args.get("first-name", "")  
    last_name = request.args.get("last-name", "")
    year = request.args.get("year", "")  
    color = request.args.get("color", "")
    return f"Hi {name} {last_name}, the year is {year}. My favorite color is {color}"
"""
    # Pass the name, last name and year
    # show this in the website:
    # Hi Santiago Donoso, the year is 2025. My favorite color is xxxxx
 
 
 
 