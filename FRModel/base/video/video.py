from __future__ import annotations
import cv2
from typing import List
from FRModel.base.image.image import Image
from dataclasses import dataclass


@dataclass
class Video:
    """ This class holds the data as OpenCV2.VideoCapture.
    Extract the actual Capture with .vid property
    """

    vid: cv2.VideoCapture

    @staticmethod
    def from_video(file_path: str) -> Video:
        """ Creates an instance using the file path. """
        return Video(cv2.VideoCapture(file_path))

    def to_images(self,
                  offsets_msec: List[int] or int,
                  failure_default: None = None
                  ) -> List[Image]:
        """ Extracts images from the video.

        Returns FRModel.Image

        :param offsets_msec: The timestamps to extract images from.
        :param failure_default: Value to default to on failure on offset read.
        :returns: List[Image]
        """

        # Correct it as a List if int
        if isinstance(offsets_msec, int): offsets_msec = [offsets_msec]

        img_list = []
        for offset in offsets_msec:
            # Move to offset and attempt reading.
            self.vid.set(cv2.CAP_PROP_POS_MSEC, offset)
            success, image = self.vid.read()

            if success:
                # CV2 uses BGR, we swap the channels here
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                img_list.append(Image.from_array(image))
            else:
                img_list.append(failure_default)

        return img_list

    # OpenCV has a lot of issues detecting duration. This returns a negative value in a test, not reliable.
    # def duration(self) -> int:
    #     """ Gets the duration of the video """
    #     self.vid.set(cv2.CAP_PROP_POS_AVI_RATIO, 1)
    #     return self.vid.get(cv2.CAP_PROP_POS_MSEC)
