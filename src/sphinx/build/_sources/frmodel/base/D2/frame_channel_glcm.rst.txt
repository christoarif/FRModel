#####################################
Frame Gray Level Co-occurrence Matrix
#####################################

**>= 0.1.0 deprecates the GLCM class to support** ``get_glcm`` **as a separate call.**

============
GLCM Getting
============

**>= 0.1.0**

There is a new convention of getting channels, including GLCM.

View some GLCM examples here: :doc:`../../../info/getting_started`

GLCM is similar to ``get_chns``. Using ``get_glcm``.

.. code-block:: python

    from frmodel.base.D2.frame2D import Frame2D

    f = Frame2D.from_image("path/to/file.jpg")
    f.get_glcm(chns=['RED', 'BLUE'])
    ar = f.CON('RED').data

=======
Binning
=======

*New in 0.0.6*

Using the argument ``bins`` in the GLCM Class, data is binned before being processed.
This makes GLCM extremely fast.

It is recommended to bin to small values such as 4, 8, 16.

=======
Example
=======

``<=0.1.0`` code

.. code-block:: python

    glcm = f.GLCM(by=1, radius=2, verbose=True, bins=8
                  channel=[f.CHN.RGB])

    frame = f.get_chns(glcm=glcm)

``<=0.1.0`` code

.. code-block:: python

    g.get_glcm(chns=f.CHN.RGB, radius=2, bins=8)

Assuming f is a ``Frame2D``.

- This grabs the GLCM features for all RGB Channels.
- The GLCM is offset by 1 x 1. (`default for >=0.1.0`)
- The Neighbour Convolution radius is 2.
- The function will output its progress with a progress bar.

.. code-block::

    GLCM Progress: 100% 20/20 [00:01<00:00, 14.91it/s]

Each increment is a GLCM direction calculated for a channel.

=========
Algorithm
=========

The algorithm information has been redacted to avoid versioning issues with the research journal. An explanation of how
it works can be found in the research journal.

It references this tutorial `GLCM Texture: A Tutorial v. 3.0 March 2017 <https://prism.ucalgary.ca/handle/1880/51900>`_

===========
Module Info
===========

.. automodule:: frmodel.base.D2.frame._frame_channel_fast_glcm