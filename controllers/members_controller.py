from flask import Blueprint, Flask, redirect, render_template, request
from models.member import Member 

members_blueprint = Blueprint("members",__name__)