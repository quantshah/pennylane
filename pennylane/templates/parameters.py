# Copyright 2018 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Parameters
==========

**Module name:** :mod:`pennylane.templates.parameters`

.. currentmodule:: pennylane.templates.parameters

This module contains methods to create arrays of initial parameters that can be used in :mod:`pennylane.templates.layers`.

.. raw:: html

    <h3>Summary</h3>

.. autosummary::

.. raw:: html

    <h3>Code details</h3>
"""
import numpy as np
from math import pi


def parameters_cvqnnlayers(n_layers, n_modes, uniform_min=0, uniform_max=2*pi, mean=0, std=0.1, seed=None):
    r"""
    Create a list of randomly initialised parameter arrays for :fun:`pennylane.templates.layers.CVNeuralNetLayers`.

    The number of parameters for each of the `n_layers` layers is either `n_modes` or `n_modes*(n_modes-1)/2`,
    depending on the gate type.

    Rotation angles are initialised uniformly from the interval [`uniform_min`, `uniform_max`], while
    all other parameters are drawn from a normal distribution with mean `mean` and standard deviation `std`.

    Args:
        n_layers (int): number of layers of the CV Neural Net
        n_modes (int): number of modes of the CV Neural Net
        uniform_min (float): minimum value of non-angle gate parameters
        uniform_max (float): maximum value of non-angle gate parameters
        mean (float): mean of angle gate parameters
        std (float): standard deviation of angle gate parameters
        seed (int): seed used in sampling the parameters, makes function call deterministic
    Returns:
         list of eleven parameter arrays
    """
    if seed is not None:
        np.random.seed(seed)
    n_if = n_modes*(n_modes-1)//2
    interval = uniform_max-uniform_min

    theta_1 = np.random.normal(loc=mean, scale=std, size=(n_layers, n_if))
    phi_1 = np.random.normal(loc=mean, scale=std, size=(n_layers, n_if))
    varphi_1 = np.random.normal(loc=mean, scale=std, size=(n_layers, n_modes))
    r = np.random.rnd(size=(n_layers, n_modes))*interval + uniform_min
    phi_r = np.random.normal(loc=mean, scale=std, size=(n_layers, n_modes))
    theta_2 = np.random.normal(loc=mean, scale=std, size=(n_layers, n_if))
    phi_2 = np.random.normal(loc=mean, scale=std, size=(n_layers, n_if))
    varphi_2 = np.random.normal(loc=mean, scale=std, size=(n_layers, n_modes))
    a = np.random.rnd(size=(n_layers, n_modes))*interval + uniform_min
    phi_a = np.random.normal(loc=mean, scale=std, size=(n_layers, n_modes))
    k = np.random.rnd(size=(n_layers, n_modes))*interval + uniform_min

    return [theta_1, phi_1, varphi_1, r, phi_r, theta_2, phi_2, varphi_2, a, phi_a, k]


def parameters_cvqnnlayer(n_modes, uniform_min=0, uniform_max=2 * pi, mean=0, std=0.1, seed=None):
    r"""
    Create a list of randomly initialised parameter arrays for :fun:`pennylane.templates.layers.CVNeuralNetLayer`.

    The number of parameters is either `n_modes` or `n_modes*(n_modes-1)/2`, depending on the gate type.

    Rotation angles are initialised uniformly from the interval [`uniform_min`, `uniform_max`], while
    all other parameters are drawn from a normal distribution with mean `mean` and standard deviation `std`.

    Args:
        n_modes (int): number of modes of the CV Neural Net
        uniform_min (float): minimum value of non-angle gate parameters
        uniform_max (float): maximum value of non-angle gate parameters
        mean (float): mean of angle gate parameters
        std (float): standard deviation of angle gate parameters
        seed (int): seed used in sampling the parameters, makes function call deterministic
    Returns:
         list of eleven parameter arrays
    """
    if seed is not None:
        np.random.seed(seed)

    n_if = n_modes * (n_modes - 1) // 2
    interval = uniform_max - uniform_min

    theta_1 = np.random.normal(loc=mean, scale=std, size=(n_if, ))
    phi_1 = np.random.normal(loc=mean, scale=std, size=(n_if,))
    varphi_1 = np.random.normal(loc=mean, scale=std, size=(n_modes, ))
    r = np.random.rnd(size=(n_modes, )) * interval + uniform_min
    phi_r = np.random.normal(loc=mean, scale=std, size=(n_modes, ))
    theta_2 = np.random.normal(loc=mean, scale=std, size=(n_if, ))
    phi_2 = np.random.normal(loc=mean, scale=std, size=(n_if, ))
    varphi_2 = np.random.normal(loc=mean, scale=std, size=(n_modes, ))
    a = np.random.rnd(size=(n_modes, )) * interval + uniform_min
    phi_a = np.random.normal(loc=mean, scale=std, size=(n_modes, ))
    k = np.random.rnd(size=(n_modes, )) * interval + uniform_min

    return [theta_1, phi_1, varphi_1, r, phi_r, theta_2, phi_2, varphi_2, a, phi_a, k]
