from db.run_sql import run_sql

from models.booking import Booking
from models.member import Member
from models.gym_class import GymClass

import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository


def save(booking):
    sql = "INSERT INTO bookings (member_id,gym_class_id) VALUES (%s,%s) RETURNING id "
    values = [booking.member.id,booking.gym_class.id]
    results = run_sql(sql,values)
    id = results[0]['id']
    booking.id = id 

def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for result in results:
        member = member_repository.select(result["member_id"])
        gym_class = gym_class_repository.select(result["gym_class_id"])
        booking = Booking(member,gym_class,result["id"])
        bookings.append(booking)
        return booking 

def select(id):
    sql = "SELECT FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)
    member = member_repository.select(result["member_id"])
    gym_class = gym_class_repository.select(result["gym_class_id"])
    booking = Booking(member,gym_class,result["id"])
    return booking 

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def update(booking):
    sql = "UPDATE bookings SET (member_id,gym_class_id) = (%s,%s) WHERE id = %s"
    values = [booking.member.id,booking.gym_class.id,booking.id]
    run_sql(sql,values)