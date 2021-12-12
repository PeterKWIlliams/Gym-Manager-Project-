from db.run_sql import run_sql

from models.booking import Booking
from models.member import Member
from models.gym_class import GymClass

import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository


def save(booking):
    sql = "INSERT INTO bookings (member_id,gym_class_id)"
