#!/bin/bash

version=$(jq -r .versions[0].version metadata.json)
zip -r "../SetHoleDiameterPlugin-$version.zip" ./*

