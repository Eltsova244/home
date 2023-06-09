from _typeshed import Incomplete
from typing import Any, Generic, TypeVar

from .base import SchemaEventTarget
from .operators import ColumnOperators
from .traversals import HasCacheKey
from .type_api import (
    Emulated as Emulated,
    NativeForEmulated as NativeForEmulated,
    TypeDecorator as TypeDecorator,
    TypeEngine as TypeEngine,
    Variant as Variant,
    to_instance as to_instance,
)

_T = TypeVar("_T")

class _LookupExpressionAdapter:
    class Comparator(TypeEngine.Comparator[Any]): ...
    comparator_factory: Any

class Concatenable:
    class Comparator(TypeEngine.Comparator[_T], Generic[_T]): ...
    comparator_factory: Any

class Indexable:
    class Comparator(TypeEngine.Comparator[_T], Generic[_T]):
        def __getitem__(self, index) -> ColumnOperators[_T]: ...
    comparator_factory: Any

class String(Concatenable, TypeEngine):
    __visit_name__: str
    RETURNS_UNICODE: Any
    RETURNS_BYTES: Any
    RETURNS_CONDITIONAL: Any
    RETURNS_UNKNOWN: Any
    length: Any
    collation: Any
    def __init__(
        self,
        length: Incomplete | None = None,
        collation: Incomplete | None = None,
        convert_unicode: bool = False,
        unicode_error: Incomplete | None = None,
        _warn_on_bytestring: bool = False,
        _expect_unicode: bool = False,
    ) -> None: ...
    def literal_processor(self, dialect): ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...
    @property
    def python_type(self): ...
    def get_dbapi_type(self, dbapi): ...

class Text(String):
    __visit_name__: str

class Unicode(String):
    __visit_name__: str
    def __init__(self, length: Incomplete | None = None, **kwargs) -> None: ...

class UnicodeText(Text):
    __visit_name__: str
    def __init__(self, length: Incomplete | None = None, **kwargs) -> None: ...

class Integer(_LookupExpressionAdapter, TypeEngine):
    __visit_name__: str
    def get_dbapi_type(self, dbapi): ...
    @property
    def python_type(self): ...
    def literal_processor(self, dialect): ...

class SmallInteger(Integer):
    __visit_name__: str

class BigInteger(Integer):
    __visit_name__: str

class Numeric(_LookupExpressionAdapter, TypeEngine):
    __visit_name__: str
    precision: Any
    scale: Any
    decimal_return_scale: Any
    asdecimal: Any
    def __init__(
        self,
        precision: Incomplete | None = None,
        scale: Incomplete | None = None,
        decimal_return_scale: Incomplete | None = None,
        asdecimal: bool = True,
    ) -> None: ...
    def get_dbapi_type(self, dbapi): ...
    def literal_processor(self, dialect): ...
    @property
    def python_type(self): ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class Float(Numeric):
    __visit_name__: str
    scale: Any
    precision: Any
    asdecimal: Any
    decimal_return_scale: Any
    def __init__(
        self, precision: Incomplete | None = None, asdecimal: bool = False, decimal_return_scale: Incomplete | None = None
    ) -> None: ...
    def result_processor(self, dialect, coltype): ...

class DateTime(_LookupExpressionAdapter, TypeEngine):
    __visit_name__: str
    timezone: Any
    def __init__(self, timezone: bool = False) -> None: ...
    def get_dbapi_type(self, dbapi): ...
    @property
    def python_type(self): ...

class Date(_LookupExpressionAdapter, TypeEngine):
    __visit_name__: str
    def get_dbapi_type(self, dbapi): ...
    @property
    def python_type(self): ...

class Time(_LookupExpressionAdapter, TypeEngine):
    __visit_name__: str
    timezone: Any
    def __init__(self, timezone: bool = False) -> None: ...
    def get_dbapi_type(self, dbapi): ...
    @property
    def python_type(self): ...

class _Binary(TypeEngine):
    length: Any
    def __init__(self, length: Incomplete | None = None) -> None: ...
    def literal_processor(self, dialect): ...
    @property
    def python_type(self): ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...
    def coerce_compared_value(self, op, value): ...
    def get_dbapi_type(self, dbapi): ...

class LargeBinary(_Binary):
    __visit_name__: str
    def __init__(self, length: Incomplete | None = None) -> None: ...

class SchemaType(SchemaEventTarget):
    name: Any
    schema: Any
    metadata: Any
    inherit_schema: Any
    def __init__(
        self,
        name: Incomplete | None = None,
        schema: Incomplete | None = None,
        metadata: Incomplete | None = None,
        inherit_schema: bool = False,
        quote: Incomplete | None = None,
        _create_events: bool = True,
    ) -> None: ...
    def copy(self, **kw): ...
    def adapt(self, impltype, **kw): ...
    @property
    def bind(self): ...
    def create(self, bind: Incomplete | None = None, checkfirst: bool = False) -> None: ...
    def drop(self, bind: Incomplete | None = None, checkfirst: bool = False) -> None: ...

class Enum(Emulated, String, SchemaType):
    __visit_name__: str
    def __init__(self, *enums, **kw) -> None: ...
    @property
    def sort_key_function(self): ...
    @property
    def native(self): ...

    class Comparator(Concatenable.Comparator[Any]): ...
    comparator_factory: Any
    def as_generic(self, allow_nulltype: bool = False): ...
    def adapt_to_emulated(self, impltype, **kw): ...
    def adapt(self, impltype, **kw): ...
    def literal_processor(self, dialect): ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...
    def copy(self, **kw): ...
    @property
    def python_type(self): ...

class PickleType(TypeDecorator):
    impl: Any
    cache_ok: bool
    protocol: Any
    pickler: Any
    comparator: Any
    def __init__(
        self, protocol=5, pickler: Incomplete | None = None, comparator: Incomplete | None = None, impl: Incomplete | None = None
    ) -> None: ...
    def __reduce__(self): ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...
    def compare_values(self, x, y): ...

class Boolean(Emulated, TypeEngine, SchemaType):  # type: ignore[misc]
    __visit_name__: str
    native: bool
    create_constraint: Any
    name: Any
    def __init__(self, create_constraint: bool = False, name: Incomplete | None = None, _create_events: bool = True) -> None: ...
    @property
    def python_type(self): ...
    def literal_processor(self, dialect): ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class _AbstractInterval(_LookupExpressionAdapter, TypeEngine):
    def coerce_compared_value(self, op, value): ...

class Interval(Emulated, _AbstractInterval, TypeDecorator):  # type: ignore[misc]
    impl: Any
    epoch: Any
    cache_ok: bool
    native: Any
    second_precision: Any
    day_precision: Any
    def __init__(
        self, native: bool = True, second_precision: Incomplete | None = None, day_precision: Incomplete | None = None
    ) -> None: ...
    @property
    def python_type(self): ...
    def adapt_to_emulated(self, impltype, **kw): ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class JSON(Indexable, TypeEngine):
    __visit_name__: str
    hashable: bool
    NULL: Any
    none_as_null: Any
    def __init__(self, none_as_null: bool = False) -> None: ...

    class JSONElementType(TypeEngine):
        def string_bind_processor(self, dialect): ...
        def string_literal_processor(self, dialect): ...
        def bind_processor(self, dialect): ...
        def literal_processor(self, dialect): ...

    class JSONIndexType(JSONElementType): ...
    class JSONIntIndexType(JSONIndexType): ...
    class JSONStrIndexType(JSONIndexType): ...
    class JSONPathType(JSONElementType): ...

    class Comparator(Indexable.Comparator[Any], Concatenable.Comparator[Any]):
        def as_boolean(self): ...
        def as_string(self): ...
        def as_integer(self): ...
        def as_float(self): ...
        def as_numeric(self, precision, scale, asdecimal: bool = True): ...
        def as_json(self): ...
    comparator_factory: Any
    @property
    def python_type(self): ...
    @property  # type: ignore[override]
    def should_evaluate_none(self): ...
    @should_evaluate_none.setter
    def should_evaluate_none(self, value) -> None: ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class ARRAY(SchemaEventTarget, Indexable, Concatenable, TypeEngine):
    __visit_name__: str
    zero_indexes: bool

    class Comparator(Indexable.Comparator[_T], Concatenable.Comparator[_T], Generic[_T]):
        def contains(self, *arg, **kw) -> ColumnOperators[_T]: ...
        def any(self, other, operator: Incomplete | None = None): ...
        def all(self, other, operator: Incomplete | None = None): ...
    comparator_factory: Any
    item_type: Any
    as_tuple: Any
    dimensions: Any
    def __init__(
        self, item_type, as_tuple: bool = False, dimensions: Incomplete | None = None, zero_indexes: bool = False
    ) -> None: ...
    @property
    def hashable(self): ...
    @property
    def python_type(self): ...
    def compare_values(self, x, y): ...

class TupleType(TypeEngine):
    types: Any
    def __init__(self, *types) -> None: ...
    def result_processor(self, dialect, coltype) -> None: ...

class REAL(Float):
    __visit_name__: str

class FLOAT(Float):
    __visit_name__: str

class NUMERIC(Numeric):
    __visit_name__: str

class DECIMAL(Numeric):
    __visit_name__: str

class INTEGER(Integer):
    __visit_name__: str

INT = INTEGER

class SMALLINT(SmallInteger):
    __visit_name__: str

class BIGINT(BigInteger):
    __visit_name__: str

class TIMESTAMP(DateTime):
    __visit_name__: str
    def __init__(self, timezone: bool = False) -> None: ...
    def get_dbapi_type(self, dbapi): ...

class DATETIME(DateTime):
    __visit_name__: str

class DATE(Date):
    __visit_name__: str

class TIME(Time):
    __visit_name__: str

class TEXT(Text):
    __visit_name__: str

class CLOB(Text):
    __visit_name__: str

class VARCHAR(String):
    __visit_name__: str

class NVARCHAR(Unicode):
    __visit_name__: str

class CHAR(String):
    __visit_name__: str

class NCHAR(Unicode):
    __visit_name__: str

class BLOB(LargeBinary):
    __visit_name__: str

class BINARY(_Binary):
    __visit_name__: str

class VARBINARY(_Binary):
    __visit_name__: str

class BOOLEAN(Boolean):
    __visit_name__: str

class NullType(TypeEngine):
    __visit_name__: str
    def literal_processor(self, dialect): ...

    class Comparator(TypeEngine.Comparator[Any]): ...
    comparator_factory: Any

class TableValueType(HasCacheKey, TypeEngine):
    def __init__(self, *elements) -> None: ...

class MatchType(Boolean): ...

NULLTYPE: NullType
BOOLEANTYPE: Boolean
STRINGTYPE: String
INTEGERTYPE: Integer
NUMERICTYPE: Numeric
MATCHTYPE: MatchType
TABLEVALUE: TableValueType
DATETIME_TIMEZONE: DateTime
TIME_TIMEZONE: Time
