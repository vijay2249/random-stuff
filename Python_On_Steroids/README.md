# Python on STEROIDS

## Usage
python steroids.py -f <methodToExecute> --args <argumentsInString>

### Example:
python steroids.py -f current_directory

python steroids.py -f file_with_extensions --args "{'extensions': ['.txt', '.ts'],'uselessKey':'useLessValue'}"

python steroids.py -f subprocess_popen

python steroids.py -f setup_venv

python steroids.py -f setup_venv --args "{'venv_name':'testing-venv'}"
