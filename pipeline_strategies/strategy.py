from abc import ABC, abstractmethod

class Strategy(ABC):
    """
    Interface for all the strategies within the different stages of the pipeline.
    """
    name: str
    id: int
    
    @abstractmethod
    def execute():
        raise NotImplementedError