#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

class State:
    def __init_(self):

    def bins(self,clip_min, clip_max, num):
        return np.linspace(clip_min, clip_max, num + 1)[1:-1]

    def digitize_state(self,observation):
        cart_pos, cart_v, pole_angle, pole_v = observation
        digitized = [
            np.digitize(cart_pos, bins=bins(-2.4, 2.4, num_dizitized)),
            np.digitize(cart_v, bins=bins(-3.0, 3.0, num_dizitized)),
            np.digitize(pole_angle, bins=bins(-0.5, 0.5, num_dizitized)),
            np.digitize(pole_v, bins=bins(-2.0, 2.0, num_dizitized))
        ]
        return sum([x * (num_dizitized**i) for i, x in enumerate(digitized)])
