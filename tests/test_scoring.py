import pytest
from enums import SCORING


@pytest.mark.parametrize(("points", "expected"),
                         [
                             (15, SCORING.Super),
                             (14, SCORING.Cool),
                             (12, SCORING.Cool),
                             (10, SCORING.Good),
                             (7, SCORING.Good),
                             (6, SCORING.Bad),
                             (4, SCORING.Bad),
                             (3, SCORING.Really_Bad),
                             (0, SCORING.Really_Bad),

                         ])
def test_are_scores_valid(system, points, expected):
    system.points = points
    assert system.get_scoring_from_points() == expected


def test_every_test_has_msg(system):
    assert set(system.ui.SCORING_MSG) == set(SCORING)
