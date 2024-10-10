# imports
import requests
import pandas as pd
import io

# importing data from the outcodes file
df = pd.read_excel("Postcode Outcodes - Final.xlsx")

# function to get the county of a given row in a dataframe
def get_outcode_county(data: pd.DataFrame, row_id: int = 1):
    # pulling relevant parts of the dataframe using postcode
    outcode = data.loc[row_id-1, "postcode"]

    api_url = ("https://opendata.camden.gov.uk/resource/tr8t-gqz7.csv?"
               "$where=starts_with(postcode_2, '" + outcode + " ')")

    try:
        response = requests.get(api_url)
        data = response.content.decode(response.apparent_encoding)
        data = io.StringIO(data.replace('\n,  \n', ''))
        response_df = pd.read_csv(data)
        # relevant columns and what to do with them:
        # easting - take average on min and max value
        # northing - same
        # county_name - need the mode
        # local_authorithy_name - need the mode
        # country_name - just take the first one
        # postcode_1 - gives an example postcode
    except Exception as e:
        print("API Request failed for",outcode)
        print(Exception)
        raise

    east = (response_df["easting"].max() + response_df["easting"].min()) / 2
    north = (response_df["northing"].max() + response_df["northing"].min()) / 2
    try:
        county = response_df["county_name"].mode()[0]
        local_auth = (response_df["local_authority_name"].mode()[0])
        if "(pseudo)" in county:
            county = local_auth
        country = response_df["country_name"][0]
        code = response_df["postcode_2"][0]
    except:
        county = "None - Postcode may not exist"
        local_auth = "None - Postcode may not exist"
        country = "None - Postcode may not exist"
        code = "None - Postcode may not exist"

    return {"eastings":east, "northings":north, "county":county, "local":local_auth, "country":country, "postcode":code}

# implementing the function to bulk request and update the dataframe
start = 50
end = 2951
for index in range(start, end):
    print("Progress: ",str(round((index-start)*100/(end-start), 2)),"%")
    if pd.isnull(df.loc[index-1, "county"]):
        try:
            info = get_outcode_county(df, index)
            print(index, info)

            df.loc[index - 1, "county"] = info["county"]
            df.loc[index - 1, "local authority"] = info["local"]
            df.loc[index - 1, "country"] = info["country"]
            df.loc[index - 1, "country"] = info["country"]
            df.loc[index - 1, "central eastings"] = info["eastings"]
            df.loc[index - 1, "central northings"] = info["northings"]
            df.loc[index - 1, "example postcode"] = info["postcode"]
        except Exception as err:
            print(err)
            raise
    if index%100 == 0:
        df.to_excel("Postcode Outcodes - Final.xlsx", index=False)

df.to_excel("Postcode Outcodes - Final.xlsx",index=False)
print("saved to excel")
