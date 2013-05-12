import requests
import lxml.html

link = "https://ooni.torproject.org/reports/2012/Hadara_Palestine.html"
html = requests.get(link).text
root = lxml.html.fromstring(html)

for site in root.cssselect("div[class='span3']"):
    image_link = site.cssselect("img")
    if not image_link:
        print "Skipping..."
        continue
    caption = site.cssselect("div[class='caption']")
    if not caption:
        print "Skipping2..."
        continue

    image_link = image_link[0].values()[0]
    #print caption
    caption_link = caption[0].cssselect("h5")[0].text

    print "![%s](%s)" % (caption_link, image_link)
    print ""
    print "[%s](%s)" % (caption_link, caption_link)
    print "\n"
    # print image_link
    # print caption_title
    # print caption_link


