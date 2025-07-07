# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:11:05 2021

@author: John Meluso
"""
import matplotlib as mpl
import matplotlib.pylab as pylab


def set_fonts(extra_params={}):
    params = {
        "font.family": "sans-serif",
        "font.sans-serif": [
            "Franklin Gothic Medium",
            "DejaVu Sans",
            "Lucida Grande",
            "Verdana",
        ],
        "mathtext.fontset": "cm",
        "legend.fontsize": 14,
        "axes.labelsize": 14,
        "axes.titlesize": 14,
        "xtick.labelsize": 14,
        "ytick.labelsize": 14,
        "figure.titlesize": 14,
    }
    for key, value in extra_params.items():
        params[key] = value
    pylab.rcParams.update(params)
