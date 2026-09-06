# Auto generated from usertools.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-07-21T10:49:57
# Schema: user-tools
#
# id: http://wtwta.org/organisation/user-tools
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import String

metamodel_version = "1.11.0"
version = None

# Namespaces
USERCONF = CurieNamespace('userconf', 'http://wtwta.org/project/user-conf#')
USERSCRIPTS = CurieNamespace('userscripts', 'http://wtwta.org/project/user-scripts#')
USERTOOLS = CurieNamespace('usertools', 'http://wtwta.org/project/user-tools#')
DEFAULT_ = USERTOOLS


# Types

# Class references



class Shell(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = USERTOOLS["Shell"]
    class_class_curie: ClassVar[str] = "usertools:Shell"
    class_name: ClassVar[str] = "Shell"
    class_model_uri: ClassVar[URIRef] = USERTOOLS.Shell


class Terminal(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = USERTOOLS["Terminal"]
    class_class_curie: ClassVar[str] = "usertools:Terminal"
    class_name: ClassVar[str] = "Terminal"
    class_model_uri: ClassVar[URIRef] = USERTOOLS.Terminal


class XDesktop(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = USERTOOLS["XDesktop"]
    class_class_curie: ClassVar[str] = "usertools:XDesktop"
    class_name: ClassVar[str] = "XDesktop"
    class_model_uri: ClassVar[URIRef] = USERTOOLS.XDesktop


class String(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = USERTOOLS["String"]
    class_class_curie: ClassVar[str] = "usertools:String"
    class_name: ClassVar[str] = "String"
    class_model_uri: ClassVar[URIRef] = USERTOOLS.String


class Array(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = USERTOOLS["Array"]
    class_class_curie: ClassVar[str] = "usertools:Array"
    class_name: ClassVar[str] = "Array"
    class_model_uri: ClassVar[URIRef] = USERTOOLS.Array


class AssociativeArray(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = USERTOOLS["AssociativeArray"]
    class_class_curie: ClassVar[str] = "usertools:AssociativeArray"
    class_name: ClassVar[str] = "AssociativeArray"
    class_model_uri: ClassVar[URIRef] = USERTOOLS.AssociativeArray


class Lib(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = USERSCRIPTS["Lib"]
    class_class_curie: ClassVar[str] = "userscripts:Lib"
    class_name: ClassVar[str] = "Lib"
    class_model_uri: ClassVar[URIRef] = USERTOOLS.Lib


class User(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = USERCONF["User"]
    class_class_curie: ClassVar[str] = "userconf:User"
    class_name: ClassVar[str] = "User"
    class_model_uri: ClassVar[URIRef] = USERTOOLS.User


@dataclass(repr=False)
class Part(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = USERCONF["Part"]
    class_class_curie: ClassVar[str] = "userconf:Part"
    class_name: ClassVar[str] = "Part"
    class_model_uri: ClassVar[URIRef] = USERTOOLS.Part

    pre: Optional[str] = None
    var: Optional[str] = None
    fun: Optional[str] = None
    als: Optional[str] = None
    ssc: Optional[str] = None
    hooks: Optional[str] = None
    funs: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.pre is not None and not isinstance(self.pre, str):
            self.pre = str(self.pre)

        if self.var is not None and not isinstance(self.var, str):
            self.var = str(self.var)

        if self.fun is not None and not isinstance(self.fun, str):
            self.fun = str(self.fun)

        if self.als is not None and not isinstance(self.als, str):
            self.als = str(self.als)

        if self.ssc is not None and not isinstance(self.ssc, str):
            self.ssc = str(self.ssc)

        if self.hooks is not None and not isinstance(self.hooks, str):
            self.hooks = str(self.hooks)

        if self.funs is not None and not isinstance(self.funs, str):
            self.funs = str(self.funs)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Package(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = USERCONF["Package"]
    class_class_curie: ClassVar[str] = "userconf:Package"
    class_name: ClassVar[str] = "Package"
    class_model_uri: ClassVar[URIRef] = USERTOOLS.Package

    sh: Optional[str] = None
    json: Optional[str] = None
    dir: Optional[str] = None
    tools: Optional[str] = None
    envd: Optional[str] = None
    scripts: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.sh is not None and not isinstance(self.sh, str):
            self.sh = str(self.sh)

        if self.json is not None and not isinstance(self.json, str):
            self.json = str(self.json)

        if self.dir is not None and not isinstance(self.dir, str):
            self.dir = str(self.dir)

        if self.tools is not None and not isinstance(self.tools, str):
            self.tools = str(self.tools)

        if self.envd is not None and not isinstance(self.envd, str):
            self.envd = str(self.envd)

        if self.scripts is not None and not isinstance(self.scripts, str):
            self.scripts = str(self.scripts)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.part__pre = Slot(uri=USERCONF.pre, name="part__pre", curie=USERCONF.curie('pre'),
                   model_uri=USERTOOLS.part__pre, domain=None, range=Optional[str])

slots.part__var = Slot(uri=USERCONF.var, name="part__var", curie=USERCONF.curie('var'),
                   model_uri=USERTOOLS.part__var, domain=None, range=Optional[str])

slots.part__fun = Slot(uri=USERCONF.fun, name="part__fun", curie=USERCONF.curie('fun'),
                   model_uri=USERTOOLS.part__fun, domain=None, range=Optional[str])

slots.part__als = Slot(uri=USERCONF.als, name="part__als", curie=USERCONF.curie('als'),
                   model_uri=USERTOOLS.part__als, domain=None, range=Optional[str])

slots.part__ssc = Slot(uri=USERCONF.ssc, name="part__ssc", curie=USERCONF.curie('ssc'),
                   model_uri=USERTOOLS.part__ssc, domain=None, range=Optional[str])

slots.part__hooks = Slot(uri=USERCONF.hooks, name="part__hooks", curie=USERCONF.curie('hooks'),
                   model_uri=USERTOOLS.part__hooks, domain=None, range=Optional[str])

slots.part__funs = Slot(uri=USERCONF.funs, name="part__funs", curie=USERCONF.curie('funs'),
                   model_uri=USERTOOLS.part__funs, domain=None, range=Optional[str])

slots.package__sh = Slot(uri=USERCONF.sh, name="package__sh", curie=USERCONF.curie('sh'),
                   model_uri=USERTOOLS.package__sh, domain=None, range=Optional[str])

slots.package__json = Slot(uri=USERCONF.json, name="package__json", curie=USERCONF.curie('json'),
                   model_uri=USERTOOLS.package__json, domain=None, range=Optional[str])

slots.package__dir = Slot(uri=USERCONF.dir, name="package__dir", curie=USERCONF.curie('dir'),
                   model_uri=USERTOOLS.package__dir, domain=None, range=Optional[str])

slots.package__tools = Slot(uri=USERCONF.tools, name="package__tools", curie=USERCONF.curie('tools'),
                   model_uri=USERTOOLS.package__tools, domain=None, range=Optional[str])

slots.package__envd = Slot(uri=USERCONF.envd, name="package__envd", curie=USERCONF.curie('envd'),
                   model_uri=USERTOOLS.package__envd, domain=None, range=Optional[str])

slots.package__scripts = Slot(uri=USERCONF.scripts, name="package__scripts", curie=USERCONF.curie('scripts'),
                   model_uri=USERTOOLS.package__scripts, domain=None, range=Optional[str])
