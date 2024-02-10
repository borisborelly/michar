from dataclasses import dataclass, asdict
from logging import Logger
from michar.api.util import get_logger
import json

log: Logger = get_logger("legistar")


@dataclass
class Record(object):
    id: int

    @property
    def dict(self) -> dict:
        return asdict(self)

    @property
    def json(self) -> dict:
        return json.dumps(self.dict, indent=4)


@dataclass
class Matter(Record):
    mat: str


@dataclass
class Event(Record):
    evt: str
