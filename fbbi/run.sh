#!/bin/bash

# $1: name of the ontology file to be processed (e.g., FBbi.owl)

./extract_all_classes.sh $1
./extract_all_imaging_methods.sh $1

python add_binary_columns.py

#rm fbbi-classes.csv
