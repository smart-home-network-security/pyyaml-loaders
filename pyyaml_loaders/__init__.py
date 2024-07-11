"""
Initialization script for package `pyyaml_loaders`.
"""

import yaml
from IncludeLoader import IncludeLoader, construct_include
from IgnoreLoader import IgnoreLoader, construct_ignore

# Add custom constructors
yaml.add_constructor("!include", construct_include, IncludeLoader)
yaml.add_multi_constructor("!", construct_ignore, IgnoreLoader)
