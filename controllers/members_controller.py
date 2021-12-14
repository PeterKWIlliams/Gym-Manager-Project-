from flask import Blueprint, Flask, redirect, render_template, request
from models.member import Member 
import repositories.member_repository as member_repository


members_blueprint = Blueprint("members",__name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members)

@members_blueprint.route("/members/new")
def new_member():
    return render_template("members/new.html")

@members_blueprint.route("/members", methods =["POST"])
def create_member():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    date_of_birth = request.form["date_of_birth"]
    gender = request.form["gender"]
    notes = request.form["notes"]
    contact_info_email = request.form["contact_info_email"]
    contact_info_number = request.form["contact_info_number"]
    membership_type = request.form["membership_type"]

    member = Member(first_name, last_name, date_of_birth, gender, notes, contact_info_email, contact_info_number, membership_type)
    member_repository.save(member)
    return redirect("/members")

@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.select(id)
    return render_template("members/edit.html", member = member)

@members_blueprint.route("/members/<id>", methods = ["POST"])
def update_member(id):
    print(request.form)
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    date_of_birth = request.form["date_of_birth"]
    gender = request.form["gender"]
    notes = request.form["notes"]
    contact_info_email = request.form["contact_info_email"]
    contact_info_number = request.form["contact_info_number"]
    membership_type = request.form["membership_type"]

    member = Member(first_name, last_name, date_of_birth, gender, notes, contact_info_email, contact_info_number, membership_type, id)
    member_repository.update(member)
    return redirect("/members")

@members_blueprint.route("/members/<id>/delete", methods =["POST"])
def delete_member(id):
    
    member_repository.delete(id)
    return redirect("/members")






