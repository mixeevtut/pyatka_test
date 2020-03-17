from signin_ui import SignIn


def test_signin():
    sign_in = SignIn()
    sign_in.setup_method()
    sign_in.signin()
    sign_in.teardown_method()
