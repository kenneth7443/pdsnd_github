import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities = ('chicago','new york city','washington') 
        city = str(input("\nEnter the city to analyse. Enter Chicago, New York City or Washington.\n>>>")).lower()
        
        if city in cities:
            break
            
        else:
            print("\nThe city entered is not in the database. Enter Chicago, New York City or Washington.")
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months = ('all','january','february','march','april','may','june') 
        month = str(input("\nEnter the month to analyse. Enter January to June or \'all\'\n>>>")).lower()
        
        if month in months:
            break
        else:
            print("\nThe month entered is not in the database. Enter January to June or \'all\'")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ('all','monday','tuesday','wednesday','thursday','friday','saturday','sunday') 
        day = str(input("\nEnter the weekday to analyse. Enter Monday to Sunday or \'all\'\n>>>")).lower()
        
        if day in days:
            break
        else:
            print("\nInvalid input. Please enter Monday to Sunday or \'all\'")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    filename =  CITY_DATA[city]
    df = pd.read_csv(filename)  
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
           
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Common MONTH is  : ', df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('Common DAY is    : ', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('Common HOUR is   : ', df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % round((time.time() - start_time),1))
    print('-'*40)
   
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used START STATION is  : ', df['Start Station'].mode()[0])
   
    # TO DO: display most commonly used end station
    print('Most commonly used END STATION is    : ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'].str.cat(df['End Station'], join = 'outer', sep = '--->', na_rep = '_') 
    frequent_trip = df['Trip'].mode()
    frequent_trip_start = frequent_trip[0].split('--->')[0]
    frequent_trip_end = frequent_trip[0].split('--->')[1]
    print('The most frequent combination of Start Station and End Station is from {} to {}.'.format(frequent_trip_start, frequent_trip_end))
    print("\nThis took %s seconds." % round((time.time() - start_time),1))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = round(df['Trip Duration'].sum(),1)
    print('The Total Travel Time is {} seconds'.format(total_travel_time))
    
    # TO DO: display mean travel time
    mean_travel_time = round(df['Trip Duration'].mean(),1)
    print('The Mean Travel Time is {} seconds'.format(mean_travel_time))

    print("\nThis took %s seconds." % round((time.time() - start_time),1))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type = df['User Type'].groupby(df['User Type']).count()
    print('The User Type count is   : \n',count_user_type)

    ########################################################################
    #       HANDLE ERROR FROM ABSENCE OF GENDER AND BIRTH YEAR             #
    ########################################################################
    # TO DO: Display counts of gender
    while True:
        try:
            counts_of_gender = round(df['Gender'].groupby(df['Gender']).count())
            print('The count of Gender  : \n', counts_of_gender)
            break
        except KeyError:
            print('There is no Gender information in the database')
            break

    # TO DO: Display earliest, most recent, and most common year of birth
    while True:
        try:
            earliest_birth_year = int(df['Birth Year'].min())
            most_recent_birth_year = int(df['Birth Year'].max())
            most_common_birth_year = int(df['Birth Year'].mode()[0])

            print('The earliest birth year is {}.'.format(earliest_birth_year))
            print('The most recent birth year is {}.'.format(most_recent_birth_year))
            print('The most common birth year is {}.'.format(most_common_birth_year))
            break
        except Exception:
            print('There is no Birth Year information in the database')
            break
  #################################################################################      
    print("\nThis took %s seconds." % round((time.time() - start_time),1)),
    print('-'*40)
    
def display_raw_data(df):
    """
   Prompts user to decide if they want to see raw data by inputing 'yes' or 'no'.
   If 'yes', display 5 rows at a time of raw data for the specified city and asks if you want to see more raw data.
   If 'no', proceed to run the rest of the code

    """
    
    raw = str(input("\nDo you want to view Raw Data. Please enter only 'yes' or 'no'?\n>>>").lower())
    i = 0
    page = 1
    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            # TO DO: appropriately subset/slice your dataframe to display next five rows
            print('\n','*'*40)
            print('Raw Data                       Page {}'.format(page))
            print('*'*40)
            print(df.iloc[i:i+5])
            print('*'*40)
                        
            # TO DO: convert the user input to lower case using lower() function
            raw = str(input("\nDo you want to view more Raw Data? Please enter only 'yes' or 'no'?\n>>>").lower())
            i += 5
            page += 1
        else:
            raw = str(input("\nYour input is invalid. Please enter only 'yes' or 'no'\n>>>").lower())
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(display_raw_data(df))
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
                
        while True:
            restart = input('\nWould you like to restart? Enter yes or no.\n>>>').lower()
            if restart in ('yes','no'):
                break
            else:
                print('\nInvalid input. Please enter \'yes\' or \'no\'.')
        if restart == 'no':
            break
        
if __name__ == "__main__":
	main()
