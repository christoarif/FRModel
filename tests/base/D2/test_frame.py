import unittest


from frmodel.base.D2.frame2D import Frame2D
from frmodel.base.consts import CONSTS
from tests.base.D2.test_d2 import TestD2


class FrameTest(TestD2):

    def test_split_xy(self):
        # Split by both X and Y
        frames = self.frame.split_xy(by=self.window, method=Frame2D.SplitMethod.DROP)

        self.assertEqual((self.window, self.window, self.channels), frames[0][0].shape)

    def test_split(self):
        # Split by Y Axis only, horizontal slices
        frames = self.frame.split(by=self.window, method=Frame2D.SplitMethod.DROP, axis=CONSTS.AXIS.Y)

        self.assertEqual(self.window, frames[0].shape[0])

    def test_slide_xy(self):
        # Slide by both X and Y
        frames = self.frame.slide_xy(by=self.window, stride=self.window // 2)

        self.assertEqual((self.window, self.window, self.channels), frames[0][0].shape)

    def test_slide(self):
        # Slide by Y Axis only, horizontal slices
        frames = self.frame.slide(by=self.window, stride=self.window // 2, axis=CONSTS.AXIS.Y)

        self.assertEqual(self.window, frames[0].shape[0])


if __name__ == '__main__':
    unittest.main()
