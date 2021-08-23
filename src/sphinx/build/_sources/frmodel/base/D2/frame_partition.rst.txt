##################
Frame Partitioning
##################

``Frame2D`` provides a quick way to create windows

=======
View As
=======

There are a few methods to split the frames. This is the recommended way as splitting doesn't use memory referencing.

- ``view_windows``
- ``view_windows_as_frames``
- ``view_blocks``
- ``view_blocks_as_frames``

--------------------------------
Windows vs. Blocks vs. As Frames
--------------------------------

Windows can overlap, blocks cannot.

Note that the functions without ``as_frames`` returns a ``np.ndarray``.

===========
Module Info
===========

.. automodule:: frmodel.base.D2.frame._frame_partition
