# *-* encoding=utf-8 *-*


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
