name="최윤성"

if [ $1 ]; then
	if [ "$2" == "zip" ]; then
		if [ -f "${name}_$(date +%Y%m%d).zip" ]; then
			rm ${name}_$(date +%Y%m%d).zip
		fi
		zip ${name}_$(date +%Y%m%d).zip $1_*
	elif [ "$2" == "py" ]; then
		touch $1_${name}_$(date +%Y%m%d).py
	elif [ "$2" == "cpp" ]; then
		touch $1_${name}_$(date +%Y%m%d).cpp
	else
		touch $1_${name}_$(date +%Y%m%d).py
	fi
else
	echo "No arg"
fi
