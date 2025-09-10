from flask import Flask, render_template, request, redirect, url_for, session
 
from icecream import ic
ic.configureOutput(prefix=f'----- | ', includeContext=True)
 
import x

 
app = Flask(__name__)

app.secret_key = "the secret"
 


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
    # user_first_name = session["user_first_name"]
    return render_template("home.html")
 
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
        db, cursor = x.db()
        q = "SELECT * FROM users WHERE user_email = %s AND user_password = %s"
        cursor.execute(q, (user_email, user_password))
        user = cursor.fetchone() # {user_pk:1, user_email:"", user_password:""....} We have this info from the database
        session["user_email"] = user["user_email"]
        session["user_first_name"] = user["user_first_name"]
        return render_template("home.html", user_first_name=user["user_first_name"])
    except:
        pass
    finally:
        pass


##############################
@app.get("/logout")
def logout():
    # session.pop["user_email"]
    # session.pop["user_first_name"]
    session.clear() # removes everything
    return redirect(url_for("view_index"))




 
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
        return redirect(url_for("view_index"))
    except Exception as ex:
        ic(ex) #see exception in the terminal
        return str(ex) # show in the browser
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()
 
 
 
 
 
 
##################################
##################################
##################################
# TRANSACTION
# begintransaction
# commit
# rollback


@app.get("/transaction")
def transaction():
    try:
        db, cursor = x.db()
        db.start_transaction()

        q = "UPDATE users SET user_password = %s WHERE user_pk = %s"
        cursor.execute(q, ("oneoneone", 1)) # the "one" will be shown as new password in the database

        q = "UPDATE users SET user_password = %s WHERE user_pk = %s"
        cursor.execute(q, ("twotwotwo", 2)) # the "two" will be shown as new password in the database
        db.commit()
        return "ok" # this will be shown in browser, if it works OK
    except Exception as ex: 
        # ex is just a variable and the exception is an object
        if "db" in locals(): db.rollback() # this makes the code save
        ic(ex)
        return str(ex) #this will be shown in browser, if it's wrong
    finally: 
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()



##################################
##################################
##################################
# Stored procedure

@app.get("/stored-procedure")
def stored_procedure():
    try:
        db, cursor = x.db()
        db.start_transaction()
        q = "CALL get_all_users()"
        cursor.execute(q)
        rows = cursor.fetchall()
        ic(rows)
        return "ok"
    except Exception as ex:
        ic(ex)
        if "db" in locals(): db.rollback()
        return str(ex)
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()
 
 
 
##################################
##################################
##################################
# Stored procedure

@app.get("/stored-procedure-get-user")
def stored_procedure_get_user():
    try:
        db, cursor = x.db()
        db.start_transaction()
        q = "CALL get_user(%s)"
        cursor.execute(q, (1,))
        row = cursor.fetchone()
        ic(row)
        return "ok"
    except Exception as ex:
        ic(ex)
        if "db" in locals(): db.rollback()
        return str(ex)
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
 
 
 
 