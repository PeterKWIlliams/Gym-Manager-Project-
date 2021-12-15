from controllers.gym_classes_controller import gym_classes
from db.run_sql import run_sql 
from models.member import Member
from models.staff import Staff
from models.gym_class import GymClass
import repositories.staff_repository as staff_repository




def save(gym_class):
    sql = "INSERT INTO gym_classes (gym_class_name, duration, staff_id) VALUES (%s, %s, %s) RETURNING id"
    values = [gym_class.gym_class_name,gym_class.duration, gym_class.staff.id]
    results = run_sql(sql,values)
    id = results[0]["id"]
    gym_class.id = id 


def select_all():
    gym_classes = []
    sql = "SELECT * FROM gym_classes"
    results = run_sql(sql)
    for result in results:
        staff = staff_repository.select(result["staff_id"])
        gym_class = GymClass(result["gym_class_name"],result["duration"], staff, result["id"])
        gym_classes.append(gym_class)
    return gym_classes


def select(id):
    
    sql = "SELECT * FROM gym_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    staff = staff_repository.select(result["staff_id"])
    gym_class = GymClass(result["gym_class_name"],result["duration"],staff,result["id"])
    return gym_class


def delete_all():
    sql = "DELETE FROM gym_classes"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM gym_classes WHERE id = %s"
    values =[id]
    run_sql(sql,values)

def update(gym_class):
    sql = "UPDATE gym_classes SET (gym_class_name,duration,staff_id) =(%s,%s,%s) WHERE id = %s"
    values = [gym_class.gym_class_name, gym_class.duration, gym_class.staff.id, gym_class.id]
    run_sql(sql,values)

def select_members_in_class(id):
    members_in_class = []
    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE bookings.gym_class_id = %s"
    values = [id]
    results = run_sql(sql,values)
    for result in results:
        member = Member(result["first_name"],result["last_name"],result["date_of_birth"],result["gender"],result["notes"],result["contact_info_email"],result["contact_info_number"],result["membership_type"])
        members_in_class.append(member)
    return members_in_class