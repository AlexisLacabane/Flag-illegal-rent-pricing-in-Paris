# Flag-illegal-rent-pricing-in-Paris

In July 2019, Paris CityHall released the ALUR Regulation setting reference rent pricing in the French capital.
As my first project, I decided to web scrap https://seloger.com (1st website for renting an appartment :house:) and compare each ad to the increased reference m2 price set by the ALUR Regulation.

The general principle of this framework was to define a maximum value of rent per m² applicable to new signed leases, called increased reference rent or “max limit”

## Tool

![](/Media/P_logo.png)
![](/Media/Spyder_logo.png)

## Purpose

Create a pipeline in :file_folder: **Code.py** to optimise the following:

- clean the data web scrap from SeLoger.com using Python, Pandas, and BeautifulSoup
        :file_folder: **ted_main_dataset.csv**
- import and compare to documentation on max limit per size and district
        :file_folder: **Regulation.xlsx**
- save links not respecting reference price set by Paris ALUR regulation
        :page_facing_up::heavy_exclamation_mark: **Watch_list.txt**

## Conclusion

My work shows an important amount of links web scrap being overpriced.
This conclusion is coherent with recent article published in LeParisien stating that 50% of available apartments in Paris are not respecting the ALUR Regulation.
- [For French Speakers] : (http://www.leparisien.fr/immobilier/encadrement-des-loyers-a-paris-une-annonce-sur-deux-est-illegale-27-01-2020-8245101.php)
- [For English Speakers] The Independent describes the ongoing war between Paris CityHall and Airbnb regarding the multinational's illegal rent pricing strategies: (https://www.independent.co.uk/travel/news-and-advice/airbnb-paris-illegal-rental-lawsuit-adverts-france-holiday-a8773386.html)

## :warning: Initialise code :warning:

1. Modify headers with your own REQUEST HEADERS by doing the following:

![](/Media/Request_Headers.gif)

2. Modify in **Code.py** the number of pages you want to web scrap:

![](/Media/Code_Screenshot.jpg)

## You Run It, You Get It !
From your terminal, run the file and get your Watch_list.txt send out to your file ! 
You can also choose to open your browser and open all links (:warning: do not use it if you web scrap 50 pages)

![](/Media/Execute_code.gif)