class Developer:
    def __init__(self, surname, position, salary) -> None:
        self.surname = surname
        self.position = position
        self.salary = salary

class SoftwareEngineer(Developer):
    def __init__(self, surname, position, salary, bonus, department) -> None:
        super().__init__(surname, position, salary)
        self.bonus = bonus
        self.department = department

developer = [
    SoftwareEngineer("Anvar","Junior", 500, 100 ,"1-bolim"),
    SoftwareEngineer("Asror","Middle", 1500, 500 ,"2-bo'lim"),
    SoftwareEngineer("Kamola"," Senior", 2500, -100 ,"3-bo'lim"),
    SoftwareEngineer("Vali","Junior", 500, -100 ,"1-bolim"),
    SoftwareEngineer("Davron","Middle", 1500, 100 ,"2-bolim"),
    SoftwareEngineer("Bahodir","Senior", 2500, -100 ,"3-bo'lim"),
    SoftwareEngineer("Farrux"," Junior", 500, 100 ,"1-bo'lim"),
    SoftwareEngineer("Jamila","Middle", 1500, 200 ,"2-bo'lim"),
    SoftwareEngineer("Jasur ","Senior", 2500, 500 ,"3-bolim"),
    SoftwareEngineer("Komila"," Junior", 500, -100 ,"1-bo'lim")
]


d1 = 0
d2 = 0
d3 = 0
for x in developer:
    if '1' in x.department:
        d1 += x.salary + x.bonus
    elif '2' in x.department:
        d2 += x.salary + x.bonus
    elif '3' in x.department:
        d3 += x.salary + x.bonus
     

print(f"""
    1-bo`lim: {d1}
    2-bo`lim: {d2}
    3-bo`lim: {d3}""")

