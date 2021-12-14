from flask import Blueprint, Flask, redirect, render_template, request
from models.booking import Booking

import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository

bookings_blueprint = Blueprint("bookings",__name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template('bookings/index.html', bookings = bookings)


@bookings_blueprint.route("/bookings/new")
def new_booking(id):
    members =  member_repository.select_all()
    gym_classes = gym_class_repository.select_all()
    return render_template("bookings/new.html",members = members,gym_classes = gym_classes)

@bookings_blueprint.route("/bookings", methods =["POST"])
def create_booking():
    member_id = request.form["member_id"]
    gym_class_id = request.form["gym_class_id"]
    member = member_repository.select(member_id)
    gym_class = gym_class_repository.select(gym_class_id)

    new_booking = Booking(member,gym_class)
    booking_repository.save(new_booking)
    return redirect("/bookings")

@bookings_blueprint.route("/bookings/<id>",methods = ["POST"])
def update_booking(id):
    member_id = request.form["member_id"]
    gym_class_id = request.form["gym_class_id"]
    member = member_repository.select(member_id)
    gym_class = gym_class_repository.select(gym_class_id)
    booking = Booking(member,gym_class)
    booking_repository.update(booking)
    return redirect ("/bookings")

@bookings_blueprint.route("/bookings/<id>/delete",methods =["POST"])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")

    
    
  


