from flask import Blueprint, Flask, redirect, render_template, request
from models.gym_class import GymClass
from models.staff import Staff
import repositories.staff_repository as staff_repository
import repositories.gym_class_repository as gym_class_repository

gym_classes_blueprint =Blueprint("gym_classes",__name__)

@gym_classes_blueprint.route("/gym_classes")
def gym_classes():
    gym_classes = gym_class_repository.select_all
    return render_template("gym_classes/index.html", gym_classes=gym_classes)

@gym_classes_blueprint.route("/gym_classes/<id>")
def show_gym_class(id):
    members = gym_class_repository.select_members_in_class(id)
    gym_class = gym_class_repository.select(id)
    return render_template("gym_classes/show.html",members = members, gym_class = gym_class)

@gym_classes_blueprint.route("/gym_classes/new")
def new_gym_class():
    staff = staff_repository.select_all()
    return render_template("gym_classes/new.html",staff = staff)

@gym_classes_blueprint.route("/gym_classes",methods = ["POST"])
def create_gym_class():
    gym_class_name = request.form["gym_class_name"]
    duration = request.form["duration"]
    staff_id = request.form["staff_id"]
    staff = staff_repository.select(staff_id)
    new_gym_class = GymClass(gym_class_name,duration,staff)
    gym_class_repository.save(new_gym_class)
    return redirect("gym_classes")

@gym_classes_blueprint.route("/gym_classes/<id>/edit")
def edit_gym_class(id):
    gym_class = gym_class_repository.select(id)
    Staff = staff_repository.select_all()
    
    return render_template("gym_classes/edit.html",gym_class = gym_class,staff = Staff)

@gym_classes_blueprint.route("/gym_classes")
def update_gym_class(id):
    gym_class_name = request.form["gym_class_name"]
    duration = request.form["duration"]
    staff_id = request.form["staff_id"]
    staff = staff_repository.select(staff_id)
    gym_class = GymClass(gym_class_name,duration,staff,id)
    gym_class_repository.update(gym_class)
    return redirect("/gym_classes")

@gym_classes_blueprint.route("/gym_classes")
def delete_gym_class(id):
    gym_class_repository.delete(id)
    return redirect("gym_classes")







    




    

