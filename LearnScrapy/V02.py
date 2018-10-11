class student():
    name = "mark"
    age = 20
    city = "beijing"

    def get_message(self):
        print(self.name)

    @classmethod
    def get_messages(cls):
        print(cls.name)

    @staticmethod
    def get_messagess():
        print(student.age)
a = student()
print(a.name)
a.get_message()
a.get_messages()
student.get_messagess()