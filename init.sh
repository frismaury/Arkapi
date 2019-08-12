# Define app file
export FLASK_APP=./source/webapp.py
export FLASK_DEBUG=1

# activate the virtual env
. ./bin/activate

# install dependencies
# pip install -r requirements.txt

# run the app
python -m flask run --host=0.0.0.0 --port=8000 && \
  deactivate
