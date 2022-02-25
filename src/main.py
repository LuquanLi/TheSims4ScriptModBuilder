import sims4.commands


@sims4.commands.Command('hello', command_type=sims4.commands.CommandType.Live)
def hello_world(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output("Hello World")


@sims4.commands.Command('cheats_help', command_type=sims4.commands.CommandType.Live)
def hello_world(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output("add_money <amount>: add money to your current sim")
    output("remove_money <amount>: remove money from your current sim")
    output("max_skill <skill name (no space)>: set the skill to max level")
    output("become_friend <firstname> <lastname>: become friend with the target sim")
    output("become_lover <firstname> <lastname>: become lover with the target sim")
