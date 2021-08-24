###############
Getting Started
###############

The main class to use would be ``Frame2D``.

==========
Must Knows
==========

----------
Convention
----------

By convention, I name ``Frame2D`` instances as ``f``.

If you see ``f.CHN`` as a type-hint, it means to use ``Frame2D.CHN.XX`` constants.
These constants are simply ``str`` or ``Tuple[str]``

You can see the constants here :doc:`available_channels`.

----------------
Loading & Saving
----------------

``Frame2D`` can be saved and loaded as ``.npz``.

.. code-block:: python

    f = Frame2D.from_image("path/to/file.jpg")
    f.save("save.npz")
    f1 = Frame2D.load("save.npz")

========
Examples
========

----------------
Loading an Image
----------------

.. code-block:: python

    from frmodel.base.D2.frame2D import Frame2D

    frame = Frame2D.from_image("path/to/file.jpg")

Here, we get an RGB Image and load it as a ``Frame2D``.

---------------------
Retrieving np.ndarray
---------------------

The ``np.ndarray`` is store inside ``Frame2D`` via a ``.data`` property call.

.. code-block:: python

    from frmodel.base.D2.frame2D import Frame2D

    frame = Frame2D.from_image("path/to/file.jpg")
    ar = frame.data

-----------------------------
Calculating Non-GLCM Channels
-----------------------------

Syntax: ``f.get_chns(List[f.CHN, str])``

In ``0.1.0`` there is a new standard of channel calculation.

This is so that the calculation call does not return a new Frame, instead, just appends to the current Frame.

The following is how you get **Hue** from a **RGB** image.

.. code-block:: python

    from frmodel.base.D2.frame2D import Frame2D

    f = Frame2D.from_image("path/to/file.jpg")
    f.get_chns('HUE')
    ar = f[..., 'HUE'].data

In the above code, **Hue** is calculated, and retrieved as an ``np.ndarray``.

---------
Shorthand
---------

Syntax: ``f.XX()``

In the case where you want to retrieve a single channel, it's easy to do so.

*The call will also automatically call the respective calculations to retrieve it.*

.. code-block:: python

    from frmodel.base.D2.frame2D import Frame2D

    f = Frame2D.from_image("path/to/file.jpg")
    ar1 = f.HUE().data

    ar2 = f[..., 'HUE'].data

When you call ``HUE()``, internally, the **Hue** is calculated and appended to ``f`` as reference.

Thus ``f`` will have **Hue** as a channel.

=======================
Concurrent Calculations
=======================

Some channels **have** to be calculated together.

For example, when you retrieve **Hue**, the **Saturation** and **Value** will also be calculated together.

.. code-block:: python

    from frmodel.base.D2.frame2D import Frame2D

    f = Frame2D.from_image("path/to/file.jpg")
    f.get_chns('HUE')
    ar = f[..., 'SATURATION'].data

====
GLCM
====

Syntax: ``f.get_glcm(chns=List[f.CHN, str], radius=int, bins=int)``

GLCM is similar to ``get_chns``. Using ``get_glcm``.

.. code-block:: python

    from frmodel.base.D2.frame2D import Frame2D

    f = Frame2D.from_image("path/to/file.jpg")
    f.get_glcm(chns=['RED', 'BLUE'])
    ar = f.CON('RED').data

``get_glcm`` calculates its features, one of which is ``CON``, and we retrieve it using the ``.CON`` method.

---------------------
Shorthand & Full Call
---------------------

Syntax: ``f.FEATURE(List[f.CHN, str])``

You can retrieve the channel in both ways.

.. code-block:: python

    from frmodel.base.D2.frame2D import Frame2D

    f = Frame2D.from_image("path/to/file.jpg")
    f.get_glcm(chns=['RED', 'BLUE'])

    # Short Hand
    ar = f.CON(['RED', 'BLUE']).data
    # Full Call
    ar = f[..., ['CON_RED', 'CON_BLUE']]).data

Notice the Full Call is more verbose, but has a more extensible API.
