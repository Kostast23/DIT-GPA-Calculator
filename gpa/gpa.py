# *-* encoding=utf-8 *-*

import getpass
import re
import requests
import sys

from adapter import TLSv1Adapter
from ects import ECTSRule
from student import StudentRecord


# Regular expression used to extract exams information from (html) text.
EXAM_REGEX = r"(?P<date>\d+),.*'(?P<code>\d+)'.*'(?P<name>.*)'.*'(?P<grade>\d+)'"


def read_exams_text(exams_text):
    """Extracts exams information from text and stores them in a StudentRecord
    instance that is returned.

    Args:
        grades_text (str): Text (html) that contains exams information.
    """
    record = StudentRecord()
    prog = re.compile(EXAM_REGEX)

    for line in exams_text.splitlines():
        match = prog.search(line)
        if match is not None:
            record.add_exam(match.group('code'), match.group('name'),
                            match.group('date'), match.group('grade'))
    return record


# Regular expression used to read ects information from text.
ECTS_REGEX = r'.* (?P<code>\d+) (?P<year>\d+) (?P<ects_before>\d+) (?P<ects_after>\d+)'


def read_ects_file(ects_file):
    """Reads ects information from a file and returns a map from course code to
    course ects information.

    Args:
        ects_file (str): Path of the input file.
    """
    ects_rules = dict()
    prog = re.compile(ECTS_REGEX)

    with open(ects_file, 'r') as f:
        for line in f.readlines():
            match = prog.search(line)
            if match is not None:
                rule = ECTSRule(match.group('year'), match.group('ects_before'),
                                match.group('ects_after'))
                ects_rules[match.group('code')] = rule
    return ects_rules


def calculate_gpa(student_record, ects_rules):
    """Calculates the GPA given a student exam history and the ects rules.

    Args:

    """
    grade_sum = .0
    ects_sum = 0

    for code, course in student_record.courses.items():
        exam = course.get_passed_exam()
        if exam is None:
            continue
        if code in ects_rules:
            rule = ects_rules[code]
            ects = rule.get_ects_at_date(exam.date)
            grade_sum += exam.grade * ects
            ects_sum += ects

    return grade_sum / ects_sum


if __name__ == '__main__':
    pass
