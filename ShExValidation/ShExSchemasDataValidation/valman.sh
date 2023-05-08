# 5/7/2023
# validates using Shex.js parser

# First location of the shex.js parser 
SHEXJS=/Users/DKS02/A123/git/research/FHIRCat/shex.js
VALIDATE=$SHEXJS/packages/shex-cli/bin
WORKDIR=/Users/DKS02/A123/git/research/FHIRCat/validation/ShExValidation/ShExSchemasDataValidation


set -x
cd $WORKDIR

export PATH=$VALIDATE:$PATH

# One way to invoke validate with YAML FILE
YAML=./FunctionPatterns/FunctionPatterns.yaml
validate --human --yaml-manifest $YAML

# Another way of invoking validate with SHEX and TTL
SHEX=./FunctionPatterns/FunctionPatterns.shex
TTL=./FunctionPatterns/FunctionPatterns.ttl
validate -x $SHEX -d $TTL -m '<inst_exists>@<FunctionPatternsShape>,<inst_noExists>@!<FunctionPatternsShape>'
set +x
