Edit 2023: yadoma was written by @esc a couple of years ago and ended up no
longer maintained. It seemed that I was the only user, so I'm taking over
maintenance. However, given the simplicity of the tool, I kept everything
largely the same, including this README. Hence, "I" refers to @esc rather than
myself.

===================================
yadoma: yet another dotfile manager
===================================

This is my personal take on a dotfile-manager.

Principles
----------

* Pile of symlinks approach
* Declarative configuration
* Composable
* Versioning not baked in
* Infinitely hackable

Prior Art (or why I decided to roll my own)
-------------------------------------------

`vcsh <https://github.com/RichiH/vcsh>`_
    written in shell (yuck) and has git baked in
`dewi <https://github.com/ft/dewi>`_
    written in perl (yuck) and didn't grok how it worked
`dotfilemanager <https://pypi.python.org/pypi/dotfilemanager/>`_
    has weird conventions and strange config

Edit: in 2018, I discovered that there are many more dotfile-managers out
there: https://dotfiles.github.io/

Example
-------

Given the yaml config ``config.yadoma`` in the directory ``config/public``::

    example-prog:
      files:
        -
          src: .rc_with_src
          dest: .rc_with_src_dest
        -
          src: .rc_with_out_dest
        - .plainrc

And, given the following files of the directory::

    .plainrc
    .rc_with_src
    .rc_with_out_dest

Doing::

    $ yadoma config/public

Will create the following symlinks in the users ``$HOME`` for the program
``example-prog``::


    .plainrc
    .rc_with_src_dest
    .rc_with_out_dest

TODO and Ideas
--------------

Many.


License
-------


Copyright 2016-2019 Valentin Haenel <valentin@haenel.co>

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License. You may obtain a copy of the
License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
