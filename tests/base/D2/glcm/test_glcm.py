import pytest

from frmodel.base.D2 import Frame2D
from tests.base.D2Fixture.test_fixture import fs as f, c


# Arrange
@pytest.fixture
def fg(f):
    f.get_glcm(chns=['RED', 'GREEN', 'BLUE', 'RED_EDGE', 'NIR'])
    return f

def test_get_glcm(fg, c):
    """ Verify labels are correctly initialized"""
    assert fg.shape[-1] == 5 + 5 * 3

