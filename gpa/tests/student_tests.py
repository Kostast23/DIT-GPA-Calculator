# *-* encoding=utf-8 *-*

import unittest

from gpa.student import Course
from gpa.student import Exam
from gpa.student import StudentRecord


class ExamTests(unittest.TestCase):
    def setUp(self):
        self.exam = Exam('20130601', '5')       # date: 06/2013, grade: 5

    def test_str_exam_matches(self):
        self.assertEqual(str(self.exam), 'Βαθμολογία: 5.0   Εξεταστική Περίοδος: 2013, Εαρινή')

    def test_str_exam_fails_to_match_random_str(self):
        self.assertNotEqual(str(self.exam), 'Whatever')

    def test_str_exam_fails_to_match_empty_str(self):
        self.assertNotEqual(str(self.exam), '')

    def test_exam_less_than_operator_for_same_year_exams(self):
        later_period_exam = Exam('20130901', '4')       # date: 09/2013
        same_period_exam = Exam('20130601', '5')        # date: 06/2013
        earlier_period_exam = Exam('20130201', '5')     # date: 02/2013
        self.assertTrue(self.exam < later_period_exam)
        self.assertFalse(self.exam < same_period_exam)
        self.assertFalse(self.exam < earlier_period_exam)

    def test_exam_less_than_operator_for_different_year_exams(self):
        earlier_year_exam = Exam('20120601', '4')       # date: 06/2012
        later_year_exam = Exam('20150201', '5')     # date: 02/2015
        self.assertFalse(self.exam < earlier_year_exam)
        self.assertTrue(self.exam < later_year_exam)


class CourseTests(unittest.TestCase):
    def setUp(self):
        self.course = Course('CourseName')

    def test_course_name_matches(self):
        self.assertEqual(self.course.name, 'CourseName')

    def test_course_exams_list_is_empty(self):
        self.assertListEqual(self.course.exams, [])

    def test_adding_exam_to_course(self):
        exams = [Exam('20120201', '10')]
        self.course.add_exam(exams[0])
        self.assertItemsEqual(self.course.exams, exams)

    def test_grades_are_added_ordered_by_date(self):
        exam = Exam('20120201', '4')            # date: 02/2012
        later_exam = Exam('20120901', '9')      # date: 09/2012
        exams = [exam, later_exam]
        self.course.add_exam(later_exam)
        self.course.add_exam(exam)
        self.assertListEqual(self.course.exams, exams)


class StudentRecordTests(unittest.TestCase):
    def setUp(self):
        self.record = StudentRecord()

    def test_empty_record(self):
        # Record should not contain any courses.
        self.assertEqual(len(self.record.courses), 0)
        self.assertRaises(KeyError, lambda: self.record.courses['ABC'])
        self.assertRaises(KeyError, lambda: self.record.courses['DEF'])

    def test_adding_one_exam(self):
        self.record.add_exam('ABC', 'ABC_NAME', '20150202', '5')

        # Record should contain one course cause only one is being added.
        self.assertEqual(len(self.record.courses), 1)
        self.assertTrue(self.record.courses['ABC'])

    def test_adding_two_exams_of_different_courses(self):
        self.record.add_exam('ABC', 'ABC_NAME', '20150202', '5')
        self.record.add_exam('DEF', 'DEF_NAME', '20160202', '6')

        # Record should contain two courses cause two exams of different
        # courses are being added.
        self.assertEqual(len(self.record.courses), 2)
        self.assertTrue(self.record.courses['ABC'])
        self.assertTrue(self.record.courses['DEF'])

    def test_adding_two_exams_of_the_same_course(self):
        self.record.add_exam('ABC', 'ABC_NAME', '20150202', '5')
        self.record.add_exam('ABC', 'ABC_NAME', '20150602', '10')

        # Record should contain only one course cause the two exams that
        # are being added are of the same course
        self.assertEqual(len(self.record.courses), 1)
        self.assertTrue(self.record.courses['ABC'])


def main():
    unittest.main()


if __name__ == '__main__':
    main()
