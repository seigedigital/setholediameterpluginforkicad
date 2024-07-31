#!/bin/bash

version=$(jq -r .versions[0].version metadata.json)
rm -f "../SetHoleDiameterPlugin-$version.zip"
zip -r "../SetHoleDiameterPlugin-$version.zip" ./* -x "*.svg" -x README.md -x LICENSE -x build.sh

# for a merge request append 
#     "download_sha256": "<shasumofarchive",
#   "download_size": <sumoffilesizes>,
#   "install_size": <sizeofarchiveinbytes>
#  to metadata.json
