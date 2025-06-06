# Scraping with GitHub Actions# Scraping with GitHub Actions

## Description

This project scrapes auction URLs using GitHub Actions. It was built to rescrape vehicle auction data from [carsandbids.com](https://carsandbids.com) in an automated, cloud-based workflow. The scraper runs on a GitHub Actions runner, sleeps between requests, saves results as a JSON file, and uploads the output to an AWS S3 bucket.

## ⚙️ Features

- Scrapes a list of auction URLs
- 5-second delay between requests to respect rate limits
- Stores results in timestamped `.json` file
- Automatically uploads the output to S3
- Runs entirely in GitHub Actions (with internet access)

## 🧪 How to Run

1. Add your list of auction URLs to a file in the repo (e.g. `my_urls.txt`)

2. Update the filename in your Python code:
   
   ```python
   with open("my_urls.txt") as f:
       urls = [line.strip() for line in f if line.strip()]
   ```

3. Push your changes to GitHub

4. Go to the **Actions** tab → Select **"Scrape URLs and Upload to S3"** → Click **"Run workflow"**

## 🔐 Secrets Required

In your repo’s **Settings > Secrets and variables > Actions**, add:

- `AWS_ACCESS_KEY_ID`

- `AWS_SECRET_ACCESS_KEY`

- `AWS_DEFAULT_REGION`

- `AUCTIONS_BUCKET`

## 📦 Output

- JSON file with scraped data (e.g. `rescraped_results_1717594223.json`)

- File is uploaded to your specified S3 bucket


