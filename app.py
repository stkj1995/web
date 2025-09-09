from flask import Flask, render_template, request

from icecream import ic
ic.configureOutput(prefix=f'----- | ', includeContext=True)

import x 

app = Flask(__name__)

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


