import services, sims4.commands
from server_commands.argument_helpers import SimInfoParam, TunableInstanceParam


RELATIONSHIP_MAX_SCORE = 100
FRIEND_TYPE = 'LTR_Friendship_Main'
ROMANCE_TYPE = 'LTR_Romance_Main'


# become_friend <FirstName> <LastName>
# the param HAS TO be : info1: SimInfoParam, info2: SimInfoParam
@sims4.commands.Command('become_friend', command_type=(sims4.commands.CommandType.Live))
def become_friend(info1: SimInfoParam, _connection=None):
    tgt_client = services.client_manager().get(_connection)
    output = sims4.commands.CheatOutput(_connection)
    sim = tgt_client.active_sim

    if info1 is None:
        output("target sim not exists")
        return

    sim.relationship_tracker.set_relationship_score(info1.id, RELATIONSHIP_MAX_SCORE, TunableInstanceParam(sims4.resources.Types.STATISTIC)(FRIEND_TYPE))
    output("become friends successfully.")

@sims4.commands.Command('become_lover', command_type=(sims4.commands.CommandType.Live),)
def become_lover(info1: SimInfoParam, _connection=None):
    tgt_client = services.client_manager().get(_connection)
    output = sims4.commands.CheatOutput(_connection)
    sim = tgt_client.active_sim

    if info1 is None:
        output("target sim not exists")
        return

    sim.relationship_tracker.set_relationship_score(info1.id, RELATIONSHIP_MAX_SCORE, TunableInstanceParam(sims4.resources.Types.STATISTIC)(ROMANCE_TYPE))
    output("become lovers successfully.")

@sims4.commands.Command('assign_friend', command_type=(sims4.commands.CommandType.Live))
def assign_friend(info1: SimInfoParam, info2: SimInfoParam, _connection=None):
    output = sims4.commands.CheatOutput(_connection)

    if info1 is None or info2 is None:
        output("at least one of the target sim does not exist")
        return

    info1.relationship_tracker.set_relationship_score(info2.id, RELATIONSHIP_MAX_SCORE, TunableInstanceParam(sims4.resources.Types.STATISTIC)(FRIEND_TYPE))
    output("set friends successfully.")

@sims4.commands.Command('assign_lover', command_type=(sims4.commands.CommandType.Live))
def assign_lover(info1: SimInfoParam, info2: SimInfoParam, _connection=None):
    output = sims4.commands.CheatOutput(_connection)

    if info1 is None or info2 is None:
        output("at least one of the target sim does not exist")
        return

    info1.relationship_tracker.set_relationship_score(info2.id, RELATIONSHIP_MAX_SCORE, TunableInstanceParam(sims4.resources.Types.STATISTIC)(ROMANCE_TYPE))
    output("set lovers successfully.")

