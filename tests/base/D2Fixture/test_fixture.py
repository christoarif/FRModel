import os
import unittest

from frmodel.base.D2 import Frame2D
from tests.path import RSC_PATH

_DIR = os.path.dirname(os.path.realpath(__file__))
_RSC = _DIR + "/../../../rsc"
class TestD2Fixture(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.frame_box = Frame2D.from_image(RSC_PATH + f"imgs/rgb/basic/box.png")
        cls.frame = Frame2D.from_image(RSC_PATH + f"imgs/rgb/chestnut/test_0.jpg")
        cls.window = 100
        cls._RSC = _RSC
        cls.channels = 3


if __name__ == '__main__':
    unittest.main()
