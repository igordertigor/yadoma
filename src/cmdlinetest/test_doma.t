  $ export HOME=$CRAMTMP
  $ export PATH=$PWD:$PATH
  $ touch example
  $ chmod +x example
  $ echo "#!/bin/sh" > example
  $ echo "echo 'hello example'" > example
  $ example
  hello example
  $ mkdir config
  $ touch config/.example
  $ echo "example_confg" > config/.example
  $ touch config/doma.cfg
  $ echo "any" >> config/doma.cfg
  $ echo "  - .example" >> config/doma.cfg

  $ doma link config

  $ ls -A1
  config
  example
  .example
