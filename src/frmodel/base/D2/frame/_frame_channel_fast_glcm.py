from __future__ import annotations

from abc import ABC
from dataclasses import dataclass, field
from typing import Tuple, List, TYPE_CHECKING, Union, Iterable

import numpy as np

from frmodel.base import CONSTS
from frmodel.base.D2.frame._cy_fast_glcm2 import CyGLCM

if TYPE_CHECKING:
    from frmodel.base.D2.frame2D import Frame2D


class _Frame2DChannelFastGLCM(ABC):
    """ This re-implements Wang Jifei's Fast GLCM Script by adding the option of binarization. """

    def get_glcm(self: 'Frame2D',
                 chns: Iterable[Frame2D.CHN] = (),
                 radius: int = 2,
                 bins: int = 8):
        """ This will get the GLCM statistics for this window

        Details on how GLCM works is shown on the wiki.

        :param chns: Channels, can be also in strings.
        :param radius: Radius of GLCM Window
        :param bins: Bin size pre-processing of GLCM.
        """

        # FAST GLCM
        chns = chns if chns else list(self.labels.keys())
        data = CyGLCM(self[..., chns].data.astype(np.float32), radius, bins).create_glcm()
        data = data.swapaxes(-2, -1).reshape([*data.shape[:2], -1])

        labels = []

        labels.extend(CONSTS.CHN.GLCM.CON( list(self._util_flatten(chns))))
        labels.extend(CONSTS.CHN.GLCM.COR( list(self._util_flatten(chns))))
        labels.extend(CONSTS.CHN.GLCM.ASM( list(self._util_flatten(chns))))
        labels.extend(CONSTS.CHN.GLCM.MEAN(list(self._util_flatten(chns))))
        labels.extend(CONSTS.CHN.GLCM.VAR( list(self._util_flatten(chns))))

        self._data = self.crop_glcm(radius, glcm_by=1).data
        t = self.append(data, labels=labels)
        self._data = t.data
        self._labels = t.labels

        return self

    def CON(self, chns: Union[List[str], str]):
        return self[:, :, [f"CON_{i}" for i in chns] if isinstance(chns, List) else f"CON_{chns}"]

    def COR(self, chns: Union[List[str], str]):
        return self[:, :, [f"COR_{i}" for i in chns] if isinstance(chns, List) else f"COR_{chns}"]

    def ASM(self, chns: Union[List[str], str]):
        return self[:, :, [f"ASM_{i}" for i in chns] if isinstance(chns, List) else f"ASM_{chns}"]

    def MEAN(self, chns: Union[List[str], str]):
        return self[:, :, [f"MEAN_{i}" for i in chns] if isinstance(chns, List) else f"MEAN_{chns}"]

    def VAR(self, chns: Union[List[str], str]):
        return self[:, :, [f"VAR_{i}" for i in chns] if isinstance(chns, List) else f"VAR_{chns}"]

