import pytest
from enums import SCORING


@pytest.mark.parametrize(("points", "expected"),
                         [
                             (15, SCORING.Super),
                             (14, SCORING.Cool),
                             (12, SCORING.Cool),
                             (10, SCORING.Good),
                             (7, SCORING.Good),
                             (6, SCORING.Cool),
                             (4, SCORING.Bad),
                             (3, SCORING.Really_Bad),
                             (0, SCORING.Really_Bad),

                         ])
def test_are_scores_valid(points, expected):
    system.po
