from .models import User
from . import login_manager

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if not User.query.filter_by(username=email).first():
        return

    user = User.query.filter_by(username=email).first()
    _password = request.form['password']
    user.is_authenticated = user.verify_password(password=_password)

    return user


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'

