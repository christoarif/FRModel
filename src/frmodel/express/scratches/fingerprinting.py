import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import skew, kurtosis
from sklearn.preprocessing import scale
#%%
from frmodel.data.load import load_spec

# Change to loadable path.
f, trees = load_spec("/Users/muktiastuticiptaningtyas/Desktop/Y2S1/URECA Forest Recovery Modelling/chestnut-18dec2020/")  # "../imgs/spec/chestnut/10May2021/90deg43m85pct255deg/map/")

#%%
features = []
names = []
for tree in trees:
    names.append(tree.name)
    tree_features = []
    # tree.frame.get_glcm()
    tree.frame.get_chns([
       # *f.CHN.HSV,
       #  f.CHN.NDI,
       #  f.CHN.EX_G,
       #  f.CHN.MEX_G,
       #  f.CHN.EX_GR,
       #  f.CHN.VEG,
        f.CHN.RED_EDGE,
        f.CHN.NIR,
        f.CHN.RED,
        f.CHN.BLUE,
        f.CHN.GREEN,
        # f.CHN.NDVI,
        # f.CHN.BNDVI,
        # f.CHN.GNDVI,
        # f.CHN.GARI,
        # f.CHN.GLI,
        # f.CHN.GBNDVI,
        # f.CHN.GRNDVI,
        # f.CHN.NDRE,
        # f.CHN.LCI,
        # f.CHN.MSAVI,
        # f.CHN.OSAVI
    ])
    tree.frame.get_glcm()
    for m in (np.mean, np.var, skew, kurtosis):
        for i in range(tree.frame.shape[-1]):
            tree_features.append(m(tree.frame.data[..., i].flatten()))
    features.append(tree_features)

#%%
ar = scale(np.asarray(features),axis=0)
#%%
fig, ax = plt.subplots(18,1, sharex=True, sharey=True, figsize=(4,10))
for i in range(18):
    ax[i].imshow(ar[i:i+1].reshape(6,-1))
    ax[i].set_title(names[i],  ha='center', va='center')
fig.tight_layout()
fig.show()

