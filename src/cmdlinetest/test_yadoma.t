# setup the fake home

  $ export HOME=$PWD/test-home
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
  $ touch config/.rc_with_src
  $ echo "example_confgrc" > config/.rc_with_src
  $ touch config/.rc_with_out_dest
  $ echo "example_confgrc.local" > config/.rc_with_out_dest
  $ touch config/yadoma.cfg
  $ cat <<EOF >> config/yadoma.cfg
  > example:
  >   files:
  >     -
  >       src: .rc_with_src
  >       dest: .rc_with_src_dest
  >     -
  >       src: .rc_with_out_dest
  > EOF
  $ cat  config/yadoma.cfg
  example:
    files:
      -
        src: .rc_with_src
        dest: .rc_with_src_dest
      -
        src: .rc_with_out_dest
# check what we have created

  $ ls -A1
  config
  example
  test-home
  $ ls -A1 config
  .rc_with_out_dest
  .rc_with_src
  yadoma.cfg

# check that home is empty

  $ ls -A1 test-home

# run yadoma

  $ yadoma link config/yadoma.cfg

# check that the config dir remains unchanged

  $ ls -A1
  config
  example
  test-home
  $ ls -A1 config
  .rc_with_out_dest
  .rc_with_src
  yadoma.cfg

# check the newly created values incl. symlinks

  $ ls -A1 test-home
  .rc_with_out_dest
  .rc_with_src_dest
  $ realpath test-home/.rc_with_src_dest
  /tmp/cramtests-.*/test_yadoma.t/config/.rc_with_src (re)

# check that 'src' is used in case of missing dest

  $ realpath test-home/.rc_with_out_dest
  /tmp/cramtests-.*/test_yadoma.t/config/.rc_with_out_dest (re)
