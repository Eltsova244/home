from _typeshed import Incomplete
from collections.abc import Callable
from typing import Any
from typing_extensions import Self

from ..sql.base import Generative
from .interfaces import LoaderOption

class Load(Generative, LoaderOption):
    path: Any
    context: Any
    local_opts: Any
    is_class_strategy: bool
    def __init__(self, entity) -> None: ...
    @classmethod
    def for_existing_path(cls, path): ...
    is_opts_only: bool
    strategy: Any
    propagate_to_loaders: bool
    def process_compile_state_replaced_entities(self, compile_state, mapper_entities) -> None: ...
    def process_compile_state(self, compile_state) -> None: ...
    def options(self, *opts) -> Self: ...
    def set_relationship_strategy(self, attr, strategy, propagate_to_loaders: bool = True) -> Self: ...
    def set_column_strategy(self, attrs, strategy, opts: Incomplete | None = None, opts_only: bool = False) -> Self: ...
    def set_generic_strategy(self, attrs, strategy) -> Self: ...
    def set_class_strategy(self, strategy, opts) -> Self: ...
    # Added dynamically at runtime
    def contains_eager(loadopt, attr, alias: Incomplete | None = None) -> Self: ...
    def load_only(loadopt, *attrs) -> Self: ...
    def joinedload(loadopt, attr, innerjoin: Incomplete | None = None) -> Self: ...
    def subqueryload(loadopt, attr) -> Self: ...
    def selectinload(loadopt, attr) -> Self: ...
    def lazyload(loadopt, attr) -> Self: ...
    def immediateload(loadopt, attr) -> Self: ...
    def noload(loadopt, attr) -> Self: ...
    def raiseload(loadopt, attr, sql_only: bool = False) -> Self: ...
    def defaultload(loadopt, attr) -> Self: ...
    def defer(loadopt, key, raiseload: bool = False) -> Self: ...
    def undefer(loadopt, key) -> Self: ...
    def undefer_group(loadopt, name) -> Self: ...
    def with_expression(loadopt, key, expression) -> Self: ...
    def selectin_polymorphic(loadopt, classes) -> Self: ...
    def baked_lazyload(loadopt, attr) -> Self: ...

class _UnboundLoad(Load):
    path: Any
    local_opts: Any
    def __init__(self) -> None: ...

class loader_option:
    name: str
    # The first parameter of this Callable should always be `loadopt: Load`
    fn: Callable[..., loader_option]
    def __call__(self, fn: Callable[..., loader_option]) -> Self: ...

# loader_option instances that can be used to dynamically add methods to Load at runtime
@loader_option()
def contains_eager(loadopt: Load, attr, alias: Incomplete | None = ...) -> loader_option: ...
@loader_option()
def load_only(loadopt: Load, *attrs) -> loader_option: ...
@loader_option()
def joinedload(loadopt, attr, innerjoin=None): ...
@loader_option()
def subqueryload(loadopt: Load, attr) -> loader_option: ...
@loader_option()
def selectinload(loadopt: Load, attr) -> loader_option: ...
@loader_option()
def lazyload(loadopt: Load, attr) -> loader_option: ...
@loader_option()
def immediateload(loadopt: Load, attr) -> loader_option: ...
@loader_option()
def noload(loadopt: Load, attr) -> loader_option: ...
@loader_option()
def raiseload(loadopt: Load, attr, sql_only: bool = ...) -> loader_option: ...
@loader_option()
def defaultload(loadopt: Load, attr) -> loader_option: ...
@loader_option()
def defer(loadopt: Load, key, raiseload: bool = ...) -> loader_option: ...
@loader_option()
def undefer(loadopt: Load, key) -> loader_option: ...
@loader_option()
def undefer_group(loadopt: Load, name) -> loader_option: ...
@loader_option()
def with_expression(loadopt: Load, key) -> loader_option: ...
@loader_option()
def selectin_polymorphic(loadopt: Load, classes) -> loader_option: ...
