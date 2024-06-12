from abc import ABC

class Character:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name


class Job:
    def __init__(self, job_type, wage):
        self._job_type = job_type
        self._wage = wage

    @property
    def job_type(self):
        return self._job_type
    @job_type.setter
    def job_type(self, job_type):
        self._job_type = job_type

    @property
    def wage(self):
        return self._wage
    @wage.setter
    def wage(self, wage):
        self._wage = wage


class Joe(Character, Job):
    def __init__(self, name, job_type, wage, age):
        Character.__init__(self, name)
        Job.__init__(self, job_type, wage)
        self._age = age

    @property
    def age(self):
        return self._age

    def __str__(self):
        return f"Joe(Name: {self.name}, Job: {self.job_type}, Wage: {self.wage}, Age: {self.age})"

    
# Exemple d'utilisation
joe = Joe(name="Joe", job_type="Developer", wage=50000, age=30)
print(joe)
