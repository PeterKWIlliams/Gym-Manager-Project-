from flask import Flask,render_template


from controllers.members_controller import members_blueprint
from controllers.staff_controller import staff_blueprint
from controllers.bookings_controller import bookings_blueprint
from controllers.gym_classes_controller import gym_classes_blueprint

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(staff_blueprint)
app.register_blueprint(bookings_blueprint)
app.register_blueprint(gym_classes_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()