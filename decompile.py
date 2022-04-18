import fnmatch
import multiprocessing
import os
import shutil
import string
import threading
from pathlib import Path
from subprocess import run
from zipfile import PyZipFile
from utils.constants import *
from utils.utils import create_directory, prepare_directory
from multiprocessing import Pool


# copy the zip files
def copy_zip(src: string, dest: string):
    shutil.copytree(src, dest)


def unzip(src: string, dest: string):
    for file in os.listdir(src):
        if file.endswith('.zip'):
            PyZipFile(src + '/' + file).extractall(dest + '/' + file.title().split('.')[0].lower())


def decompile_worker(args):
    dest_path, src_file = args
    print("Decompiling %s" % src_file)
    rv = run([uncompyle6, "-o", dest_path, src_file], text=True,
             capture_output=True)
    print("Done %s" % src_file)
    return [rv.returncode, rv.stderr]


def decompile(src: string):
    print('start decompiling ' + src)

    # total = 0
    # success = 0
    todo = []

    for root, dirs, files in os.walk(src):
        for filename in fnmatch.filter(files, "*.pyc"):
            # print('.', end='') if success % 30 or success == 0 else print('.')  # next line
            # total += 1

            src_file_path = str(os.path.join(root, filename))
            relative_path = str(Path(root).relative_to(project_game_unzip_dir))
            desc_path = project_game_decompile_dir + '/' + relative_path

            target_file_name = filename.replace('.pyc', '.py')
            todo.append([desc_path + "/" + target_file_name, src_file_path])

    with Pool(num_decompilers) as pool:
        rv = pool.map(decompile_worker, todo)

    total = len(todo)
    success = sum([1 for x in rv if x[0] == 0 and not x[1]])

    print('success rate: ' + str(round((success * 100) / total, 2)) + '%')


def copy_files_and_unzip():
    # The Sims 4.app/Contents/Python generated.zip
    # The Sims 4.app/Contents/Data/Simulation/Gameplay -> base.zip, core.zip, simulation.zip
    prepare_directory(project_game_zip_dir)
    copy_zip(game_content_python, project_game_zip_dir + project_game_python)
    copy_zip(game_content_gameplay, project_game_zip_dir + project_game_gameplay)

    prepare_directory(project_game_unzip_dir)
    unzip(project_game_zip_dir + project_game_python, project_game_unzip_dir)
    unzip(project_game_zip_dir + project_game_gameplay, project_game_unzip_dir)


def run_decompile():
    for folder in [project_game_unzip_dir + '/' + x for x in os.listdir(project_game_unzip_dir)]:
        decompile(folder)


def prepare():
    done = False
    while not done:
        try:
            create_directory(project_dir + '/game')
            copy_files_and_unzip()

            prepare_directory(project_game_decompile_dir)
        except PermissionError:
            continue
        done = True
    return


if __name__ == '__main__':
    multiprocessing.freeze_support()
    prepare()
    run_decompile()
