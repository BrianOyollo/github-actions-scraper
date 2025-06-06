import time
import driver_setup
import scrape_auction
import upload
import notify


with open("src/rescrape_urls_part_3.txt", "r") as file:
    urls = [url.strip() for url in file.readlines()]


# init driver
driver = driver_setup.setup_driver()

# scrape data
results = []
for url in urls:
    auction_data = scrape_auction.scrape_auction_data(driver, url)
    results.append(auction_data)
    time.sleep(5)

# teardown driver
driver_setup.driver_teardown(driver)

# save to local json file
upload.upload_to_s3(results)

notify.send_notification('github_actions', f"{len(results)} auctions scraped and saved successfully")

