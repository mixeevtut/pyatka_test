from signin_ui import SignIn


def main():
    sign_in = SignIn()
    sign_in.setup_method()
    sign_in.signin()
    sign_in.teardown_method()


if __name__ == '__main__':
    main()
