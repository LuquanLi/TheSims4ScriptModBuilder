import fnmatch
import os
import shutil
import py_compile
from zipfile import PyZipFile, ZIP_STORED
from pathlib import Path
from constants import *
from utils import prepare_directory


def compile_src():
    my_game_mod_dir = mods_dir + '/' + mod_name

    prepare_directory(project_build_dir)
    prepare_directory(project_build_compile_dir)
    prepare_directory(my_game_mod_dir)

    # Compile the mod
    for root, dirs, files in os.walk(project_src_dir):
        for filename in fnmatch.filter(files, '*.py'):
            src_py = root + '/' + filename
            relative_path = str(Path(root).relative_to(project_src_dir))
            desc_path = project_build_compile_dir + '/' + relative_path
            compile_pyc = desc_path + '/' + filename.replace('.py', '.pyc')

            py_compile.compile(src_py, compile_pyc)

    # zip
    zip_mod_file = mod_name + '.ts4script'
    compiled_mod = PyZipFile(project_build_dir + '/' + zip_mod_file, mode='w', compression=ZIP_STORED, allowZip64=True, optimize=2)
    for root, dirs, files in os.walk(project_build_compile_dir):
        relative_path = str(Path(root).relative_to(project_build_compile_dir))
        for file in files:
            compiled_mod.write(os.path.join(root, file), relative_path + '/' + file)
    compiled_mod.close()

    # Copy it over to the mods folder
    shutil.copyfile(project_build_dir + '/' + zip_mod_file, my_game_mod_dir + '/' + zip_mod_file)


compile_src()