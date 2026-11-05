#!/bin/bash

docker run -v $PWD/:/work -w /work --rm -ti obolibrary/robot robot filter --input $1 --term FBbi:00000222 --select "annotations self descendants" --signature true --output FBbi-imaging-methods.owl

docker run -v $PWD/:/work -w /work --rm -ti obolibrary/robot robot export --input FBbi-imaging-methods.owl --header "ID|LABEL|definition" --include classes --entity-select NAMED --export fbbi-imaging-methods.csv

rm FBbi-imaging-methods.owl