from __future__ import annotations

from abc import ABC
from typing import List, TYPE_CHECKING

import numpy as np
from skimage.util import view_as_windows, view_as_blocks

from frmodel.base.consts import CONSTS

if TYPE_CHECKING:
    from frmodel.base.D2.frame2D import Frame2D

from warnings import warn


class _Frame2DPartition(ABC):

    def view_windows(self: 'Frame2D',
                     height: int,
                     width: int,
                     height_step: int,
                     width_step: int) -> np.ndarray:
        """ Partitions the image into windows using striding

        Note that the parameters must cleanly divide the image else it'll be cropped
        
        E.g. 200 x 200 cannot be 100 Step 3 x 100 Step 7

        The dims are [RowBlock, ColBlock, Row, Col, Channels]

        :param height: Height of expected window
        :param width: Width of expected window
        :param height_step: Step of height window
        :param width_step: Step of width window
        """

        view: np.ndarray =\
            view_as_windows(self.data,
                            (height, width, self.shape[-1]),
                            (height_step, width_step, 1)).squeeze(2)
        # [HW, WW, H, W, C]
        return view

    def view_windows_as_frames(self: 'Frame2D',
                               height: int,
                               width: int,
                               height_step: int,
                               width_step: int) -> List[List['Frame2D']]:
        """ Partitions the image into windows using striding

        Note that the parameters must cleanly divide the image else it'll be cropped

        E.g. 200 x 200 cannot be 100 Step 3 x 100 Step 7

        :param height: Height of expected window
        :param width: Width of expected window
        :param height_step: Step of height window
        :param width_step: Step of width window
        """
        view = self.view_windows(height, width, height_step, width_step)
        return [[self.create(view[h, w], self.labels)
                 for h in range(view.shape[0])] for w in range(view.shape[1])]

    def view_blocks(self: 'Frame2D',
                    height: int,
                    width: int) -> np.ndarray:
        """ Partitions the image into blocks using striding

        Note that the height and width must be a divisor.

        The dims are [RowBlock, ColBlock, Row, Col, Channels]

        :param height: Height of expected block, must be int divisor of original height
        :param width: Width of expected block, must be int divisor of original width
        """
        view: np.ndarray =\
            view_as_blocks(self.data,
                           (height, width, self.shape[-1])).squeeze(2)
        # [HW, WW, H, W, C]
        return view

    def view_blocks_as_frames(self: 'Frame2D',
                              height: int,
                              width: int) -> List[List['Frame2D']]:
        """ Partitions the image into blocks using striding

        Note that the height and width must be a divisor.

        :param height: Height of expected block, must be int divisor of original height
        :param width: Width of expected block, must be int divisor of original width
        """
        view = self.view_blocks(height, width)

        return [[self.create(view[h, w], self.labels)
                 for h in range(view.shape[0])] for w in range(view.shape[1])]
