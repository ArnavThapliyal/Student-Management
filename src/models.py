"""
Data models for the Student Performance Tracker.
"""

from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Student:
    roll_number: str
    name: str
    email: str
    marks: Dict[str, float]

class PerformanceTracker:
    def __init__(self):
        self.students: List[Student] = []

    def add_student(self, student: Student):
        self.students.append(student)

    def update_student(self, roll_number: str, updated_student: Student):
        for i, student in enumerate(self.students):
            if student.roll_number == roll_number:
                self.students[i] = updated_student
                return True
        return False

    def delete_student(self, roll_number: str):
        self.students = [s for s in self.students if s.roll_number != roll_number]

    def search_student(self, roll_number: str = None, name: str = None):
        for student in self.students:
            if (roll_number and student.roll_number == roll_number) or \
               (name and student.name.lower() == name.lower()):
                return student
        return None

    def compute_statistics(self):
        if not self.students:
            return None
        total_marks = [sum(student.marks.values()) for student in self.students]
        return {
            'highest': max(total_marks),
            'lowest': min(total_marks),
            'average': sum(total_marks) / len(total_marks)
        }
