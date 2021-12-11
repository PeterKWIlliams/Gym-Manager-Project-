from flask import Blueprint, Flask, redirect, render_template, request
from models.booking import Booking

bookings_blueprint = Blueprint("bookings",__name__)