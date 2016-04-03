# *-* encoding=utf-8 *-*

import unittest

from gpa.student import Exam


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


def main():
    unittest.main()


if __name__ == '__main__':
    main()
