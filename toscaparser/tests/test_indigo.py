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
from toscaparser.elements.entity_type import EntityType
import toscaparser.imports
from toscaparser.tests.base import TestCase
from toscaparser.tosca_template import ToscaTemplate
from toscaparser.utils.yamlparser import load_yaml


class IndigoToscaTemplate(ToscaTemplate):

    CUSTOM_TYPES_FILE = os.path.join(os.path.dirname(
                                     os.path.abspath(__file__)),
                                     "data/indigo/custom_types.yaml")

    def __init__(self, path, parsed_params=None, a_file=True):
        # Load custom data
        custom_def = load_yaml(self.CUSTOM_TYPES_FILE)
        # and update tosca_def with the data
        EntityType.TOSCA_DEF.update(custom_def)

        super(IndigoToscaTemplate, self).__init__(path, parsed_params, a_file)

    def _get_custom_types(self, type_definitions, imports=None):
        """Handle custom types defined in imported template files

        This method loads the custom type definitions referenced in "imports"
        section of the TOSCA YAML template.
        """

        custom_defs = {}
        type_defs = []
        if not isinstance(type_definitions, list):
            type_defs.append(type_definitions)
        else:
            type_defs = type_definitions

        if not imports:
            imports = self._tpl_imports()

        if imports:
            custom_defs = toscaparser.imports.\
                ImportsLoader(imports, self.path,
                              type_defs).get_custom_defs()

        # Handle custom types defined in current template file
        for type_def in type_defs:
            if type_def != "imports":
                inner_custom_types = self.tpl.get(type_def) or {}
                if inner_custom_types:
                    custom_defs.update(inner_custom_types)
        return custom_defs


class IndigoTest(TestCase):

    def test_galaxy(self):
        tosca_tpl = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "data/indigo/examples/galaxy_tosca.yaml")
        IndigoToscaTemplate(tosca_tpl)

    def test_web_mysql(self):
        tosca_tpl = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "data/indigo/examples/web_mysql_tosca.yaml")
        IndigoToscaTemplate(tosca_tpl)

    def test_elastic_cluster(self):
        tosca_tpl = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "data/indigo/examples/clues_tosca.yaml")
        IndigoToscaTemplate(tosca_tpl)
