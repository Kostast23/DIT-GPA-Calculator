# *-* encoding=utf-8 *-*

import bisect


class Exam(object):
    """A student's Exam date and grade.

    Exam is held in a certain exam period (month and year).
    The exact day of the examination is redundant.

    Attributes:
        date (str): Exam date in yyyymm format, e.g. 201506.
        grade (float): Student's grade.
        exam_periods (dict): Maps months to exam periods.
    """

    exam_periods = {'02': 'Χειμερινή', '06': 'Εαρινή', '09': 'Επαναληπτική'}

    def __init__(self, date, grade):
        """
        Args:
            date (str): Exam date in yyyymmdd format, e.g. 20150601.
            grade (str): Student's grade (try to store as float).
        """
        self.date = date[:6]  # keep only the year and the month
        try:
            self.grade = float(grade)
        except ValueError:
            self.grade = .0

    def __str__(self):
        """Returns a human readable form of the exam grade and date."""
        year = self.date[:4]
        month = self.date[4:6]
        return 'Βαθμολογία: {:4s}  Εξεταστική Περίοδος: {:s}, {:s}'.format(
               unicode(self.grade).encode('utf-8'),
               unicode(year).encode('utf-8'),
               self.exam_periods[month])

    def __lt__(self, other):
        """Returns true if the exam was held earlier than the other exam."""
        return self.date < other.date


class Course(object):
    """Information about the course and the student's exam history in it.

    Attributes:
        name (str): The course's name.
        exams (list): List of Exams instances sorted from old to new.
    """

    passing_grade = 5

    def __init__(self, name):
        self.name = name
        self.exams = []

    def add_exam(self, exam):
        """Adds the exam to the list respecting Exam ordering."""
        bisect.insort_left(self.exams, exam)

    def get_passed_exam(self):
        """In case there is an exam with passing grade return it."""
        if len(self.exams) != 0 and self.exams[-1].grade >= self.passing_grade:
            return self.exams[-1]
        else:
            return None


class StudentRecord(object):
    """Records a student's grades in their courses.
    
    Attributes:
        courses (dict): Maps course codes to Course class instances.
    """

    def __init__(self):
        self.courses = dict()

    def add_exam(self, code, name, date, grade):
        """Creates an Exam instance and adds it to the right course history.

        Args:
            code (str): Course code.
            name (str): Course name.
            date (str): Date of the exam in yyyymmdd format.
            grade (str): Exam grade.
        """
        exam = Exam(date, grade)

        # If there is no record for a course, create one
        if code not in self.courses:
            self.courses[code] = Course(name)
        self.courses[code].add_exam(exam)

    def empty(self):
        """Returns true if there are no courses"""
        return len(self.courses) == 0
