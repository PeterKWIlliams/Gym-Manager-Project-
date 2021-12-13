from flask import Blueprint, Flask, redirect, render_template, request
from models.gym_class import GymClass
import repositories.staff_repository as staff_repository
import repositories.gym_class_repository as gym_class_repository

gym_classes_blueprint =Blueprint("gym_classes",__name__)

@gym_classes_blueprint.route("/gym_classes")
def gym_classes():
    gym_classes = gym_class_repository.select_all
    return render_template("gym_classes/index.html", gym_classes =  gym_classes)

@gym_classes_blueprint.route("/gym_classes/<id>")
def show_gym_class(id):
    members = gym_class_repository.select_members_in_class(id)
    gym_class = gym_class_repository.select(id)
    return render_template("gym_classes/show.html")

@gym_classes_blueprint.route("/gym_classes/new")
def new_gym_class():
    staff = staff_repository.select_all()
    return render_template("gym_classes/new.html")
    




    

