#!/bin/bash

# requires sponge (from moreutils) and jq

# With thanks to the MISP team for
# https://github.com/MISP/misp-galaxy/blob/master/jq_all_the_things.sh,
# from which this script was derived

#validate json schemata
for file in `find seps/ -name "*.json"`
do
  echo validating ${file}
  cat ${file} | jq . >/dev/null
  rc=$?
  if [[ $rc != 0 ]]; then exit $rc; fi
done

set -e
set -x

# beautify json schemata
for file in `find seps/ -name "*.json"`
do
  echo beautifing ${file}
  cat ${file} | jq . | sponge ${file}
done
