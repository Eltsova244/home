from _typeshed import Incomplete, SupportsKeysAndGetItem
from collections.abc import Iterable
from typing import Any, TypeVar, overload
from typing_extensions import Literal, SupportsIndex

from ..orm.attributes import Event
from ..util.langhelpers import _symbol, symbol

_T = TypeVar("_T")
_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

class _PlainColumnGetter:
    cols: Any
    composite: Any
    def __init__(self, cols) -> None: ...
    def __reduce__(self): ...
    def __call__(self, value): ...

class _SerializableColumnGetter:
    colkeys: Any
    composite: Any
    def __init__(self, colkeys) -> None: ...
    def __reduce__(self): ...
    def __call__(self, value): ...

class _SerializableColumnGetterV2(_PlainColumnGetter):
    colkeys: Any
    composite: Any
    def __init__(self, colkeys) -> None: ...
    def __reduce__(self): ...

def column_mapped_collection(mapping_spec): ...

class _SerializableAttrGetter:
    name: Any
    getter: Any
    def __init__(self, name) -> None: ...
    def __call__(self, target): ...
    def __reduce__(self): ...

def attribute_mapped_collection(attr_name): ...
def mapped_collection(keyfunc): ...

class collection:
    @staticmethod
    def appender(fn): ...
    @staticmethod
    def remover(fn): ...
    @staticmethod
    def iterator(fn): ...
    @staticmethod
    def internally_instrumented(fn): ...
    @staticmethod
    def converter(fn): ...
    @staticmethod
    def adds(arg): ...
    @staticmethod
    def replaces(arg): ...
    @staticmethod
    def removes(arg): ...
    @staticmethod
    def removes_return(): ...

collection_adapter: Any

class CollectionAdapter:
    attr: Any
    owner_state: Any
    invalidated: bool
    empty: bool
    def __init__(self, attr, owner_state, data) -> None: ...
    @property
    def data(self): ...
    def bulk_appender(self): ...
    def append_with_event(self, item, initiator: Incomplete | None = None) -> None: ...
    def append_without_event(self, item) -> None: ...
    def append_multiple_without_event(self, items) -> None: ...
    def bulk_remover(self): ...
    def remove_with_event(self, item, initiator: Incomplete | None = None) -> None: ...
    def remove_without_event(self, item) -> None: ...
    def clear_with_event(self, initiator: Incomplete | None = None) -> None: ...
    def clear_without_event(self) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __nonzero__(self) -> bool: ...
    def fire_append_wo_mutation_event(self, item, initiator: Incomplete | None = None): ...
    def fire_append_event(self, item, initiator: Incomplete | None = None): ...
    def fire_remove_event(self, item, initiator: Incomplete | None = None) -> None: ...
    def fire_pre_remove_event(self, initiator: Incomplete | None = None) -> None: ...

class InstrumentedList(list[_T]):
    def append(self, item, _sa_initiator: Event | Literal[False] | None = None) -> None: ...
    def clear(self, index: SupportsIndex = -1) -> None: ...
    def extend(self, iterable: Iterable[_T]) -> None: ...
    def insert(self, index: SupportsIndex, value: _T) -> None: ...
    def pop(self, index: SupportsIndex = -1) -> _T: ...
    def remove(self, value: _T, _sa_initiator: Event | Literal[False] | None = None) -> None: ...

class InstrumentedSet(set[_T]):
    def add(self, value: _T, _sa_initiator: Event | Literal[False] | None = None) -> None: ...
    def difference_update(self, value: Iterable[_T]) -> None: ...  # type: ignore[override]
    def discard(self, value: _T, _sa_initiator: Event | Literal[False] | None = None) -> None: ...
    def intersection_update(self, other: Iterable[_T]) -> None: ...  # type: ignore[override]
    def remove(self, value: _T, _sa_initiator: Event | Literal[False] | None = None) -> None: ...
    def symmetric_difference_update(self, other: Iterable[_T]) -> None: ...
    def update(self, value: Iterable[_T]) -> None: ...  # type: ignore[override]

class InstrumentedDict(dict[_KT, _VT]): ...

class MappedCollection(dict[_KT, _VT]):
    keyfunc: Any
    def __init__(self, keyfunc) -> None: ...
    def set(self, value: _VT, _sa_initiator: Event | Literal[False] | None = None) -> None: ...
    def remove(self, value: _VT, _sa_initiator: Event | Literal[False] | None = None) -> None: ...
    def __delitem__(self, key: _KT, _sa_initiatorEvent: Event | Literal[False] | None = None) -> None: ...
    def __setitem__(self, key: _KT, value: _VT, _sa_initiator: Event | Literal[False] | None = None) -> None: ...
    @overload
    def pop(self, key: _KT) -> _VT: ...
    @overload
    def pop(self, key: _KT, default: _VT | _T | _symbol | symbol = ...) -> _VT | _T: ...
    @overload  # type: ignore[override]
    def setdefault(self, key: _KT, default: _T) -> _VT | _T: ...
    @overload
    def setdefault(self, key: _KT, default: None = None) -> _VT | None: ...
    @overload
    def update(self, __other: SupportsKeysAndGetItem[_KT, _VT] = ..., **kwargs: _VT) -> None: ...
    @overload
    def update(self, __other: Iterable[tuple[_KT, _VT]] = ..., **kwargs: _VT) -> None: ...
