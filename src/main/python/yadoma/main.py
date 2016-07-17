"""yadoma

Usage:
  yadoma [options] link <config>...
  yadoma [options] <config>...

Options:
  -v --verbose  Verbose mode
  -d --dry-run  Dry run

"""

import os

from docopt import docopt
import yaml

LINK = 'link'
SUBCOMMANDS = [LINK]
VERBOSE = False
DRY_RUN = False


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
    else:
        verbose(message)
        try:
            os.symlink(src, dest)
        except OSError as ose:
            if ose.errno == 17:
                warn("symlink exists in target:{0}".format(dest))
            else:
                raise
        else:
            verbose("successful")


def main():
    arguments = docopt(__doc__)
    global VERBOSE
    global DRY_RUN
    if arguments['--verbose']:
        VERBOSE = True
        verbose('arguments:')
        verbose(arguments)
    if arguments['--dry-run']:
        DRY_RUN = True
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
