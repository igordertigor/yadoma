===================================
yadoma: yet another dotfile manager
===================================

This is my personal take on a dotfile manager.

Principles
----------

* Pile of symlinks approach
* Declarative configuration
* Composable
* Versioning not baked in

Example
-------

Given the config in home, e.g. ``yadoma.yaml``:

.. code:: yaml

   - ~/config/zsh-config
   - ~/config/vim-config
   - ~/config/ssh-config

Given the following directory structure:

.. code:: console

   $ ls ~/config/zsh-config
   .zshrc
   $ ls ~/config/vim-config
   .vimrc
   .vim
   $ ls ~/config/ssh-config
   .ssh/
   $ ls ~/config/ssh-config/.ssh
   .ssh/config


Given a files of the form:

.. code:: yaml

    file:
      name: my_zsh_config

Let's imagine something different:

.. code:: yaml

   ~/public_config/
     - zsh
       - .zshrc
       - .zshrc.local
       - .zsh/
     - ssh
       - .ssh/config

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
