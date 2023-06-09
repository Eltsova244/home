from _typeshed import Incomplete
from typing import Any, Generic, TypeVar

from ..orm.query import Query
from ..orm.session import Session

_T = TypeVar("_T")

class ShardedQuery(Query[_T], Generic[_T]):
    id_chooser: Any
    query_chooser: Any
    execute_chooser: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def set_shard(self, shard_id): ...

class ShardedSession(Session):
    shard_chooser: Any
    id_chooser: Any
    execute_chooser: Any
    query_chooser: Any
    def __init__(
        self,
        shard_chooser,
        id_chooser,
        execute_chooser: Incomplete | None = None,
        shards: Incomplete | None = None,
        query_cls=...,
        **kwargs,
    ): ...
    def connection_callable(
        self, mapper: Incomplete | None = None, instance: Incomplete | None = None, shard_id: Incomplete | None = None, **kwargs
    ): ...
    def get_bind(self, mapper: Incomplete | None = None, shard_id: Incomplete | None = None, instance: Incomplete | None = None, clause: Incomplete | None = None, **kw): ...  # type: ignore[override]
    def bind_shard(self, shard_id, bind) -> None: ...
