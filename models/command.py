from abc import ABC, abstractmethod

def get_command(text):
    if 'распознать' in text.lower():
        last_word = text.split(' ')[-1]
    else



class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class ShapeSearch(Command):
    def execute(self):
        pass