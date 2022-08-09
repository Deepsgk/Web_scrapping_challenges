from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
def scrape():
     
     executable_path = {'executable_path': ChromeDriverManager().install()}
     browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
     url = 'https://redplanetscience.com/'
     browser.visit(url)


# Convert the browser html to a soup object and then quit the browser
     html = browser.html
     soup = bs(html, 'html.parser')



     soup.find_all('div', class_='content_title')

# Use the parent element to find the first a tag and save it as `news_title`
     news_title=soup.find_all('div', class_='content_title')[0]
     news_title


# Use the parent element to find the paragraph text
     news_p=soup.find_all('div', class_='article_teaser_body')[0]
     news_p

#comparison table
     mars_df = pd.read_html('https://galaxyfacts-mars.com')[0]
     mars_df.columns=['Description', 'Mars', 'Earth']
     mars_df.set_index('Description', inplace=True)
     mars_df




    
     url2 = "https://marshemispheres.com/"
     browser.visit(url2)
     hemisphere_image_urls = []

     for i in range(4):
        html = browser.html
        soup = bs(html, "html.parser")
    
        title = soup.find_all("h3")[i].get_text()
        browser.find_by_tag('h3')[i].click()
    
        html = browser.html
        soup = bs(html, "html.parser")
    
        img1_url = soup.find("img", class_="wide-image")["src"]
    
        hemisphere_image_urls.append({
            "title": title,
            "img_url": url2 + img1_url
        })
        browser.back()
        
        title1 = hemisphere_image_urls[0]["title"]
        image1 = hemisphere_image_urls[0]["img_url"]
    
        title2 = hemisphere_image_urls[1]["title"]
        image2 = hemisphere_image_urls[1]["img_url"]

        title3 = hemisphere_image_urls[2]["title"]
        image3 = hemisphere_image_urls[2]["img_url"]

        title4 = hemisphere_image_urls[3]["title"]
        image4 = hemisphere_image_urls[3]["img_url"]
          
        hemisphere_image_urls   
    
# Visit URL
     url1 = 'https://spaceimages-mars.com'
     browser.visit(url1)

# Find and click the full image button
     full_image_elem = browser.find_by_tag('button')[1]
     full_image_elem.click()


# Parse the resulting html with soup/Images
     html1 = browser.html
     img_soup = soup(html1, 'html.parser')
     img_soup
     img_url_rel = img_soup.find('img', class_='fancybox-image')["src"]
     img_url_rel
     featured_img_url = f'https://spaceimages-mars.com/{img_url_rel}'
     featured_img_url


# Quit browser
     browser.quit()


# 4. Print the list that holds the dictionary of each image url and title.

    
     final_mars_data = {
"latest_title": news_title,
"latest_paragraph" : news_p,
"featured_image": featured_img_url,
"comparison_table": mars_df,
"hemisphere_scrape": hemisphere_image_urls,
"title1": title1,
"title2": title2,
"title3": title3,
"title4": title4,
"image1": image1,
"image2": image2,
"image3": image3,
"image4": image4



}
     
     return final_mars_data
 