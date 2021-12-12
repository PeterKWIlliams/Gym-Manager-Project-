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
staff_repository.delete_all()
gym_class_repository.delete_all()
member_repository.delete_all()


staff1 = Staff("james","webb","PT")
staff_repository.save(staff1)





