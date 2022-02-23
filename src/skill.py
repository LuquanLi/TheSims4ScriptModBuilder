import string

import services
import sims4.commands
import statistics.skill
from server_commands.argument_helpers import TunableInstanceParam


def get_skill_type(skill: string) -> TunableInstanceParam(sims4.resources.Types.STATISTIC):
    skill_map = {
        "singing": "Major_Singing",
        "herbalism": "Major_Herbalism",
        "baking": "Major_Baking",
        "charisma": "Major_Charisma",
        "comedy": "Major_Comedy",
        "cooking": "Major_HomestyleCooking",
        "dancing": "Minor_Dancing",
        "djmixing": "Major_DJMixing",
        "fishing": "Major_Fishing",
        "fitness": "Skill_Fitness",
        "gardening": "Major_Gardening",
        "gourmetcooking": "Major_GourmetCooking",
        "guitar": "Major_Guitar",
        "handiness": "Major_Handiness",
        "logic": "Major_Logic",
        "mischief": "Major_Mischief",
        "bartending": "Major_Bartending",
        "painting": "Major_Painting",
        "photography": "Major_Photography",
        "piano": "Major_Piano",
        "programming": "Major_Programming",
        "rocketscience": "Major_RocketScience",
        "videogaming": "Major_VideoGaming",
        "violin": "Major_Violin",
        "wellness": "Major_Wellness",
        "writing": "Major_Writing",
        "creativity": "Skill_Child_Creativity",
        "mental": "Skill_Child_Mental",
        "motor": "Skill_Child_Motor",
        "social": "Skill_Child_Social",
        "imagination": "Toddler_Imagination",
        "communication": "Toddler_Communication",
        "movement": "Toddler_Movement",
        "potty": "Toddler_Potty",
        "thinking": "Toddler_Thinking",
        "bowling": "Skill_Bowling",
        "parenting": "Skill_Parenting",
        "dogtraining": "Skill_DogTraining",
        "veterinarian": "Major_Veterinarian",
        "archaeology": "Major_Archaeology",
        "localculture": "Minor_LocalCulture",
        "skating": "Hidden_Skating",
        "flowerarranging": "AdultMajor_FlowerArranging",
    }
    return TunableInstanceParam(sims4.resources.Types.STATISTIC)(skill_map[skill])


# skill
# stat_type: TunableInstanceParam(sims4.resources.Types.STATISTIC)
@sims4.commands.Command('max_skill', command_type=(sims4.commands.CommandType.Live),
                        console_type=(sims4.commands.CommandType.Cheat))
def max_skill(search_string=None, _connection=None):
    tgt_client = services.client_manager().get(_connection)
    sim = tgt_client.active_sim

    stat_type = get_skill_type(search_string.lower())
    stat = sim.commodity_tracker.get_statistic(stat_type)

    if stat is None:
        stat = sim.commodity_tracker.add_statistic(stat_type)
        if stat is None:
            return

    if not isinstance(stat, statistics.skill.Skill):
        return

    sim.commodity_tracker.set_user_value(stat_type, stat_type.max_level)
