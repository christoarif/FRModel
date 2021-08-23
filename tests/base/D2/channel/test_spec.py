import pytest

from tests.base.D2Fixture.test_fixture import fs as f, c


def test_labels(f, c):
    """ Verify labels are correctly initialized"""
    assert 0 == f.labels[c.RED]
    assert 1 == f.labels[c.GREEN]
    assert 2 == f.labels[c.BLUE]
    assert 3 == f.labels[c.RED_EDGE]
    assert 4 == f.labels[c.NIR]

def test_get_present(f, c):
    """ Gets the channels that is already present. Synonymous with data_chn """
    assert 0 == f[..., c.RED]     .labels[c.RED]
    assert 0 == f[..., c.GREEN]   .labels[c.GREEN]
    assert 0 == f[..., c.BLUE]    .labels[c.BLUE]
    assert 0 == f[..., c.RED_EDGE].labels[c.RED_EDGE]
    assert 0 == f[..., c.NIR]     .labels[c.NIR]

def test_get_calculate(f, c):
    """ Calculates channels that are absent """
    g = f.get_chns(self_=False, chns=[c.NDVI])  # This should give us the HSV Channels only

    assert 0 == g[..., c.NDVI].labels[c.NDVI]

    # NIR isn't present anymore due to self_=False
    with pytest.raises(KeyError):
        _ = g[..., c.NIR]

def test_shape(f, c):
    """ Tests the data shape and orientation """
    assert (f.height(), f.width(), len(f.labels)) == f.shape

def test_all_chns(f, c):
    """ This tests getting the channel by property.

    Note that if you get a channel that isn't calculated yet, it will automatically
    calculate that and append it to itself.

    This is done this way because it's not time-intensive and it's convenient in programming.

    """
    assert f.RED().shape[-1]        == 1; assert f.shape[-1] == 5
    assert f.GREEN().shape[-1]      == 1; assert f.shape[-1] == 5
    assert f.BLUE().shape[-1]       == 1; assert f.shape[-1] == 5
    assert f.RGB().shape[-1]        == 3; assert f.shape[-1] == 5
    assert f.RGBRENIR().shape[-1]   == 5; assert f.shape[-1] == 5
    assert f.HUE().shape[-1]        == 1; assert f.shape[-1] == 8
    assert f.SATURATION().shape[-1] == 1; assert f.shape[-1] == 8
    assert f.VALUE().shape[-1]      == 1; assert f.shape[-1] == 8
    assert f.NDI().shape[-1]        == 1; assert f.shape[-1] == 9
    assert f.EX_G().shape[-1]       == 1; assert f.shape[-1] == 10
    assert f.MEX_G().shape[-1]      == 1; assert f.shape[-1] == 11
    assert f.EX_GR().shape[-1]      == 1; assert f.shape[-1] == 12
    assert f.VEG().shape[-1]        == 1; assert f.shape[-1] == 13
    assert f.RED_EDGE().shape[-1]   == 1; assert f.shape[-1] == 13
    assert f.NIR().shape[-1]        == 1; assert f.shape[-1] == 13
    assert f.NDVI().shape[-1]       == 1; assert f.shape[-1] == 14
    assert f.BNDVI().shape[-1]      == 1; assert f.shape[-1] == 15
    assert f.GNDVI().shape[-1]      == 1; assert f.shape[-1] == 16
    assert f.GARI().shape[-1]       == 1; assert f.shape[-1] == 17
    assert f.GLI().shape[-1]        == 1; assert f.shape[-1] == 18
    assert f.GBNDVI().shape[-1]     == 1; assert f.shape[-1] == 19
    assert f.GRNDVI().shape[-1]     == 1; assert f.shape[-1] == 20
    assert f.NDRE().shape[-1]       == 1; assert f.shape[-1] == 21
    assert f.LCI().shape[-1]        == 1; assert f.shape[-1] == 22
    assert f.MSAVI().shape[-1]      == 1; assert f.shape[-1] == 23
    assert f.OSAVI().shape[-1]      == 1; assert f.shape[-1] == 24
    assert f.X().shape[-1]          == 1; assert f.shape[-1] == 26
    assert f.Y().shape[-1]          == 1; assert f.shape[-1] == 26
    assert f.XY().shape[-1]         == 2; assert f.shape[-1] == 26

