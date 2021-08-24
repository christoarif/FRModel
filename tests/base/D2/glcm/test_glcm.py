import pytest

from frmodel.base.D2 import Frame2D
from tests.base.D2Fixture.test_fixture import fs as f, c


@pytest.fixture
def fg(f):
    f.get_glcm(chns=['RED', 'GREEN', 'BLUE'])
    return f

def test_get_glcm(fg, c):
    assert fg.shape[-1] == 5 + 5 * 3

def test_shorthand(fg, c):
    """ Shorthand allows the user to get by feature without having to
    repeat the prefix

    f['CON_RED', 'CON_BLUE'] == f.CON('RED', 'BLUE')

    """
    assert fg.CON('RED').shape[-1] == 1

    with pytest.raises(KeyError):
        fg.CON('RED_EDGE')
    with pytest.raises(KeyError):
        fg.CON('??')

    assert fg.CON(['RED', 'GREEN']).shape[-1] == 2

    with pytest.raises(KeyError):
        fg.CON(['RED', 'RED_EDGE'])
    with pytest.raises(KeyError):
        fg.CON(['??', 'RED'])

def test_shorthand_features(fg, c):
    """ Test the other features. """
    assert fg.CON('RED').shape[-1] == 1
    assert fg.COR('RED').shape[-1] == 1
    assert fg.ASM('RED').shape[-1] == 1
    assert fg.MEAN('RED').shape[-1] == 1
    assert fg.VAR('RED').shape[-1] == 1
