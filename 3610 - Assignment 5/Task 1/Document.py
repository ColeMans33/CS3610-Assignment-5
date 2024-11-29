from abc import ABC, abstractmethod
class Document(ABC):

  @staticmethod
  @abstractmethod
  def create() -> None:
    pass
