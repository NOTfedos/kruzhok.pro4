pyv="$(python3 -V 2>&1)"
version=$(echo "$pyv" | grep -Po '(?<=Python )(.+)')
echo "$version"
if [[ -z "$version" ]]
then
    echo "No Python!"
    exit
fi
parsedVersion="${version//./}"

if [[ "$parsedVersion" -lt "300" ]]
then
    echo "Wrong version of Python!"
    exit
fi

python3 -m pip install requests
