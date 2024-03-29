import toml
import json
from dataclasses import dataclass
import michar.api.config as CFGPKG
from michar.api.util import get_logger
import importlib.resources

log = get_logger("config")

CONFIG_PATH: str = CFGPKG.__package__
CONFIG_NAME: str = "config.toml"


@dataclass
class ConfigProfile(object):
    """
    Michars Configuration Profile
    """

    _config: dict = None

    def __post_init__(self):
        log.debug(f"Loading michar config from {CONFIG_PATH}")
        libs = importlib.resources.files(f"{CONFIG_PATH}")

        self._config = toml.load(f"{libs}/{CONFIG_NAME}")
        log.debug(self.config)

    @property
    def config(self) -> dict:
        return json.dumps(self._config, indent=4)

    def _sources(self) -> dict:
        return self._config["env"]["sources"]

    @property
    def sources(self) -> list:
        return list(self._sources())

    def get_source_url(self, source: str) -> str:
        url: str = self._sources()[source]["url"]
        log.debug(f"Found {url=} for {source=}")
        return url
