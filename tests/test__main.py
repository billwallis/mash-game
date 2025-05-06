import random
import textwrap

from mash import main


def test__results_are_printed_as_expected(capsys):
    """
    Test the results are printed as expected.

    Note that this is a crappy test. It will be improved later.
    """

    random.seed(0)

    main.main()
    captured = capsys.readouterr()

    assert captured.out == textwrap.dedent(
        """\
               attire: Casual Clothes
                foods: Completely new food
               drinks: Soft Only
        entertainment: Home Games (video or board)
        """
    )
