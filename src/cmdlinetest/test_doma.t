  $ export HOME=$CRAMTMP
  $ mkdir config
  $ touch config/.example
  $ echo "example_confg" > config/.example
  $ touch config/doma.cfg
  $ echo "any" >> config/doma.cfg
  $ echo "  - .example" >> config/doma.cfg

  $ doma link config

  $ ls -A1
  config
  .example
