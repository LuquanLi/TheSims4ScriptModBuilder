import fnmatch
import os
import py_compile
import shutil
import string
from pathlib import Path
from zipfile import PyZipFile, ZIP_STORED

from utils.constants import *
from utils.utils import prepare_directory


def compile_py(src: string, dest: string):
    # Compile the mod
    for root, dirs, files in os.walk(src):
        for filename in fnmatch.filter(files, '*.py'):
            src_py = root + '/' + filename
            relative_path = str(Path(root).relative_to(src))
            desc_path = dest + '/' + relative_path
            compile_pyc = desc_path + '/' + filename.replace('.py', '.pyc')

            py_compile.compile(src_py, compile_pyc)


def zip_ts4script(src: string):
    # zip
    zip_mod_file = mod_name + '.ts4script'
    compiled_mod = PyZipFile(project_build_dir + '/' + zip_mod_file, mode='w', compression=ZIP_STORED, allowZip64=True,
                             optimize=2)
    for root, dirs, files in os.walk(src):
        relative_path = str(Path(root).relative_to(src))
        for file in files:
            compiled_mod.write(os.path.join(root, file), relative_path + '/' + file)
    compiled_mod.close()

    return zip_mod_file


def start_compile():
    my_game_mod_dir = mods_dir + '/' + mod_name

    prepare_directory(project_build_dir)
    prepare_directory(project_build_compile_dir)
    prepare_directory(my_game_mod_dir)

    compile_py(project_src_dir, project_build_compile_dir)
    zip_mod_file = zip_ts4script(project_build_compile_dir)

    # Copy it over to the mods folder
    shutil.copyfile(project_build_dir + '/' + zip_mod_file, my_game_mod_dir + '/' + zip_mod_file)


start_compile()
