# scraping-example
An example Python script to scrape JSON data from a webpage to check if a product has released (in this case, Xenoblade Chronicles 3 Special Edition release)

In order to use this script you will need to install everything necessary to use the Selenium library with the Chrome webdriver installed at a system level. The Chrome webdriver allows the entire page to loaded, including dynamic JSON content, which is not rendered when using a simple HTTP request to the page URL. The page must be loaded in the Chrome webdriver in order for the Javascript to run, which injects the JSON that we parse in this example into the page source. This is why Selenium and the Chrome webdriver are being used.
