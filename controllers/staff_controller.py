from flask import Blueprint, Flask, redirect, render_template, request
from models.staff import Staff 

import repositories.staff_repository as staff_repository

staff_blueprint = Blueprint("staff",__name__)

@staff_blueprint.route("/staff")
def staff():
    staff = staff_repository.select_all()
    return render_template("staff/index.html", staff=staff)

@staff_blueprint.route("/staff/new")
def new_staff():
    return render_template("staff/new.html")

@staff_blueprint.route("/staff", methods=["POST"])
def create_staff():
    print(request.data)
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    job_title = request.form["job_title"]
    new_staff = Staff(first_name, last_name, job_title)
    staff_repository.save(new_staff)
    return redirect("/staff")

@staff_blueprint.route("/staff/<id>/edit")
def edit_staff(id):
    staff = staff_repository.select(id)
    return render_template("staff/edit.html", staff=staff)

@staff_blueprint.route("/staff")
def update_staff(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    job_title = request.form["job_title"]
    staff = Staff(first_name,last_name, job_title, id)
    staff_repository.update(staff)


@staff_blueprint.route("/staff")
def delete_staff(id):
    staff_repository.delete(id)
    return redirect("/staff")






  




