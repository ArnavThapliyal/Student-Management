 
"""
Visualization functions for student performance data.
"""

import matplotlib.pyplot as plt
import pandas as pd
import os

PLOTS_DIR = 'plots'

def plot_marks_distribution(students):
    """Create a histogram of overall marks distribution."""
    total_marks = [sum(student.marks.values()) for student in students]
    plt.hist(total_marks, bins=10, alpha=0.7, color='blue')
    plt.title('Marks Distribution')
    plt.xlabel('Total Marks')
    plt.ylabel('Number of Students')
    plt.grid(True)
    plt.savefig(os.path.join(PLOTS_DIR, 'marks_distribution.png'))
    plt.close()

def plot_average_scores(students):
    """Create a bar chart of each student’s average score."""
    names = [student.name for student in students]
    averages = [sum(student.marks.values()) / len(student.marks) for student in students]
    plt.bar(names, averages, color='green')
    plt.title('Average Scores of Students')
    plt.xlabel('Students')
    plt.ylabel('Average Score')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, 'average_scores.png'))
    plt.close()

def plot_top_performers(students, dates):
    """Create a time-series line chart of top performers over multiple exam dates."""
    # Assuming dates and scores are provided in a suitable format
    top_performers = sorted(students, key=lambda s: sum(s.marks.values()), reverse=True)[:5]
    for student in top_performers:
        plt.plot(dates, [sum(student.marks.values())] * len(dates), label=student.name)
    plt.title('Top Performers Over Time')
    plt.xlabel('Exam Dates')
    plt.ylabel('Total Marks')
    plt.legend()
    plt.savefig(os.path.join(PLOTS_DIR, 'top_performers.png'))
    plt.close()