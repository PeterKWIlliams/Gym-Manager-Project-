import unittest
from models.member import Member
class TestMemeber(unittest.TestCase):
    def setUp(self):
        Member("jack","black","28.02.1998","Male","Hey there guys","jackblack@gmail.com","12345678910","standard")

    