from db.run_sql import run_sql
from models.member import Member

def save(member):
    sql = "INSERT INTO members(first_name,last_name,date_of_birth,gender,notes,contact_info_email,contact_info_number,membership_type) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id"
    
    values =[member.first_name,member.last_name,member.date_of_birth,member.gender,member.notes,member.contact_info_email,member.contact_info_number,member.membership_type]
    
    results = run_sql(sql,values)
    
    id = results[0]["id"]
    
    member.id = id 


def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for result in results:
        member = Member(result["first_name"],result["last_name"],result["date_of_birth"],result["gender"],result["notes"],result["contact_info_email"],result["contact_info_number"],result["membership_type"],result["id"])
        members.append(member)
    return members

def select(id):
    sql = "SELECT * FROM members WHERE id = %s"
    values =[id]
    result = run_sql(sql,values)[0]
    member = Member(result["first_name"],result["last_name"],result["date_of_birth"],result["gender"],result["notes"],result["contact_info_email"],result["contact_info_number"],result["membership_type"],result["id"])
    return member


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def update(member):
    sql = "UPDATE members SET(first_name, last_name, date_of_birth, gender, notes, contact_info_email, contact_info_number, membership_type) = (%s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s "
    values = [member.first_name, member.last_name, member.date_of_birth, member.gender, member.notes, member.contact_info_email, member.contact_info_number, member.membership_type, member.id]
    run_sql(sql, values)


    
