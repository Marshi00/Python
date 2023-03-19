from internet_speed_twitter_bot import InternetSpeedTwitterBot

twi_speed_complain_bot = InternetSpeedTwitterBot(driver_path="chromedriver_win32/chromedriver.exe")
# twi_speed_complain_bot.get_internet_speed(url="https://www.speedtest.net/")
twi_speed_complain_bot.tweet_at_provider()
