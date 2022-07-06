from utils.models.commands.command import Command
from utils.models.commands.money_search import MoneySearch
from utils.models.commands.check_balance import CheckBalance
from utils.models.commands.follow_command import FollowCommand
from utils.models.commands.history_command import HistoryCommand
from utils.models.commands.nothing_command import NothingCommand
from utils.models.commands.other_search import OtherSearch
from utils.models.commands.shape_search import ShapeSearch
from utils.models.commands.help_command import HelpCommand
from utils.models.commands.boost_command import BoostCommand
from utils.models.commands.stat_command import StatCommand
from utils.models.commands.reduce_command import ReduceCommand
from utils.models.figure import figures


def get_commands() -> list[Command]:
    """Function for get all commands"""
    return [FollowCommand(), HistoryCommand(), OtherSearch(),
            MoneySearch(), CheckBalance(), HelpCommand(),
            BoostCommand(), StatCommand(), ReduceCommand()] + \
           [ShapeSearch(figure) for figure in figures]


def get_command(text):
    """Get command for text"""
    for command in get_commands():
        if text.lower() == command.key_word.lower():
            return command
    return NothingCommand()


def first_execure(text, user):
    """Execute command not according to the script"""
    command = get_command(text)
    command.execute(user)
    return command