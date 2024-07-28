#!/bin/bash

version=$(jq -r .versions[0].version metadata.json)
rm -f "../SetHoleDiameterPlugin-$version.zip"
zip -r "../SetHoleDiameterPlugin-$version.zip" ./* -x "*.svg" -x README.md -x LICENSE -x build.sh

