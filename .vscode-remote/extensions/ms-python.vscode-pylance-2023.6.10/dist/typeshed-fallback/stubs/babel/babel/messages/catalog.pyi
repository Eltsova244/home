import datetime
from collections import OrderedDict
from collections.abc import Generator, Iterable, Iterator
from typing_extensions import TypeAlias

from babel.core import Locale

__all__ = ["Message", "Catalog", "TranslationError"]

_MessageID: TypeAlias = str | tuple[str, ...] | list[str]

class Message:
    id: _MessageID
    string: _MessageID
    locations: list[tuple[str, int]]
    flags: set[str]
    auto_comments: list[str]
    user_comments: list[str]
    previous_id: list[str]
    lineno: int | None
    context: str | None
    def __init__(
        self,
        id: str,
        string: str = "",
        locations: Iterable[tuple[str, int]] = (),
        flags: Iterable[str] = (),
        auto_comments: Iterable[str] = (),
        user_comments: Iterable[str] = (),
        previous_id: _MessageID = (),
        lineno: int | None = None,
        context: str | None = None,
    ) -> None: ...
    def __cmp__(self, other: Message) -> int: ...
    def __gt__(self, other: Message) -> bool: ...
    def __lt__(self, other: Message) -> bool: ...
    def __ge__(self, other: Message) -> bool: ...
    def __le__(self, other: Message) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def is_identical(self, other: Message) -> bool: ...
    def clone(self) -> Message: ...
    def check(self, catalog: Catalog | None = None) -> list[TranslationError]: ...
    @property
    def fuzzy(self) -> bool: ...
    @property
    def pluralizable(self) -> bool: ...
    @property
    def python_format(self) -> bool: ...

class TranslationError(Exception): ...

class Catalog:
    domain: str | None
    project: str
    version: str
    copyright_holder: str
    msgid_bugs_address: str
    last_translator: str
    language_team: str
    charset: str
    creation_date: datetime.datetime | str
    revision_date: datetime.datetime | datetime.time | float | str
    fuzzy: bool
    obsolete: OrderedDict[str | tuple[str, str], Message]
    def __init__(
        self,
        locale: str | Locale | None = None,
        domain: str | None = None,
        header_comment: str | None = ...,
        project: str | None = None,
        version: str | None = None,
        copyright_holder: str | None = None,
        msgid_bugs_address: str | None = None,
        creation_date: datetime.datetime | str | None = None,
        revision_date: datetime.datetime | datetime.time | float | str | None = None,
        last_translator: str | None = None,
        language_team: str | None = None,
        charset: str | None = None,
        fuzzy: bool = True,
    ) -> None: ...
    @property
    def locale(self) -> Locale | None: ...
    @locale.setter  # Assigning a string looks up the right Locale object.
    def locale(self, value: Locale | str | None) -> None: ...
    @property
    def locale_identifier(self) -> str | None: ...
    @property
    def header_comment(self) -> str: ...
    @header_comment.setter
    def header_comment(self, value: str) -> None: ...
    @property
    def mime_headers(self) -> list[tuple[str, str]]: ...
    @mime_headers.setter
    def mime_headers(self, value: Iterable[tuple[str | bytes, str | bytes]]) -> None: ...
    @property
    def num_plurals(self) -> int: ...
    @property
    def plural_expr(self) -> str: ...
    @property
    def plural_forms(self) -> str: ...
    def __contains__(self, id: _MessageID) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Message]: ...
    def __delitem__(self, id: _MessageID) -> None: ...
    def __getitem__(self, id: _MessageID) -> Message: ...
    def __setitem__(self, id: _MessageID, message: Message) -> None: ...
    def add(
        self,
        id: _MessageID,
        string: _MessageID | None = None,
        locations: Iterable[tuple[str, int]] = (),
        flags: Iterable[str] = (),
        auto_comments: Iterable[str] = (),
        user_comments: Iterable[str] = (),
        previous_id: _MessageID = (),
        lineno: int | None = None,
        context: str | None = None,
    ) -> Message: ...
    def check(self) -> Generator[tuple[Message, list[TranslationError]], None, None]: ...
    def get(self, id: _MessageID, context: str | None = None): ...
    def delete(self, id, context: str | None = None) -> None: ...
    def update(
        self,
        template: Catalog,
        no_fuzzy_matching: bool = False,
        update_header_comment: bool = False,
        keep_user_comments: bool = True,
    ) -> None: ...
    def is_identical(self, other: Catalog) -> bool: ...
