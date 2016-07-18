"""yadoma

Usage:
  yadoma [options] link <config>...
  yadoma [options] <config>...

Options:
  -h --help         Help screen
  --version         Version
  -v --verbose      Verbose mode
  -d --dry-run      Dry run
  --force-symlink   Force overwrite symlinks

"""

import os

from docopt import docopt
import yaml

from . import __version__ as version

LINK = 'link'
SUBCOMMANDS = [LINK]
VERBOSE = False
DRY_RUN = False
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


def get_subcommand(arguments):
    for subcommand in SUBCOMMANDS:
        if arguments[subcommand]:
            return subcommand
    else:
        return LINK


def link(file_, base_dir, target_dir):
    if isinstance(file_, str):
        src = os.path.abspath(os.path.join(base_dir, file_))
        dest = os.path.join(target_dir, file_)
    else:
        try:
            src = os.path.abspath(os.path.join(base_dir, file_['src']))
        except KeyError:
            raise ConfigError("missing 'src' entry")
        try:
            dest = os.path.join(target_dir, file_['dest'])
        except KeyError:
            dest = os.path.join(target_dir, file_['src'])
    message = "will try to symlink '{0}' to '{1}'...".format(src, dest)
    if DRY_RUN:
        info(message)
        info('...but will not because we are in a dry-run.')
    else:
        verbose(message)
        if (not os.path.exists(dest) or
                os.path.exists(dest) and FORCE_SYMLINK):
            if FORCE_SYMLINK:
                verbose('(will remove existing symlink as requested)')
                os.remove(dest)
            os.symlink(src, dest)
            verbose("...successful.")
        else:
            warn("...failed: symlink exists in target:{0}".format(dest))


def main():
    arguments = docopt(__doc__, version=version)
    global VERBOSE
    global DRY_RUN
    global FORCE_SYMLINK
    if arguments['--verbose']:
        VERBOSE = True
        verbose('arguments:')
        verbose(arguments)
    if arguments['--dry-run']:
        DRY_RUN = True
    if arguments['--force-symlink']:
        FORCE_SYMLINK = True
    target_dir = os.environ['HOME']
    config_paths = arguments['<config>']
    subcommand = get_subcommand(arguments)
    for config_path in config_paths:
        base_dir = os.path.dirname(config_path)
        loaded_config = yaml.load(open(config_path).read())
        verbose('loaded config:')
        verbose(loaded_config)
        if subcommand == LINK:
            for program, program_config in loaded_config.items():
                for file_ in program_config['files']:
                    link(file_, base_dir, target_dir)
