# noinspection SpellCheckingInspection
class Config(object):
    def __init__(self, environment):
        """ Establish environment variables that will be used during test case execution. Typically
        environment-specific.
        """

        if environment.lower() == 'qa':
            self.env = 'qa'
        elif environment.lower() == 'uat':
            self.env = 'uat'
        else:
            raise ValueError(f"{environment} is not a valid environment.")

        self.url = self.pick_url({
            "qa": "https://www.google.com",
            "uat": "https://www.rbauction.com"
        })

        self.username = "sugumar3034@gmail.com"
        self.password = "Welcome@123"
        self.google_search_text = "mobile integration workgroup"

        # test data
        self.search_text = "excavator"
        self.industry = "Construction"
        self.min_year = "2018"
        self.max_year = "2020"
        self.make = "CATERPILLAR"

    # noinspection PyMethodMayBeStatic
    def pick_url(self, env_dict) -> str:
        return self.pick(env_dict)

    def pick(self, env_dict):
        return env_dict[self.env]
