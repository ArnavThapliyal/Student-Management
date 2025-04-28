"""
Command-line interface for the Student Performance Tracker.
"""

import validation
import storage
from models import PerformanceTracker, Student
import visualization
import os

def run_cli():
    tracker = PerformanceTracker()

    # Load existing data from JSON or CSV
    students_data = storage.read_json()
    for data in students_data:
        student = Student(**data)
        tracker.add_student(student)

    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Show Statistics")
        print("6. Import CSV")
        print("7. Export CSV")
        print("8. Generate Plots")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            roll = input("Enter roll number: ")
            if not validation.validate_roll(roll):
                print("Invalid roll number format.")
                continue
            name = input("Enter name: ")
            email = input("Enter email: ")
            if not validation.validate_email(email):
                print("Invalid email format.")
                continue
            marks = {}
            while True:
                subject = input("Enter subject (or 'done' to finish): ")
                if subject.lower() == 'done':
                    break
                mark = float(input(f"Enter marks for {subject}: "))
                marks[subject] = mark
            student = Student(roll, name, email, marks)
            tracker.add_student(student)
            print("Student added successfully.")

        elif choice == '2':
            roll = input("Enter roll number of student to update: ")
            student = tracker.search_student(roll=roll)
            if student:
                print(f"Current data: {student}")
                name = input("Enter new name (leave blank to keep current): ")
                email = input("Enter new email (leave blank to keep current): ")
                if name:
                    student.name = name
                if email and validation.validate_email(email):
                    student.email = email
                else:
                    print("Invalid email format. Keeping current email.")
                while True:
                    subject = input("Enter subject to update marks (or 'done' to finish): ")
                    if subject.lower() == 'done':
                        break
                    mark = float(input(f"Enter new marks for {subject}: "))
                    student.marks[subject] = mark
                tracker.update_student(roll, student)
                print("Student updated successfully.")
            else:
                print("Student not found.")

        elif choice == '3':
            roll = input("Enter roll number of student to delete: ")
            tracker.delete_student(roll)
            print("Student deleted successfully.")

        elif choice == '4':
            roll = input("Enter roll number or name to search: ")
            student = tracker.search_student(roll=roll) or tracker.search_student(name=roll)
            if student:
                print(student)
            else:
                print("Student not found.")

        elif choice == '5':
            stats = tracker.compute_statistics()
            if stats:
                print(f"Highest: {stats['highest']}, Lowest: {stats['lowest']}, Average: {stats['average']:.2f}")
            else:
                print("No students available.")

        elif choice == '6':
            csv_file = input("Enter CSV file path to import: ")
            initial_data = storage.import_initial_data(csv_file)
            for data in initial_data:
                student = Student(**data)
                tracker.add_student(student)
            print("Data imported successfully.")

        elif choice == '7':
            csv_file = input("Enter CSV file path to export: ")
            df = storage.read_csv()
            if not df.empty:
                storage.write_csv(df)
                print("Data exported successfully.")
            else:
                print("No data to export.")

        elif choice == '8':
            if not os.path.exists('plots'):
                os.makedirs('plots')
            visualization.plot_marks_distribution(tracker.students)
            visualization.plot_average_scores(tracker.students)
            print("Plots generated successfully.")

        elif choice == '9':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")