#!/bin/bash

JSON="application/json"
TEXT="application/text"

METHOD=POST
if [ "$1" == "-u" ]; then
        METHOD=PUT
fi

for c in hosts groups templates; do
pushd $c
for i in `echo *`; do
	if [ $c == "templates" ]; then
		curl -H "Content-type: $TEXT" -X $METHOD --data-binary @$i http://127.0.0.1/api/1.0/$c/$i
	else
		curl -H "Content-type: $JSON" -X $METHOD -d @$i http://127.0.0.1/api/1.0/$c/$i
	fi
done
popd
done
