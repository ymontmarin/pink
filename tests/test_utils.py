#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2022 Stéphane Caron
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Test fixture for other library features.
"""

import os
import unittest

from pink.models import build_from_urdf
from pink.utils import custom_configuration_vector


class TestExtras(unittest.TestCase):
    def setUp(self):
        """
        Prepare test fixture.
        """
        models_dir = os.path.join(os.path.dirname(__file__), "models")
        self.upkie_description = os.path.join(models_dir, "upkie_description")

    def test_custom_configuration_vector(self):
        """
        Check a custom configuration vector for Upkie. Assumes the left and
        right knees have joint indices respectively 8 and 11 in the
        configuration vector.
        """
        robot = build_from_urdf(self.upkie_description)
        q = custom_configuration_vector(robot, left_knee=0.2, right_knee=-0.2)
        self.assertAlmostEqual(q[8], 0.2)
        self.assertAlmostEqual(q[11], -0.2)
