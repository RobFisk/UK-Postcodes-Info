# UK-Postcodes-Info
A file containing information from Open Data Camden (https://opendata.camden.gov.uk/Maps/National-Statistics-Postcode-Lookup-Camden-Map/thx4-v2bd) summarised by postal outcode

Code was used to find every postcode outcode by going through the ids in the camden dataset (I couldn't find the exact code used but made sure to double check we had them all).

Then the main.py file was used to generate the dataset seen in the CSV. The columns were calculated as follows:
- Outcode: Every two/three/four digit postal outcode e.g. DE1
- Country: The country that the outcode is found in e.g. Scotland
- County: The count that the majority of addresses in the outcode are located in e.g. Dorset
- Region: The broader region in which the majority of addresses are found (missing in the dataset outside of England) e.g. South East
- Parliamentary Constituency: Similarly, majority Parliamentary constituency e.g. Chelmsford
- Local Authority: Similarly, the majority local council e.g. Aberdeen City
- Central Latitude: The midpoint between the furthest north and south addresses in the postcode.
- Central Longitude: The same but for east/west
(Eastings/Northings are a translation of Lat/Longitude into other co-ordinates)

Enjoy!
