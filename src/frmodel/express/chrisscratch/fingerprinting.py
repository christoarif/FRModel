import os
import sys
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import hist
from scipy.stats import skew, kurtosis
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import scale
from frmodel import *
from frmodel.base.D2 import Frame2D
from frmodel.data.load import load_spec
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import joblib

#%%
features = []
names = []
directory = "/Users/muktiastuticiptaningtyas/Desktop/FRModel_data/GLCM_Results/Dec20/"
for treefile in os.listdir(directory):
    names.append(treefile[:-5])
    tree = Frame2D.load(directory+treefile)
    tree_featuresNew = []
    # tree.get_chns([
    #    # *f.CHN.HSV,
    #    #  f.CHN.NDI,
    #    #  f.CHN.EX_G,
    #    #  f.CHN.MEX_G,
    #    #  f.CHN.EX_GR,
    #    #  f.CHN.VEG,
    #     f.CHN.RED_EDGE,
    #     f.CHN.NIR,
    #     f.CHN.RED,
    #     f.CHN.BLUE,
    #     f.CHN.GREEN,
    #     # f.CHN.NDVI,
    #     # f.CHN.BNDVI,
    #     # f.CHN.GNDVI,
    #     # f.CHN.GARI,
    #     # f.CHN.GLI,
    #     # f.CHN.GBNDVI,
    #     # f.CHN.GRNDVI,
    #     # f.CHN.NDRE,
    #     # f.CHN.LCI,
    #     # f.CHN.MSAVI,
    #     # f.CHN.OSAVI
    # ])
    for m in (np.mean, np.var, skew, kurtosis):
        for i in range(tree.shape[-1]):
            tree_featuresNew.append(m(tree.data[..., i].flatten()))
    features.append(tree_featuresNew)

#%%
ar = scale(np.asarray(features),axis=0)
#ar2 = np.asarray(features)
# ar_column_normalised = (ar2 - ar2.min(0)) / ar2.ptp(0)
#%%
fig, ax = plt.subplots(18,1, sharex=True, sharey=True, figsize=(4,10))
for i in range(18):
    ax[i].imshow(ar[i:i+1].reshape(3,-1), cmap = "jet")
    ax[i].set_title(names[i],  ha='center', va='center')
#fig.tight_layout()
fig.suptitle("5bit GLCM Dec 20", y=0.95)
fig.show()

