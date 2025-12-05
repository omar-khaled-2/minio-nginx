import os
from abc import ABC, abstractmethod


class Secret(ABC):
    @abstractmethod
    def get(self) -> str:
        pass


class DockerSecret(Secret):

    def __init__(self):
        self._cache = {}
        

    def get(self, name: str) -> str:
        if name in self._cache:
            return self._cache[name]
        if os.path.exists(f"/run/secrets/{name}"):
            with open(f"/run/secrets/{name}") as f:
                self._cache[name] = f.read().strip()
                return self._cache[name]

        raise RuntimeError(f"Secret '{name}' not found in Docker secrets")
 

secret = DockerSecret()