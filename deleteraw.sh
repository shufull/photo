#/bin/sh

DIR=$1

if [ ! -e ${DIR} ];then
	echo "" >&2
	exit 1
fi

rm -f ${DIR}/*.NEF