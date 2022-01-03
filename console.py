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

staff2= Staff("Lovely","Star","PT")
staff_repository.save(staff2)

staff3 = Staff("Tyler","harvey","PT")
staff_repository.save(staff3)


member1 = Member("John","Malkovich","28.02.1998","Male","Sprained knee 2 weeks ago","JohnMalkovich@gmail.com","12345078","premium")
member_repository.save(member1)

member2 = Member("Billie","Triellish","26.02.1998","Female","","BillieTriellish@gmail.com","12345698","premium")
member_repository.save(member2)


member3 = Member("Jamie","Rotten","27.02.1998","Female","referred friend julie","johnnyRotten@gmail.com","12345678","standard")
member_repository.save(member3)


gym_class1 = GymClass("pilates",50,staff1) 
gym_class_repository.save(gym_class1)

gym_class3= GymClass("Zumba",60,staff3) 
gym_class_repository.save(gym_class3)

gym_class2 = GymClass("pilates",30,staff2) 
gym_class_repository.save(gym_class2)

booking1 = Booking(member1,gym_class1)
booking_repository.save(booking1)

booking2 =Booking(member2,gym_class2)
booking_repository.save(booking2)
