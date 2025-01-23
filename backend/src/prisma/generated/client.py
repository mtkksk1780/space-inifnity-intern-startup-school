# -*- coding: utf-8 -*-
# code generated by Prisma. DO NOT EDIT.
# pyright: reportUnusedImport=false
# fmt: off
from __future__ import annotations

# global imports for type checking
from builtins import bool as _bool
from builtins import int as _int
from builtins import float as _float
from builtins import str as _str
import sys
import decimal
import datetime
from typing import (
    TYPE_CHECKING,
    Optional,
    Iterable,
    Iterator,
    Sequence,
    Callable,
    ClassVar,
    NoReturn,
    TypeVar,
    Generic,
    Mapping,
    Tuple,
    Union,
    List,
    Dict,
    Type,
    Any,
    Set,
    overload,
    cast,
)
from typing_extensions import TypedDict, Literal


LiteralString = str
# -- template client.py.jinja --
import warnings
import logging
from datetime import timedelta
from pathlib import Path
from types import TracebackType
from typing_extensions import override

from pydantic import BaseModel

from . import types, models, errors, actions
from ._base_client import BasePrisma, UseClientDefault, USE_CLIENT_DEFAULT
from .types import DatasourceOverride, HttpConfig, MetricsFormat
from ._types import BaseModelT, PrismaMethod, TransactionId, Datasource
from .bases import _PrismaModel
from ._builder import QueryBuilder, dumps
from .generator.models import EngineType, OptionalValueFromEnvVar, BinaryPaths
from ._compat import removeprefix, model_parse
from ._constants import CREATE_MANY_SKIP_DUPLICATES_UNSUPPORTED, DEFAULT_CONNECT_TIMEOUT, DEFAULT_TX_MAX_WAIT, DEFAULT_TX_TIMEOUT
from ._raw_query import deserialize_raw_results
from ._metrics import Metrics
from .metadata import PRISMA_MODELS, RELATIONAL_FIELD_MAPPINGS
from ._transactions import AsyncTransactionManager, SyncTransactionManager

# re-exports
from ._base_client import SyncBasePrisma, AsyncBasePrisma, load_env as load_env
from ._registry import (
    register as register,
    get_client as get_client,
    RegisteredClient as RegisteredClient,
)


__all__ = (
    'ENGINE_TYPE',
    'SCHEMA_PATH',
    'BINARY_PATHS',
    'Batch',
    'Prisma',
    'Client',
    'load_env',
    'register',
    'get_client',
)

log: logging.Logger = logging.getLogger(__name__)

# [ADD] Add the path to the schema.prisma file and the binary paths
root_path = Path(__file__).parent.parent
SCHEMA_PATH = root_path / 'schema.prisma'
PACKAGED_SCHEMA_PATH = root_path / 'schema.prisma'
BINARY_PATHS = model_parse(BinaryPaths, {
    'queryEngine': {
        'darwin': str(root_path / 'query-engine-darwin')
    },
    'introspectionEngine': {},
    'migrationEngine': {},
    'libqueryEngine': {},
    'prismaFmt': {}
})
print("BINARY_PATHS", BINARY_PATHS)
ENGINE_TYPE: EngineType = EngineType.binary

# SCHEMA_PATH = Path('/Users/masatotakakusaki/Project/Group/Tenatch/space-infinity-intern-startup-school/backend/src/prisma/schema.prisma')
# PACKAGED_SCHEMA_PATH = Path(__file__).parent.joinpath('schema.prisma')
# ENGINE_TYPE: EngineType = EngineType.binary
# BINARY_PATHS = model_parse(BinaryPaths, {'queryEngine': {'darwin': '/Users/masatotakakusaki/.cache/prisma-python/binaries/5.17.0/393aa359c9ad4a4bb28630fb5613f9c281cde053/node_modules/prisma/query-engine-darwin'}, 'introspectionEngine': {}, 'migrationEngine': {}, 'libqueryEngine': {}, 'prismaFmt': {}})


class Prisma(AsyncBasePrisma):
    # Note: these property names can be customised using `/// @Python(instance_name: '...')`
    # https://prisma-client-py.readthedocs.io/en/stable/reference/schema-extensions/#instance_name
    message: 'actions.MessageActions[models.Message]'
    user: 'actions.UserActions[models.User]'
    project: 'actions.ProjectActions[models.Project]'
    submission: 'actions.SubmissionActions[models.Submission]'
    feedback: 'actions.FeedbackActions[models.Feedback]'

    __slots__ = (
        'message',
        'user',
        'project',
        'submission',
        'feedback',
    )

    def __init__(
        self,
        *,
        use_dotenv: bool = True,
        log_queries: bool = False,
        auto_register: bool = False,
        datasource: DatasourceOverride | None = None,
        connect_timeout: int | timedelta = DEFAULT_CONNECT_TIMEOUT,
        http: HttpConfig | None = None,
    ) -> None:
        super().__init__(
            http=http,
            use_dotenv=use_dotenv,
            log_queries=log_queries,
            datasource=datasource,
            connect_timeout=connect_timeout,
        )
        self._set_generated_properties(
            schema_path=SCHEMA_PATH,
            engine_type=ENGINE_TYPE,
            prisma_models=PRISMA_MODELS,
            packaged_schema_path=PACKAGED_SCHEMA_PATH,
            relational_field_mappings=RELATIONAL_FIELD_MAPPINGS,
            preview_features=set([]),
            active_provider='postgresql',
            default_datasource_name='db',
        )

        self.message = actions.MessageActions[models.Message](self, models.Message)
        self.user = actions.UserActions[models.User](self, models.User)
        self.project = actions.ProjectActions[models.Project](self, models.Project)
        self.submission = actions.SubmissionActions[models.Submission](self, models.Submission)
        self.feedback = actions.FeedbackActions[models.Feedback](self, models.Feedback)

        if auto_register:
            register(self)

    @property
    @override
    def _default_datasource(self) -> Datasource:
        return {
            'name': 'db',
            'url': OptionalValueFromEnvVar(**{'value': None, 'fromEnvVar': 'DATABASE_URL'}).resolve(),
            'source_file_path': '/Users/masatotakakusaki/Project/Group/Tenatch/space-infinity-intern-startup-school/backend/src/prisma/schema.prisma',
        }

    async def execute_raw(self, query: LiteralString, *args: Any) -> int:
        resp = await self._execute(
            method='execute_raw',
            arguments={
                'query': query,
                'parameters': args,
            },
            model=None,
        )
        return int(resp['data']['result'])

    @overload
    async def query_first(
        self,
        query: LiteralString,
        *args: Any,
    ) -> dict[str, Any]:
        ...

    @overload
    async def query_first(
        self,
        query: LiteralString,
        *args: Any,
        model: Type[BaseModelT],
    ) -> Optional[BaseModelT]:
        ...

    async def query_first(
        self,
        query: LiteralString,
        *args: Any,
        model: Optional[Type[BaseModelT]] = None,
    ) -> Union[Optional[BaseModelT], dict[str, Any]]:
        """This function is the exact same as `query_raw()` but returns the first result.

        If model is given, the returned record is converted to the pydantic model first,
        otherwise a raw dictionary will be returned.
        """
        results: Sequence[Union[BaseModelT, dict[str, Any]]]
        if model is not None:
            results = await self.query_raw(query, *args, model=model)
        else:
            results = await self.query_raw(query, *args)

        if not results:
            return None

        return results[0]

    @overload
    async def query_raw(
        self,
        query: LiteralString,
        *args: Any,
    ) -> List[dict[str, Any]]:
        ...

    @overload
    async def query_raw(
        self,
        query: LiteralString,
        *args: Any,
        model: Type[BaseModelT],
    ) -> List[BaseModelT]:
        ...

    async def query_raw(
        self,
        query: LiteralString,
        *args: Any,
        model: Optional[Type[BaseModelT]] = None,
    ) -> Union[List[BaseModelT], List[dict[str, Any]]]:
        """Execute a raw SQL query against the database.

        If model is given, each returned record is converted to the pydantic model first,
        otherwise results will be raw dictionaries.
        """
        resp = await self._execute(
            method='query_raw',
            arguments={
                'query': query,
                'parameters': args,
            },
            model=model,
        )
        result = resp['data']['result']
        if model is not None:
            return deserialize_raw_results(result, model=model)

        return deserialize_raw_results(result)

    def batch_(self) -> Batch:
        """Returns a context manager for grouping write queries into a single transaction."""
        return Batch(client=self)

    def tx(
        self,
        *,
        max_wait: Union[int, timedelta] = DEFAULT_TX_MAX_WAIT,
        timeout: Union[int, timedelta] = DEFAULT_TX_TIMEOUT,
    ) -> TransactionManager:
        """Returns a context manager for executing queries within a database transaction.

        Entering the context manager returns a new Prisma instance wrapping all
        actions within a transaction, queries will be isolated to the Prisma instance and
        will not be commited to the database until the context manager exits.

        By default, Prisma will wait a maximum of 2 seconds to acquire a transaction from the database. You can modify this
        default with the `max_wait` argument which accepts a value in milliseconds or `datetime.timedelta`.

        By default, Prisma will cancel and rollback ay transactions that last longer than 5 seconds. You can modify this timeout
        with the `timeout` argument which accepts a value in milliseconds or `datetime.timedelta`.

        Example usage:

        ```py
        async with client.tx() as transaction:
            user1 = await client.user.create({'name': 'Robert'})
            user2 = await client.user.create({'name': 'Tegan'})
        ```

        In the above example, if the first database call succeeds but the second does not then neither of the records will be created.
        """
        return TransactionManager(
            client=self,
            max_wait=max_wait,
            timeout=timeout,
        )


TransactionManager = AsyncTransactionManager[Prisma]


# TODO: this should return the results as well
# TODO: don't require copy-pasting arguments between actions and batch actions
class Batch:
    message: 'MessageBatchActions'
    user: 'UserBatchActions'
    project: 'ProjectBatchActions'
    submission: 'SubmissionBatchActions'
    feedback: 'FeedbackBatchActions'

    def __init__(self, client: Prisma) -> None:
        self.__client = client
        self.__queries: List[str] = []
        self._active_provider = client._active_provider
        self.message = MessageBatchActions(self)
        self.user = UserBatchActions(self)
        self.project = ProjectBatchActions(self)
        self.submission = SubmissionBatchActions(self)
        self.feedback = FeedbackBatchActions(self)

    def _add(self, **kwargs: Any) -> None:
        builder = QueryBuilder(
            **kwargs,
            prisma_models=PRISMA_MODELS,
            relational_field_mappings=RELATIONAL_FIELD_MAPPINGS,
        )
        self.__queries.append(builder.build_query())

    async def commit(self) -> None:
        """Execute the queries"""
        # TODO: normalise this, we should still call client._execute
        queries = self.__queries
        self.__queries = []

        payload = {
            'batch': [
                {
                    'query': query,
                    'variables': {},
                }
                for query in queries
            ],
            'transaction': True,
        }
        await self.__client._engine.query(
            dumps(payload),
            tx_id=self.__client._tx_id,
        )

    def execute_raw(self, query: LiteralString, *args: Any) -> None:
        self._add(
            method='execute_raw',
            arguments={
                'query': query,
                'parameters': args,
            }
        )

    async def __aenter__(self) -> 'Batch':
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        if exc is None:
            await self.commit()


# NOTE: some arguments are meaningless in this context but are included
# for completeness sake
class MessageBatchActions:
    def __init__(self, batcher: Batch) -> None:
        self._batcher = batcher

    def create(
        self,
        data: types.MessageCreateInput,
        include: Optional[types.MessageInclude] = None
    ) -> None:
        self._batcher._add(
            method='create',
            model=models.Message,
            arguments={
                'data': data,
                'include': include,
            },
        )

    def create_many(
        self,
        data: List[types.MessageCreateWithoutRelationsInput],
        *,
        skip_duplicates: Optional[bool] = None,
    ) -> None:
        if skip_duplicates and self._batcher._active_provider in CREATE_MANY_SKIP_DUPLICATES_UNSUPPORTED:
            raise errors.UnsupportedDatabaseError(self._batcher._active_provider, 'create_many_skip_duplicates')

        self._batcher._add(
            method='create_many',
            model=models.Message,
            arguments={
                'data': data,
                'skipDuplicates': skip_duplicates,
            },
            root_selection=['count'],
        )

    def delete(
        self,
        where: types.MessageWhereUniqueInput,
        include: Optional[types.MessageInclude] = None,
    ) -> None:
        self._batcher._add(
            method='delete',
            model=models.Message,
            arguments={
                'where': where,
                'include': include,
            },
        )

    def update(
        self,
        data: types.MessageUpdateInput,
        where: types.MessageWhereUniqueInput,
        include: Optional[types.MessageInclude] = None
    ) -> None:
        self._batcher._add(
            method='update',
            model=models.Message,
            arguments={
                'data': data,
                'where': where,
                'include': include,
            },
        )

    def upsert(
        self,
        where: types.MessageWhereUniqueInput,
        data: types.MessageUpsertInput,
        include: Optional[types.MessageInclude] = None,
    ) -> None:
        self._batcher._add(
            method='upsert',
            model=models.Message,
            arguments={
                'where': where,
                'include': include,
                'create': data.get('create'),
                'update': data.get('update'),
            },
        )

    def update_many(
        self,
        data: types.MessageUpdateManyMutationInput,
        where: types.MessageWhereInput,
    ) -> None:
        self._batcher._add(
            method='update_many',
            model=models.Message,
            arguments={'data': data, 'where': where,},
            root_selection=['count'],
        )

    def delete_many(
        self,
        where: Optional[types.MessageWhereInput] = None,
    ) -> None:
        self._batcher._add(
            method='delete_many',
            model=models.Message,
            arguments={'where': where},
            root_selection=['count'],
        )



# NOTE: some arguments are meaningless in this context but are included
# for completeness sake
class UserBatchActions:
    def __init__(self, batcher: Batch) -> None:
        self._batcher = batcher

    def create(
        self,
        data: types.UserCreateInput,
        include: Optional[types.UserInclude] = None
    ) -> None:
        self._batcher._add(
            method='create',
            model=models.User,
            arguments={
                'data': data,
                'include': include,
            },
        )

    def create_many(
        self,
        data: List[types.UserCreateWithoutRelationsInput],
        *,
        skip_duplicates: Optional[bool] = None,
    ) -> None:
        if skip_duplicates and self._batcher._active_provider in CREATE_MANY_SKIP_DUPLICATES_UNSUPPORTED:
            raise errors.UnsupportedDatabaseError(self._batcher._active_provider, 'create_many_skip_duplicates')

        self._batcher._add(
            method='create_many',
            model=models.User,
            arguments={
                'data': data,
                'skipDuplicates': skip_duplicates,
            },
            root_selection=['count'],
        )

    def delete(
        self,
        where: types.UserWhereUniqueInput,
        include: Optional[types.UserInclude] = None,
    ) -> None:
        self._batcher._add(
            method='delete',
            model=models.User,
            arguments={
                'where': where,
                'include': include,
            },
        )

    def update(
        self,
        data: types.UserUpdateInput,
        where: types.UserWhereUniqueInput,
        include: Optional[types.UserInclude] = None
    ) -> None:
        self._batcher._add(
            method='update',
            model=models.User,
            arguments={
                'data': data,
                'where': where,
                'include': include,
            },
        )

    def upsert(
        self,
        where: types.UserWhereUniqueInput,
        data: types.UserUpsertInput,
        include: Optional[types.UserInclude] = None,
    ) -> None:
        self._batcher._add(
            method='upsert',
            model=models.User,
            arguments={
                'where': where,
                'include': include,
                'create': data.get('create'),
                'update': data.get('update'),
            },
        )

    def update_many(
        self,
        data: types.UserUpdateManyMutationInput,
        where: types.UserWhereInput,
    ) -> None:
        self._batcher._add(
            method='update_many',
            model=models.User,
            arguments={'data': data, 'where': where,},
            root_selection=['count'],
        )

    def delete_many(
        self,
        where: Optional[types.UserWhereInput] = None,
    ) -> None:
        self._batcher._add(
            method='delete_many',
            model=models.User,
            arguments={'where': where},
            root_selection=['count'],
        )



# NOTE: some arguments are meaningless in this context but are included
# for completeness sake
class ProjectBatchActions:
    def __init__(self, batcher: Batch) -> None:
        self._batcher = batcher

    def create(
        self,
        data: types.ProjectCreateInput,
        include: Optional[types.ProjectInclude] = None
    ) -> None:
        self._batcher._add(
            method='create',
            model=models.Project,
            arguments={
                'data': data,
                'include': include,
            },
        )

    def create_many(
        self,
        data: List[types.ProjectCreateWithoutRelationsInput],
        *,
        skip_duplicates: Optional[bool] = None,
    ) -> None:
        if skip_duplicates and self._batcher._active_provider in CREATE_MANY_SKIP_DUPLICATES_UNSUPPORTED:
            raise errors.UnsupportedDatabaseError(self._batcher._active_provider, 'create_many_skip_duplicates')

        self._batcher._add(
            method='create_many',
            model=models.Project,
            arguments={
                'data': data,
                'skipDuplicates': skip_duplicates,
            },
            root_selection=['count'],
        )

    def delete(
        self,
        where: types.ProjectWhereUniqueInput,
        include: Optional[types.ProjectInclude] = None,
    ) -> None:
        self._batcher._add(
            method='delete',
            model=models.Project,
            arguments={
                'where': where,
                'include': include,
            },
        )

    def update(
        self,
        data: types.ProjectUpdateInput,
        where: types.ProjectWhereUniqueInput,
        include: Optional[types.ProjectInclude] = None
    ) -> None:
        self._batcher._add(
            method='update',
            model=models.Project,
            arguments={
                'data': data,
                'where': where,
                'include': include,
            },
        )

    def upsert(
        self,
        where: types.ProjectWhereUniqueInput,
        data: types.ProjectUpsertInput,
        include: Optional[types.ProjectInclude] = None,
    ) -> None:
        self._batcher._add(
            method='upsert',
            model=models.Project,
            arguments={
                'where': where,
                'include': include,
                'create': data.get('create'),
                'update': data.get('update'),
            },
        )

    def update_many(
        self,
        data: types.ProjectUpdateManyMutationInput,
        where: types.ProjectWhereInput,
    ) -> None:
        self._batcher._add(
            method='update_many',
            model=models.Project,
            arguments={'data': data, 'where': where,},
            root_selection=['count'],
        )

    def delete_many(
        self,
        where: Optional[types.ProjectWhereInput] = None,
    ) -> None:
        self._batcher._add(
            method='delete_many',
            model=models.Project,
            arguments={'where': where},
            root_selection=['count'],
        )



# NOTE: some arguments are meaningless in this context but are included
# for completeness sake
class SubmissionBatchActions:
    def __init__(self, batcher: Batch) -> None:
        self._batcher = batcher

    def create(
        self,
        data: types.SubmissionCreateInput,
        include: Optional[types.SubmissionInclude] = None
    ) -> None:
        self._batcher._add(
            method='create',
            model=models.Submission,
            arguments={
                'data': data,
                'include': include,
            },
        )

    def create_many(
        self,
        data: List[types.SubmissionCreateWithoutRelationsInput],
        *,
        skip_duplicates: Optional[bool] = None,
    ) -> None:
        if skip_duplicates and self._batcher._active_provider in CREATE_MANY_SKIP_DUPLICATES_UNSUPPORTED:
            raise errors.UnsupportedDatabaseError(self._batcher._active_provider, 'create_many_skip_duplicates')

        self._batcher._add(
            method='create_many',
            model=models.Submission,
            arguments={
                'data': data,
                'skipDuplicates': skip_duplicates,
            },
            root_selection=['count'],
        )

    def delete(
        self,
        where: types.SubmissionWhereUniqueInput,
        include: Optional[types.SubmissionInclude] = None,
    ) -> None:
        self._batcher._add(
            method='delete',
            model=models.Submission,
            arguments={
                'where': where,
                'include': include,
            },
        )

    def update(
        self,
        data: types.SubmissionUpdateInput,
        where: types.SubmissionWhereUniqueInput,
        include: Optional[types.SubmissionInclude] = None
    ) -> None:
        self._batcher._add(
            method='update',
            model=models.Submission,
            arguments={
                'data': data,
                'where': where,
                'include': include,
            },
        )

    def upsert(
        self,
        where: types.SubmissionWhereUniqueInput,
        data: types.SubmissionUpsertInput,
        include: Optional[types.SubmissionInclude] = None,
    ) -> None:
        self._batcher._add(
            method='upsert',
            model=models.Submission,
            arguments={
                'where': where,
                'include': include,
                'create': data.get('create'),
                'update': data.get('update'),
            },
        )

    def update_many(
        self,
        data: types.SubmissionUpdateManyMutationInput,
        where: types.SubmissionWhereInput,
    ) -> None:
        self._batcher._add(
            method='update_many',
            model=models.Submission,
            arguments={'data': data, 'where': where,},
            root_selection=['count'],
        )

    def delete_many(
        self,
        where: Optional[types.SubmissionWhereInput] = None,
    ) -> None:
        self._batcher._add(
            method='delete_many',
            model=models.Submission,
            arguments={'where': where},
            root_selection=['count'],
        )



# NOTE: some arguments are meaningless in this context but are included
# for completeness sake
class FeedbackBatchActions:
    def __init__(self, batcher: Batch) -> None:
        self._batcher = batcher

    def create(
        self,
        data: types.FeedbackCreateInput,
        include: Optional[types.FeedbackInclude] = None
    ) -> None:
        self._batcher._add(
            method='create',
            model=models.Feedback,
            arguments={
                'data': data,
                'include': include,
            },
        )

    def create_many(
        self,
        data: List[types.FeedbackCreateWithoutRelationsInput],
        *,
        skip_duplicates: Optional[bool] = None,
    ) -> None:
        if skip_duplicates and self._batcher._active_provider in CREATE_MANY_SKIP_DUPLICATES_UNSUPPORTED:
            raise errors.UnsupportedDatabaseError(self._batcher._active_provider, 'create_many_skip_duplicates')

        self._batcher._add(
            method='create_many',
            model=models.Feedback,
            arguments={
                'data': data,
                'skipDuplicates': skip_duplicates,
            },
            root_selection=['count'],
        )

    def delete(
        self,
        where: types.FeedbackWhereUniqueInput,
        include: Optional[types.FeedbackInclude] = None,
    ) -> None:
        self._batcher._add(
            method='delete',
            model=models.Feedback,
            arguments={
                'where': where,
                'include': include,
            },
        )

    def update(
        self,
        data: types.FeedbackUpdateInput,
        where: types.FeedbackWhereUniqueInput,
        include: Optional[types.FeedbackInclude] = None
    ) -> None:
        self._batcher._add(
            method='update',
            model=models.Feedback,
            arguments={
                'data': data,
                'where': where,
                'include': include,
            },
        )

    def upsert(
        self,
        where: types.FeedbackWhereUniqueInput,
        data: types.FeedbackUpsertInput,
        include: Optional[types.FeedbackInclude] = None,
    ) -> None:
        self._batcher._add(
            method='upsert',
            model=models.Feedback,
            arguments={
                'where': where,
                'include': include,
                'create': data.get('create'),
                'update': data.get('update'),
            },
        )

    def update_many(
        self,
        data: types.FeedbackUpdateManyMutationInput,
        where: types.FeedbackWhereInput,
    ) -> None:
        self._batcher._add(
            method='update_many',
            model=models.Feedback,
            arguments={'data': data, 'where': where,},
            root_selection=['count'],
        )

    def delete_many(
        self,
        where: Optional[types.FeedbackWhereInput] = None,
    ) -> None:
        self._batcher._add(
            method='delete_many',
            model=models.Feedback,
            arguments={'where': where},
            root_selection=['count'],
        )



Client = Prisma