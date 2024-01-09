class Singleton:
    __instance = None

    @classmethod
    def instance(cls):
        if Singleton.__instance == None:
        	__instance = super(Singleton, cls).__new__(cls)
        return __instance
