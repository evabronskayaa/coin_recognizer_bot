from utils.models.commands.command import Command
from utils.models.commands.credit_command import CreditCommand
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


def get_commands(bot, char_id) -> list[Command]:
    """Function for get all commands"""
    return [FollowCommand(bot, char_id), HistoryCommand(char_id), OtherSearch(char_id),
            MoneySearch(char_id), CheckBalance(char_id), HelpCommand(char_id)] + \
           [ShapeSearch(figure, char_id) for figure in figures]


def get_command(text, bot,chat_id):
    """Get command for text"""
    for command in get_commands(bot, chat_id):
        if text.lower() == command.key_word.lower():
            return command
    return NothingCommand(chat_id)
