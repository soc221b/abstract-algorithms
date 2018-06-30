################################################################################
# Functions
################################################################################
# you could pass expect error-code to $1
assert()
{
    error=$?
    if [[ $# -eq 1 ]]; then
        if [ $error -ne $1 ]; then
            echo "exit ($error)"
            error_code=1
        fi
    else
        if [ $error -ne 0 ]; then
            echo "exit ($error)"
            error_code=1
        fi
    fi
}

CXX=g++-7
cwd=$(pwd)
root_path="$(cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )/.."
error_code=0

cd "$root_path/test"
for cpp_file in `find */*.cpp`
do
    $CXX --std=c++11 -Wall "$cpp_file"
    assert 0
done

cd "$cwd"

if [ $error_code -eq 0 ]; then
    echo 'Passed'
else
    echo 'Error'
    exit 1
fi
