from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.11.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'usertools',
     'id': 'http://wtwta.org/organisation/user-tools',
     'imports': ['userscripts', 'userconf'],
     'name': 'user-tools',
     'prefixes': {'usertools': {'prefix_prefix': 'usertools',
                                'prefix_reference': 'http://wtwta.org/project/user-tools#'}},
     'source_file': 'src/usertools/schema/usertools.yaml'} )


class Lib(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://wtwta.org/project/user-scripts'})

    pass


class User(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://wtwta.org/project/user-conf'})

    pass


class Part(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://wtwta.org/project/user-conf'})

    pre: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Part']} })
    var: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Part']} })
    fun: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Part']} })
    als: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Part']} })
    ssc: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Part']} })
    hooks: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Part']} })
    funs: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Part']} })


class Package(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://wtwta.org/project/user-conf'})

    sh: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Package']} })
    json: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Package']} })
    dir: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Package']} })
    tools: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Package']} })
    envd: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Package']} })
    scripts: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Package']} })


class Shell(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://wtwta.org/organisation/user-tools'})

    pass


class Terminal(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://wtwta.org/organisation/user-tools'})

    pass


class XDesktop(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://wtwta.org/organisation/user-tools'})

    pass


class String(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://wtwta.org/organisation/user-tools'})

    pass


class Array(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://wtwta.org/organisation/user-tools'})

    pass


class AssociativeArray(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://wtwta.org/organisation/user-tools'})

    pass


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Lib.model_rebuild()
User.model_rebuild()
Part.model_rebuild()
Package.model_rebuild()
Shell.model_rebuild()
Terminal.model_rebuild()
XDesktop.model_rebuild()
String.model_rebuild()
Array.model_rebuild()
AssociativeArray.model_rebuild()
