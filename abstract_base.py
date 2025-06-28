# abstract_base.py
from abc import ABC, abstractmethod

class BaseAnalysis(ABC):
    @abstractmethod
    def run_analysis(self):
        pass

