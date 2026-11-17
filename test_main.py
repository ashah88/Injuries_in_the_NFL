"""
Ajay Shah, Jack Kjar, Shreyas Sao
CSE 163 A
Tests the projects analysis scripts
"""

import data_cleaning
import test_q1
import test_q2
import test_q3


def main() -> None:
    """
    Run data cleaning followed by all analysis script tests.
    """
    data_cleaning.main()
    test_q1.main()
    test_q2.main()
    test_q3.main()


if __name__ == "__main__":
    main()
