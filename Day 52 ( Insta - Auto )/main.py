from drivers import InstaFollower

SIMILAR_ACCOUNT = "chefsteos"

bot = InstaFollower("chromedriver_win32/chromedriver.exe")
bot.login(url="https://www.instagram.com/")
bot.find_followers(url="https://www.instagram.com/", taget_account=SIMILAR_ACCOUNT)
bot.follow()
