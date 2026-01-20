"""
    客户类
"""
import re
class Customer:
    def __init__(self, c_id, name, age="None",phone="None",email="None"):
        self.c_id = c_id
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Id: {self.c_id:<15},Name: {self.name:<15},Age: {self.age:<15},Phone: {self.phone:<15},Email: {self.email:<15}"

    @staticmethod
    def check_id(c_id):
        return c_id.isdigit()

    @staticmethod
    def check_name(name):
        return name.isalpha()

    @staticmethod
    def check_age(age):
        return age.isdigit()

    @staticmethod
    def check_phone(phone):
        pattern = r"^1[3456789]\d{9}$"
        return True if re.match(pattern, phone) else False

    @staticmethod
    def check_email(email):
        pattern = r"[\w!#$%&'*+-/=?^`{|}~.]+@[\w!#$%&'*+-/=?^`{|}~.]+\.[a-zA-Z]{2,}$"
        return True if re.match(pattern, email) else False

