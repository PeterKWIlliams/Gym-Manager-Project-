from flask import Blueprint, Flask, redirect, render_template, request
from models.staff import Staff 

staff_blueprint = Blueprint("staff",__name__)