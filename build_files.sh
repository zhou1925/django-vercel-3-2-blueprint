# build-files.sh
echo "BUILD START"

# create a virtual environment named 'venv' if it doesn't already exist
python3.9 -m venv venv

# activate the virtual environment
source venv/bin/activate

# install distutils manually
pip install setuptools==58.0.4 # A version that includes distutils

# install all deps in the venv
pip install -r requirements.txt

# collect static files using the Python interpreter from venv
python manage.py collectstatic --noinput

# if you will use db
# python3.9 manage.py makemigrations
# python3.9 manage.py migrate

# if you wanna create your superuser in this script
# echo "from django.contrib.auth.models import User; User.objects.createw_superuser('admon', 'admon@abc.com', 'superadmonpass')" | python manage.py shell

echo "BUILD END"
