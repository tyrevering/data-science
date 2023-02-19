# -*- coding: utf-8 -*-
"""Establishing certainty equivalent discounting rates. Formulas and theorems
based off paper on discounting rates for civil infrastructure written by Ji
Yun Lee https://www.sciencedirect.com/science/article/pii/S0167473015000466"""

__author__ = "ty revering"

from random import uniform
from matplotlib import pyplot as plt


def discount_factor(t, min_rate=0.01, max_rate=0.1):
    """Returns the discrete discount factor given time t and a randomized
    discount rate"""
    return 1 / ((1 + uniform(min_rate, max_rate))**t)


def cert_equiv_factor(t_horizon):
    """Returns the certainty equivalent discount factor of a time horizon,
    given the discount factor"""
    total_disc_factor = 0
    for t in range(t_horizon):
        total_disc_factor += discount_factor(t)

    return total_disc_factor / t_horizon


def cert_equiv_rate(t_horizon):
    return ((1 / (cert_equiv_factor(t_horizon))**(1 / t_horizon))-1)


def plot_rates():
    """Graphing with time horizons ranging from 10 to 300 years"""
    t_horizons = [10, 50, 100, 300]
    cert_equiv_rates = []
    cert_equiv_factors = []

    for t_horizon in t_horizons:
        cert_equiv_rates.append(cert_equiv_rate(t_horizon))
        cert_equiv_factors.append(cert_equiv_factor(t_horizon))

    plt.plot(t_horizons, cert_equiv_rates)
    plt.xlabel("Time Horizons")
    plt.ylabel("Certainty Equivalent Discount Rate")


if __name__ == "__main__":
    plot_rates()
