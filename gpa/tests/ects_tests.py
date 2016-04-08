# *-* encoding=utf-8 *-*

import unittest

from gpa.ects import ECTSRule


class ECTSRuleTests(unittest.TestCase):
    def setUp(self):
        self.date = '201602'
        self.ects_before = '6'
        self.ects_after = '8'
        self.rule = ECTSRule(self.date, self.ects_before, self.ects_after)

    def test_rule_initialization(self):
        self.assertEqual(self.rule.date, self.date)

        # ECTS value should be stored as int type.
        self.assertEqual(self.rule.ects_before, int(self.ects_before))
        self.assertEqual(self.rule.ects_after, int(self.ects_after))

    def test_ects_at_date_prior_to_change(self):
        before_date = '201509'
        self.assertLess(before_date, self.date)
        ects = self.rule.get_ects_at_date(before_date)
        self.assertEqual(ects, int(self.ects_before))

    def test_ects_at_date_of_change(self):
        ects = self.rule.get_ects_at_date(self.date)
        self.assertEqual(ects, int(self.ects_before))

    def test_ects_at_date_after_change(self):
        after_date = '201606'
        self.assertLess(self.date, after_date)
        ects = self.rule.get_ects_at_date(after_date)
        self.assertEqual(ects, int(self.ects_after))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
