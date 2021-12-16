#!/bin/bash
getValueFromConfigFile() {
	local nameOfConfig=$1
	local value=`grep $nameOfConfig ./config/localconfig.py | awk -F ':' '{print $2}'`
	local valueLen=${#value}
	local lastCharacter=${value:$valueLen-1:$valueLen}
	local subStringLength
	if [ "$lastCharacter" = "," ]; then
		subStringLength=$(expr $valueLen - 3)
	else
		subStringLength=$(expr $valueLen - 2)
	fi
	echo $value | cut -c2-$subStringLength
}
