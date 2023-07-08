"""yadoma

Usage:
  yadoma [options] <config>...

Options:
  -h --help            Help screen
  --version            Version
  -v --verbose         Verbose mode
  -f --force-symlink   Force overwrite symlinks
"""

import os

from docopt import docopt
import yaml

from . import __version__ as version

VERBOSE = False
FORCE_SYMLINK = False


class CMDLineExit(Exception):
    pass


class ConfigError(Exception):
    pass


def verbose(message):
    if VERBOSE:
        print(message)


def info(message):
    print(message)


def warn(message):
    print('warn: ' + message)


def link(file_, base_dir, target_dir):
    # decode json
    if isinstance(file_, str):
        src = os.path.abspath(os.path.join(base_dir, file_))
        dest = os.path.expanduser(os.path.join(target_dir, file_))
    else:
        try:
            src = os.path.abspath(os.path.join(base_dir, file_['src']))
        except KeyError:
            raise ConfigError("missing 'src' entry")
        try:
            dest = os.path.expanduser(os.path.join(target_dir, file_['dest']))
        except KeyError:
            dest = os.path.expanduser(os.path.join(target_dir, file_['src']))
    message = "'{0}' --> '{1}': {2}"
    dest_exists = os.path.lexists(dest)

    def print_status(status):
        """Closure to print status."""
        info(message.format(src, dest, status))

    if not dest_exists:
        print_status('does not exist, will link')
        os.symlink(src, dest)

    elif dest_exists and os.path.islink(dest):
        if os.path.realpath(dest) == src:
            print_status('is valid link, doing nothing')
        elif os.path.realpath(dest) != src and not FORCE_SYMLINK:
            print_status('is invalid link, ignoring, use --force-symlink to force')
        elif os.path.realpath(dest) != src and FORCE_SYMLINK:
            print_status('is invalid link, but will link anyway due to --force-symlink')
            os.remove(dest)
            os.symlink(src, dest)

    elif dest_exists and os.path.isfile(dest):
        if not FORCE_SYMLINK:
            print_status('is an existing file, use --force-symlink to force')
        elif FORCE_SYMLINK:
            print_status(
                'is an existing file, but will link anyway due to --force-symlink '
            )
            os.remove(dest)
            os.symlink(src, dest)

    elif dest_exists and os.path.isdir(dest):
        if not FORCE_SYMLINK:
            print_status('is an existing directory, use --force-symlink to force')
        elif FORCE_SYMLINK:
            print_status(
                'is an existing directory, but will link anyway due to --force-symlink '
            )
            os.remove(dest)
            os.symlink(src, dest)

    elif dest_exists and os.path.ismount(dest):
        if not FORCE_SYMLINK:
            print_status('is an existing mount point, use --force-symlink to force')
        elif FORCE_SYMLINK:
            print_status(
                'is an existing mount point, but will link anyway due to --force-symlink '
            )
            os.remove(dest)
            os.symlink(src, dest)


def main():
    arguments = docopt(__doc__, version=version)
    global VERBOSE
    global DRY_RUN
    global FORCE_SYMLINK
    if arguments['--verbose']:
        VERBOSE = True
        verbose('arguments:')
        verbose(arguments)
    if arguments['--force-symlink']:
        FORCE_SYMLINK = True
    target_dir = os.environ['HOME']
    config_paths = arguments['<config>']
    for config_path in config_paths:
        base_dir = os.path.dirname(config_path)
        loaded_config = yaml.load(open(config_path).read(), Loader=yaml.SafeLoader)
        verbose('loaded config:')
        verbose(loaded_config)
        for program, program_config in loaded_config.items():
            for file_ in program_config['files']:
                link(file_, base_dir, target_dir)
