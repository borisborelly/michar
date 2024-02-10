from dataclasses import dataclass, asdict
from logging import Logger
from michar.api.util import get_logger
import json
import abc
from tabulate import tabulate

log: Logger = get_logger("legistar")


@dataclass
class Record(object):
    id: int = None
    name: str = None

    @property
    def dict(self) -> dict:
        return asdict(self)

    @property
    def json(self) -> dict:
        return json.dumps(self.dict, indent=4)

    @property
    def markdown(self) -> str:
        return tabulate(self.json, tablefmt="pipe")

    @abc.abstractclassmethod
    def from_dict(self, data: dict) -> "Record":
        pass


@dataclass
class Matter(Record):

    def from_dict(self, data: dict) -> "Matter":
        self.id = data["MatterId"]
        self.name = data["MatterName"]
        return self


@dataclass
class Event(Record):
    location: str = None
    time: str = None
    date: str = None

    def from_dict(self, data: dict) -> "Event":
        self.id = data["EventId"]
        self.name = data["EventBodyName"]
        self.location = data["EventLocation"]
        self.time = data["EventTime"]
        self.date = data["EventDate"]
        return self
