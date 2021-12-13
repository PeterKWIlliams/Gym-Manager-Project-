import pdb 

from models.booking import Booking 
import repositories.booking_repository as booking_repository

from models.gym_class import GymClass 
import repositories.gym_class_repository as gym_class_repository

from models.member import Member
import repositories.member_repository as member_repository

from models.staff import Staff 
import repositories.staff_repository as staff_repository


booking_repository.delete_all()
gym_class_repository.delete_all()
staff_repository.delete_all()
member_repository.delete_all()


staff1 = Staff("James","Webb","PT")
staff_repository.save(staff1)

member1 = Member("John","Malkovich","28.02.1998","Male","hello","JohnMalkovich@gmail.com","12345678","premium")
member_repository.save(member1)

gym_class1 = GymClass("pilates",50,staff1) 
gym_class_repository.save(gym_class1)

booking1 = Booking(member1,gym_class1)
booking_repository.save(booking1)













