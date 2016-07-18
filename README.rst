===================================
yadoma: yet another dotfile manager
===================================

This is my personal take on a dotfile manager.

Prior Art
---------

- `vcsh <https://github.com/RichiH/vcsh>`_
- `dewi <https://github.com/ft/dewi>`_
- `dotfilemanager <https://pypi.python.org/pypi/dotfilemanager/>`_

Principles
----------

* Pile of symlinks approach
* Declarative configuration
* Composable
* Versioning not baked in

Example
-------

Given the config ``config.yadoma`` in the directory ``config/public``::

    example-prog:
      files:
        -
          src: .rc_with_src
          dest: .rc_with_src_dest
        -
          src: .rc_with_out_dest

And, given the following files of the directory ::

    .rc_with_src
    .rc_with_out_dest

Doing::

    $ yadoma config/public

Will create the following two symlinks in the users ``$HOME`` for the program
``example-prog``::


    .rc_with_src_dest
    .rc_with_out_dest


License
-------


Copyright 2016 Valentin Haenel <valentin@haenel.co>

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License. You may obtain a copy of the
License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
