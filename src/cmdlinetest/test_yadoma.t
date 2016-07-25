# setup the fake home

  $ export HOME=$PWD/test-home
  $ mkdir $HOME

# put the current working dir on the path

  $ export PATH=$PWD:$PATH

# create an example program that we can execute and check it works

  $ touch example-prog
  $ chmod +x example-prog
  $ echo "#!/bin/sh\n" > example-prog
  $ echo "echo 'hello example-prog'" > example-prog
  $ example-prog
  hello example-prog

# create the fake config directory with configs

  $ mkdir config
  $ touch config/.rc_with_src
  $ echo "example_prog_confgrc" > config/.rc_with_src
  $ touch config/.rc_with_out_dest
  $ echo "example_prog_confgrc.local" > config/.rc_with_out_dest
  $ touch config/.plain_rc
  $ echo "example_prog_plainrc" > config/.plain_rc
  $ touch config/yadoma.cfg
  $ cat <<EOF >> config/yadoma.cfg
  > example-prog:
  >   files:
  >     -
  >       src: .rc_with_src
  >       dest: .rc_with_src_dest
  >     -
  >       src: .rc_with_out_dest
  >     - .plain_rc
  > EOF
  $ cat  config/yadoma.cfg
  example-prog:
    files:
      -
        src: .rc_with_src
        dest: .rc_with_src_dest
      -
        src: .rc_with_out_dest
      - .plain_rc

# check what we have created

  $ ls -A1
  config
  example-prog
  test-home
  $ ls -A1 config
  .plain_rc
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
  example-prog
  test-home
  $ ls -A1 config
  .plain_rc
  .rc_with_out_dest
  .rc_with_src
  yadoma.cfg

# check the newly created values incl. symlinks

  $ ls -A1 test-home
  .plain_rc
  .rc_with_out_dest
  .rc_with_src_dest
  $ readlink -f test-home/.rc_with_src_dest
  /tmp/cramtests-.*/test_yadoma.t/config/.rc_with_src (re)
  $ readlink -f test-home/.plain_rc
  /tmp/cramtests-.*/test_yadoma.t/config/.plain_rc (re)

# check that 'src' is used in case of missing dest

  $ readlink -f test-home/.rc_with_out_dest
  /tmp/cramtests-.*/test_yadoma.t/config/.rc_with_out_dest (re)
