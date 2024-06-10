import webbrowser

# List of URLs to open in the browser
urls = [
    "http://example.com",
    "http://anotherexample.com",
    # Add more URLs as needed
]

# Open each URL in a new tab
for url in urls:
    webbrowser.open_new_tab(url)