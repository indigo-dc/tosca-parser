#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
import time
from toscaparser.tests.base import TestCase
from toscaparser.tosca_template import ToscaTemplate


class IndigoTest(TestCase):

    def test_indigo_examples(self):
        filenames = []
        try:
            tests_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "data/indigo/examples")
            filenames = [os.path.join(root, name)
                         for root, dirs, files in os.walk(tests_path)
                         for name in files
                         if name.endswith((".yaml"))]
        except Exception:
            pass
        for num, filename in enumerate(filenames):
            if num < 20:
                ToscaTemplate(filename)

    def test_indigo_examples2(self):
        filenames = []
        try:
            tests_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "data/indigo/examples")
            filenames = [os.path.join(root, name)
                         for root, dirs, files in os.walk(tests_path)
                         for name in files
                         if name.endswith((".yaml"))]
        except Exception:
            pass
        for num, filename in enumerate(filenames):
            if num >= 20:
                ToscaTemplate(filename)
