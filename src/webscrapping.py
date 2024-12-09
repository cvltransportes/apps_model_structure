from botweb import BotWeb


class MyBot(BotWeb):
    def __init__(self, *args, **kwargs):
        super().__init__(
            # The prefix name to be concatenated with the credentials_keys
            # eg. WEB_SYSTEM_USERNAME, WEB_SYSTEM_PASSWORD
            # these variables will be setted as environment variables
            # with the values asked from the terminal.
            # To prevent of every run ask the credentials from the terminal
            # restart the IDE after provide the credentials values
            prefix_env="WEB_SYSTEM",
            credentials_keys=["USERNAME", "PASSWORD"]
            )

    def login(self):
        """My login logic here! (Abstract method needs to be implemented)"""
        # self._enter_username(self.credentials['USERNAME'])
        # self._enter_password(self.credentials['PASSWORD'])
        # self._submit()

        # This method sets the cookies into the self.session: requests.Session
        # It enable making requests inside the system
        # see the post_example() method bellow
        self.get_cookies()

    def post_example(self):
        # The headers inspected from the network request
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
            "authorization": "",
            "content-type": "application/json;charset=UTF-8",
        }

        # If the system store the token in the local storage it would work,
        # else override it with your own logic to get the token authorization
        headers.update({
            "authorization": self.get_token_authorization_from_storage()
            })

        # The payload inspected from the network request
        body = 'a=something&b=anotherthing'
        response = self.session.post(
            "https://example.com.br",
            headers=headers,
            data=body,
        )
        if response.status_code == 200:
            print(response.json())


if __name__ == '__main__':
    with MyBot() as mybot:
        mybot.init_browser(headless=False, browser="firefox")
        mybot.open(
            "https://github.com/login"
        )
        mybot.login()
        # mybot.post_example()
        input("Digite algo para continuar...")
