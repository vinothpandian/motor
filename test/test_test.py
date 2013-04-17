# Copyright 2013 10gen, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Test Motor's test helpers."""

from tornado.testing import gen_test

import motor
from test import MotorTest, assert_raises


def require_callback(callback=None):
    motor.check_callable(callback, True)
    callback(None, None)


def dont_require_callback(callback=None):
    motor.check_callable(callback, False)
    if callback is not None:
        callback(None, None)


class MotorCallbackTestTest(MotorTest):
    @gen_test
    def test_check_required_callback(self):
        yield self.check_required_callback(require_callback)
        with assert_raises(Exception):
            yield self.check_required_callback(dont_require_callback)

    @gen_test
    def test_check_optional_callback(self):
        yield self.check_optional_callback(dont_require_callback)
        with assert_raises(Exception):
            yield self.check_optional_callback(require_callback)
