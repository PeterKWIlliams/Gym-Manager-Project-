from db.run_sql import run_sql
from models.staff import Staff


def save(staff):
    sql = "INSERT INTO staff (first_name,last_name,job_title) VALUES (%s, %s, %s) RETURNING id "
    values = [staff.first_name,staff.last_name,staff.job_title]
    results = run_sql(sql,values)
    id = results[0]['id']
    staff.id = id 

def select_all():
    all_staff = []
    sql = "SELECT * FROM staff"
    results =run_sql(sql)
    for result in results:
        staff = Staff(result["first_name"],result["last_name"],result["job_title"],result["id"])
        all_staff.append(staff)
    return all_staff

def select(id):
    sql = "SELECT * FROM staff where id = %s"
    values = [id]