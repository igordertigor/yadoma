import os
from pybuilder.core import use_plugin, init
from pybuilder.vcs import VCSRevision

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
#use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.cram")
use_plugin("filter_resources")


name = "yadoma"
default_task = "publish"
version = '{0}.{1}'.format(VCSRevision().count,
                           os.environ.get('TRAVIS_BUILD_NUMBER', 0))


@init
def set_properties(project):
    project.depends_on('docopt')
    project.depends_on('pyyaml')
    project.get_property('filter_resources_glob').extend(
        ['**/yadoma/__init__.py'])
