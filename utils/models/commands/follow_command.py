from utils.models.commands.command import Command


class FollowCommand(Command):
    """Command for get follow images"""

    def execute(self, data):
        pass
        # todo print follows

    @Command.message.getter
    def message(self):
        return 'FollowCommand'

    @Command.key_word.getter
    def key_word(self):
        return "избранное"

    @Command.is_script.getter
    def is_script(self) -> bool:
        return False