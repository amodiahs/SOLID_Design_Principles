# Dependency Inversion Principle
# a). High level module should not depend on low level modules. Both should depend on abstractions
# b). Abstractions should not depend on details. Details should depend on abstractions
'''
We are directly using team_student_memberships.team_memberships In our high level class Analysis and we are using the implementation 
of this list directly in high level class. As of now this is fine but imagine a situation in which we need to change this 
implementation from list to something else. In that case our high-level class Analysis would break as it is dependent on 
implementation details of Low level class TeamMemberships.
'''

from enum import Enum
from abc import ABCMeta, abstractmethod

class Teams(Enum):
  BLUE_TEAM = 1
  RED_TEAM = 2
  GREEN_TEAM = 3

class Student:
  def __init__(self, name):
    self.name = name

class TeamMemberships():
  def __init__(self):
    self.team_memberships = []

  def add_team_memberships(self, student, team):
    self.team_memberships.append((student, team))

class Analysis():
  def __init__(self, team_student_memberships):
    memberships = team_student_memberships.team_memberships
    for members in memberships:
      if members[1] == Teams.RED_TEAM:
        print(f'{members[0].name} is in RED team')

student1 = Student('Ravi')
student2 = Student('Archie')
student3 = Student('James')

team_memberships = TeamMemberships()
team_memberships.add_team_memberships(student1, Teams.BLUE_TEAM)
team_memberships.add_team_memberships(student2, Teams.RED_TEAM)
team_memberships.add_team_memberships(student3, Teams.GREEN_TEAM)

Analysis(team_memberships)