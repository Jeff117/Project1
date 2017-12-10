from flask import *
import os
from database import *
from user import User


class App(Flask):
    def __init__(self):
        Flask.__init__(self, "animal_shelter", static_url_path="/static")
        self.__user = None
        self.__dir = os.path.dirname(os.getcwd())
        self.add_url_rule("/static/<path:filename>", view_func=self.serve_static, methods=["GET"])
        self.add_url_rule("/_login", view_func=self.__login, methods=["POST"])
        self.add_url_rule("/_logout", view_func=self.__log_out, methods=["GET", "POST"])
        self.add_url_rule("/login", view_func=self.view_login, methods=["GET"])
        self.add_url_rule("/", view_func=self.view_index, methods=["GET"])
        self.add_url_rule("/report", view_func=self.view_report, methods=["GET"])
        self.add_url_rule("/shelter", view_func=self.view_shelter,  methods=["GET"])
        self.add_url_rule("/find", view_func=self.view_find, methods=["GET"])

    def serve_static(self, filename):
        return send_from_directory(os.path.join(self.__dir, "static", filename))

    def __login(self):
        username = request.form["username"]
        password = request.form["password"]
        user_id = Database.valid(username, password)
        if user_id is None:
            return "User not found!"
        self.__user = User(user_id, username, password) 
        return redirect("/")

    def __log_out(self):
        self.__user = None
        return redirect("/")

    def view_login(self):
        return render_template("login.html", title="Login")

    def view_index(self):
        if self.__user is None:
            return redirect("/login")
        return render_template("index.html", title="Animal Shelter", active_home=True)

    def view_report(self):
        if self.__user is None:
            return redirect("/login")
        return render_template("report.html", title="Report a lost friend ", active_report=True)

    def view_shelter(self):
        if self.__user is None:
            return redirect("/login")
        return render_template("shelter_page.html", title="Marina Animal Shelter", active_shelter=True)

    def view_find(self):
        if self.__user is None:
            return redirect("/login")
        return render_template("search.html", title="Adopt a new buddy!", active_search=True)


if __name__ == "__main__":
    app = App()
    app.run(port=80)
