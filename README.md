>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

### Date created  : ***20-02-2024***
Include the date you created this project and README file.

#**Explore US Bikeshare Data**

## Description

The project is designed to **filter _US Bikeshare data_ and calculate the some stats** using `functions`. The bikeshare.py file prompts the user if the want to see raw data. Below is the sample of the functions used.

#### Function `get_filters():`
    """
    Asks user to specify a _city, month,_ and _day_ to analyze.

    Returns:
        -(str) city - name of the city to analyze
        *(str) month - name of the month to filter by, or "all" to apply no month filter
        +(str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

#### Function `load_data(city, month, day):`
    """
    Loads data for the specified ***city and filters by month and day*** if applicable.

    Args:
        -(str) city - name of the city to analyze
        *(str) month - name of the month to filter by, or "all" to apply no month filter
        +(str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
#### Stats functions

```    
-*time_stats(df):* Displays statistics on the most frequent times of travel.
-*station_stats(df):* Displays statistics on the most popular stations and trip.
-*trip_duration_stats(df):* Displays statistics on the total and average trip duration.
-*user_stats(df):* Displays statistics on bikeshare users.
```

### Files used
-***chicago.csv***
-***new_york_city.csv***
-***washington.csv***

### Credits
It's important to give proper credit. Add links to any repo that inspired you or blogposts you consulted.

