"""
Ajay Shah, Jack Kjar, Shreyas Sao
CSE 163 A
Run the project's data cleaning and analysis scripts in order.
"""

import data_cleaning
import question2
import question3
import research_question_1
import test_q1
import test_q2
import test_q3


def main() -> None:
    """
    Run data cleaning followed by all research question analyses and tests.
    """
    data_cleaning.main()
    research_question_1.main()
    question2.main()
    question3.main()

    test_q1.main()
    test_q2.main()
    test_q3.main()


if __name__ == "__main__":
    main()
