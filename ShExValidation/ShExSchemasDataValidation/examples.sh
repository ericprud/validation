#!/bin/bash
# ############################
# author: Deepak Sharma
# email: m2dks@yahoo.com
# ############################
#
# examples to include in README.md

# Run this script to generate README.md programmatically
# Following array has a list of strings
# Each string has a delimiter "#" to split the string
# first part (before #) is name of a sub-directory - it must match
# second part (after #) is description that goes in README to describe what type of test is in the subdirectory.

declare -a examples=(
					 "basic_type_test#A Basic Type Test"
	                 "quantity_test#Quantity Resource Tests for type arcs"
					 "constraint_tests_without_IMPORT#A collection of ShEx constraint tests without IMPORT"
	                 "constraint_testsd#A collection of ShEx constraint tests"
	                 )