import services
import sims4.commands
from protocolbuffers import Consts_pb2


# Money
@sims4.commands.Command('add_money', command_type=(sims4.commands.CommandType.Live))
def add_money(amount: int = 0, _connection=None):
    tgt_client = services.client_manager().get(_connection)
    output = sims4.commands.CheatOutput(_connection)

    modify_fund_helper(amount, Consts_pb2.TELEMETRY_MONEY_CHEAT, tgt_client.active_sim)

    output("Add ${0}".format(amount))


@sims4.commands.Command('remove_money', command_type=(sims4.commands.CommandType.Live))
def remove_money(amount: int = 0, _connection=None):
    tgt_client = services.client_manager().get(_connection)
    output = sims4.commands.CheatOutput(_connection)
    current_amount = tgt_client.active_sim.family_funds.money

    # if the amount is higher than family fund, only clear up the family fund
    is_amount_overflow = amount > current_amount
    remove_amount = current_amount if is_amount_overflow else amount

    modify_fund_helper(-remove_amount, Consts_pb2.TELEMETRY_MONEY_CHEAT, tgt_client.active_sim)

    if is_amount_overflow:
        output("Current family fund is not enough")

    output("Remove ${0}".format(remove_amount))


def modify_fund_helper(amount, reason, sim):
    if amount > 0:
        sim.family_funds.add(amount, reason, sim)
    else:
        sim.family_funds.try_remove(-amount, reason, sim)
