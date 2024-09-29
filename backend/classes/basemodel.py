from abc import ABC, abstractmethod

class basemodel():
    @abstractmethod
    def get_header(self):
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def predict(self):
        pass

    @abstractmethod
    def format_results(self):
        pass

    @abstractmethod
    def get_results(self):
        pass
