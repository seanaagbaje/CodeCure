from flask import render_template
from flask import current_app as app

def register_routes(app):
    @app.route("/")
    def home_route():
        return render_template("home.html")