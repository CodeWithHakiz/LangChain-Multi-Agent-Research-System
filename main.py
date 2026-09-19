from src.tools.tool import web_search,scrape_url

output = web_search.invoke("Latest news on AI Research")
print(output)




results = scrape_url.invoke("https://aimagazine.com")
print(results)
