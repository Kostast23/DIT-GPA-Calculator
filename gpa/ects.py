# *-* encoding=utf-8 *-*


class ECTSRule(object):
    """Defines the ECTS of a course before and after a date.

    Attributes:
        date (str): The date of the change in yyyymm format.
        ects_before (int): ECTS up to and until the change.
        ects_after (int): ECTS after the change.
    """
    def __init__(self, date, ects_before, ects_after):
        self.date = date
        self.ects_before = int(ects_before)
        self.ects_after = int(ects_after)

    def get_ects_at_date(self, date):
        """Given a date returns the ects τhat are valid at that date."""
        return self.ects_before if date <= self.date else self.ects_after
