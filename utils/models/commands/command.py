from abc import ABC, abstractmethod


class Command(ABC):

    # выполнение команды
    @abstractmethod
    def execute(self, data):
        pass

    # сообщение, которое выведет команда с началом работы
    @property
    def message(self) -> str:
        pass

    # ключевое слово по которому мы поймем что нужно выполнить данную команду
    @property
    def key_word(self) -> str:
        pass

    # булевская переменная для того что бы показать нужно ли дальше работать с этой командой или она выполнена
    @property
    def is_script(self) -> bool:
        pass

    # получить меню для телеграм бота
    @property
    def get_menu(self):
        pass
