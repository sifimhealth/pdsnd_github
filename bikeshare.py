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
    
    city = input("Enter city name:.......\n ").lower()
    while city not in CITY_DATA:
        city = input("Enter a valid city name:either chicago, new york city or washington\n ")
            
            
        
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january','fabruary','march','april','may','june']
    month = input("Enter month:......\n ").lower()
    while month not in months:
        month = input("Invalid input, please enter a valid month:......\n ")
           
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day = input('Enter day of week:......\n ').lower()
    while day not in days:
        day = input("Invalid input, please enter a valid day:......\n ")
                 
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
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

       
    
    if month != 'all':
        months = ['january','fabruary','march','april','may','june']
        month = months.index(month) + 1
        df = df[df['month']==month]
        
    if day != 'all':
        df = df[df['day_of_week']==day.title()]
    return df
        
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month=df['month'].mode()[0]                                 
    print('The most frequent month of travel is: ',popular_month)
                                             
                                  

    # TO DO: display the most common day of week
    popular_week = df['day_of_week'].mode()[0]
    print('The most frequent week of travel is: ', popular_week)

    # TO DO: display the most common start hour
        
    popular_hour = df['hour'].mode()[0]
    print('The most frequent hour of travel is: ',popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
   
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_station = df['Start Station'].mode()[0]

    print('The Most Commonly Used Start Station:', popular_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    print('The Most Commonly Used End Station:', popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    frequent_start_to_end_trip = df.groupby(["Start Station", "End Station"]).size().idxmax()

    print('Most Frequent Combination of Start and End Station Trip:', frequent_start_to_end_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['travel_time'] = df['End Time'] - df['Start Time']

    total_travel_time = df['travel_time'].sum()

    print("Total Travel Time:", total_travel_time)



    # TO DO: display mean travel time
    average_travel_time = df['travel_time'].mean()

    print('Average Travel Time:', average_travel_time)

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()

    print('Count of User Types:\n', user_types)

    print('\n')

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
   
        print('Count of Gender Type: \n', gender)
    except KeyError:
        print('Gender column does not exist:')
    print('\n')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        early_year = df['Birth Year'].min()

        print('Earliest Year of Birth:', early_year)
    
        print('\n')

        recent_year = df['Birth Year'].max()

        print('Most Recent Year of Birth:', recent_year)

        print('\n')

        common_year = df['Birth Year'].mode()

        print('Most Common Year of Birth:', common_year)
    except KeyError:
        print('Birth Year does not exist:')
    print('\n')
    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        read_mode = True
        count = 0
        df = pd.read_csv(CITY_DATA[city])
        while read_mode:
            data_view = input('\nWould you like view Raw Data? Enter yes or no.\n')
            if data_view.lower() != 'no':
                print(df.iloc[count:count+5])
                count = count + 5
            else:
                           
                print('You are exiting Raw Data view.\n')
                read_mode = False
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()        
             
                          
             
            
        

