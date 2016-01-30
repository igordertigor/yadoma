# setup the fake home

  $ export HOME=$PWD/home
  $ mkdir $HOME

# put the current working dir on the path

  $ export PATH=$PWD:$PATH

# create an example program that we can execute and check it works

  $ touch example
  $ chmod +x example
  $ echo "#!/bin/sh\n" > example
  $ echo "echo 'hello example'" > example
  $ example
  hello example

# create the fake config directory with configs

  $ mkdir config
  $ touch config/.examplerc
  $ echo "example_confgrc" > config/.examplerc
  $ touch config/.examplerc.local
  $ echo "example_confgrc.local" > config/.examplerc.local
  $ touch config/doma.cfg
  $ cat <<EOF >> config/doma.cfg
  > example:
  >   files:
  >     -
  >       src: .examplerc
  >       dest: .examplerc
  >     -
  >       src: .examplerc.local
  >       dest: .examplerc.local
  > EOF
  $ cat  config/doma.cfg
  example:
    files:
      -
        src: .examplerc
        dest: .examplerc
      -
        src: .examplerc.local
        dest: .examplerc.local
# check what we have created

  $ ls -A1
  config
  example
  home
  $ ls -A1 config
  doma.cfg
  .examplerc
  .examplerc.local

# check that home is empty

  $ ls -A1 home

# run doma

  $ doma link config/doma.cfg

# check that the config dir remains unchanged

  $ ls -A1
  config
  example
  home
  $ ls -A1 config
  doma.cfg
  .examplerc
  .examplerc.local

# check the newly created values incl. symlinks

  $ ls -A1 home
  .examplerc
  .examplerc.local
  $ realpath home/.examplerc
  /tmp/cramtests-.*/test_doma.t/config/.examplerc (re)
  $ realpath home/.examplerc.local
  /tmp/cramtests-.*/test_doma.t/config/.examplerc.local (re)
