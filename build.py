import os
import sys
import shutil
import subprocess

BUILD_DIR = "build"

def tool_exists(tool):
    return shutil.which(tool) is not None

def build():
    if not os.path.exists('build'):
        os.mkdir('build')
    os.chdir('build')
    if not tool_exists('cmake'):
        print('CMake not found')
        sys.exit(1)
    if not tool_exists('make'):
        print('Make not found')
        sys.exit(1)
    if not tool_exists('ninja'):
        subprocess.run(['cmake', '..'])
        subprocess.run(['make'])
    else:
        subprocess.run(['cmake', '-G Ninja', '..'])
        subprocess.run(['ninja'])

if __name__ == '__main__':
    build()

