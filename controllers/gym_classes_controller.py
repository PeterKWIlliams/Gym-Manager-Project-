from flask import Blueprint, Flask, redirect, render_template, request
from models.gym_class import GymClass

gym_classes_blueprint =Blueprint("gym_classes",__name__)

