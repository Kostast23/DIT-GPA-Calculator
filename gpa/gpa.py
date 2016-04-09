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


if __name__ == '__main__':
    pass
