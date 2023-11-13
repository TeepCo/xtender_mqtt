SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
WORK_DIR=${SCRIPT_DIR}/../src/sino/scom
# Be sure virtual environment is set up
cd ${SCRIPT_DIR}/..
pipenv install
pipenv run pip install -r ${SCRIPT_DIR}/../../requirements.txt
# Start build in the 'src' folder
cd src

# Remove generated files to force a complete build
rm -f ${WORK_DIR}/*.cpp
rm -f ${WORK_DIR}/*.pyd
rm -f ${WORK_DIR}/*.so

# Build the extension
# pipenv run pip install -r ${SCRIPT_DIR}/requirements.txtl
cd ..
pipenv run python ${SCRIPT_DIR}/../setup.py build_ext --inplace

# Move it to right location 'eq.: sino/scom'
mv -f baseframe.*so ${WORK_DIR}/
mv -f property.*so ${WORK_DIR}/





