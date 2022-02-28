import configparser

config = configparser.ConfigParser()
config.read('config.ini')

project_dir = config['Directory']['ProjectDir']
game_content_dir = config['Directory']['Sims4GameContentDir']
mods_dir = config['Directory']['Sims4ModDir']
project_game_zip_dir = project_dir + '/game/zip'
project_game_unzip_dir = project_dir + '/game/unzip'
project_game_decompile_dir = project_dir + '/game/decompile'
game_content_python = game_content_dir + '/Python'
# for windows
# game_content_python = game_content_dir + '/Game/Bin/Python'
game_content_gameplay = game_content_dir + '/Data/Simulation/Gameplay'
project_game_python = '/python'
project_game_gameplay = '/gameplay'
project_build_dir = project_dir + '/build'
project_build_compile_dir = project_build_dir + '/compile'
project_src_dir = project_dir + '/src'

uncompyle6 = config['Dependency']['Uncompyle6Path']
mod_name = config['Mod']['Name']
