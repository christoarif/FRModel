#############
Frame Channel
#############

*Channel2D Class is deprecated from 0.0.3 onwards, replaced by the current in-built methods*

================
Getting Channels
================

**>= 0.1.0**

There is a new convention of getting channels.

View some examples here: :doc:`../../../info/getting_started`

The new format, uses the following calling template

.. code-block:: python

    f: Frame2D
    f.get_chns(chns:List[CHN])

For example

.. code-block:: python

    f: Frame2D
    f.get_chns([f.CHN.HSV, f.CHN.EX_G, f.CHN.VEG])

The ``CHN`` argument can be grabbed from ``Frame2D`` class or any instance, or ``from consts import CONSTS``, though
the latter method is not recommended as it's verbose.

These ``CHN`` are actually strings, hence it's perfectly valid to call as

.. code-block:: python

    f: Frame2D
    f.get_chns(self_=True, chns=['H', 'S']) # Other arguments omitted

However, it's not recommended as it's prone to capitalization errors and typos.


Note that ``get_all_chns`` and ``get_chns`` gets all channels above.

The difference between those 2 is that, with ``get_all_chns`` you exclude channels you don't need,
depending on your choices, one may be more succinct than the other.

=======
Slicing
=======
*New in 0.0.6*

You can now slice like NumPy for the dimensions
.. code-block:: python

    f: Frame2D
    f[..., f.CHN.RED]
    f[0:100, 200:300, f.CHN.RGB]

==============
Retriving GLCM
==============

For GLCM, you need to specify its texture and the channel

.. code-block:: python

    f: Frame2D
    f[..., f.CHN.GLCM.COR(f.CHN.RED)]

========
Formulas
========

Below, we list all formulas that are used to calculate each index.

R: Red Wide, G: Green Wide, B: Blue Wide.

r: Red Narrow, g: Green Narrow, b: Blue Narrow, e: Red Edge, n: Near Infared

====
GLCM
====

GLCM is detailed in the :doc:`GLCM Implementation Page <frame_channel_glcm>`.

==
XY
==

The XY coordinate for every Pixel

===
HSV
===

HSV (Hue, Saturation, Value)

====
EX_G
====

Excess Green, defined as

.. math::

    2G - 1R - 1B

=====
MEX_G
=====

Modified Excess Green, defined as

.. math::

    1.262G - 0.884R - 0.331B

=====
EX_GR
=====

Excess Green Minus Red, defined as

.. math::

    3G - 2.4R - B

===
NDI
===

Normalized Difference Index, defined as

.. math::

    \frac{G - R}{G + R}

===
VEG
===

Vegetative Index, defined as

.. math::

    \frac{G}{R^{a} * B^{1-a}}

====
NDVI
====

Normalized Difference Vegetation Index

.. math::
    \frac{n - r}{n + r}

=====
BNDVI
=====

Blue Normalized Difference Vegetation Index

.. math::
    \frac{n - b}{n + b}

=====
GNDVI
=====

Green Normalized Difference Vegetation Index

.. math::
    \frac{n - g}{n + g}

====
GARI
====

Green Atmospherically Resistant Vegetation Index

.. math::
    \frac{n - g + b - r}{n - g - b + r}

===
GLI
===

Green Leaf Index

.. math::
    \frac{2 * g - r - b}{2 * g + r + b}

======
GBNDVI
======

Green Blue Normalized Difference Vegetation Index

.. math::
    \frac{n - b}{n + b}

======
GRNDVI
======

Green Red Normalized Difference Vegetation Index

.. math::
    \frac{n - g}{n + g}

====
NDRE
====

Normalized Difference Red Edge

.. math::
    \frac{n - e}{n + e}

===
LCI
===

Leaf Chlorophyll Index

.. math::
    \frac{n - e}{n + r}

=====
MSAVI
=====

Modified Soil Adjusted Vegetation Index

.. math::
    X = (2n + 1) \\
    (X - \sqrt{X^2 - 8 (n - r)}) / 2

=====
OSAVI
=====

Optimized Soil Adjusted Vegetation Index

.. math::
    \frac{n - r}{n + r + 0.16}

===========
Module Info
===========

.. automodule:: frmodel.base.D2.frame._frame_channel