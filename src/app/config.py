# objects are referenced by Flask using Flask().config.from_object('config.className')


class Config(object):
    DEBUG = None
    TESTING = None


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    DEBUG = False
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
