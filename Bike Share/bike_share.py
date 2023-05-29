import time
import numpy as np
import pandas as pd


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january','february','march','april','may','june', 'all']

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'all']


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
    city = input("Please enter the city (chicago, new york city, washington) > ").lower()
    while city not in list(CITY_DATA.keys()):
        city = input("Please enter a valid city (chicago, new york city, washington) > ").lower()
    print(f'You have chosen {city} as your city')
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please enter a month from (all, january, february, ... , june) > ').lower()
    while month not in MONTHS:
        month = input('Please enter a valid month from (all, january, february, ... , june) > ').lower()
    print(f'You have chosen {month} as your month')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please enter a day (all, monday, tuesday, ... sunday) > ').lower()
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while day not in days:
        day = input('Please enter a valid day (all, monday, tuesday, ... sunday) > ').lower()
    print(f'You have chosen {day} as your day')
        

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

    ## Converting times
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    days =  ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    pop_month = df['month'].mode()[0]
    print(f'Most popular month is: ', pop_month)

    # TO DO: display the most common day of week
    print(f'Most popular day is: ',df['day'].mode()[0])

    # TO DO: display the most common start hour
    print(f'Most popular hour is: ',df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_start = df['Start Station'].mode()[0]
    print(f'Most popular starting station is {pop_start}') 
    
    # TO DO: display most commonly used end station
    pop_end = df['End Station'].mode()[0]
    print(f'Most popular ending station is {pop_end}')
    
    # TO DO: display most frequent combination of start station and end station trip
    combinations = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).head(1)
    print(f'Most repeated combination is {combinations}')
                 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(f'The total travel time is:', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print(f'The total travel time is: ', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(f"User Types: {df['User Type'].value_counts()}")
    
    if city != 'washington':
        # TO DO: Display counts of gender
        print(f"Gender: {df['Gender'].value_counts()}")


        # TO DO: Display earliest, most recent, and most common year of birth
        print(f'Most Common Birth Year: ',{df['Birth Year'].mode()[0]})
        print(f'Latest Birth Year: ',{df['Birth Year'].max()})
        print(f'Earliest Birth Year: ',{df['Birth Year'].min()})
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def view_data(df):
    print()
    print('-'*40,'\n')
    ans = input('Would you like to see 5 rows of data? enter "yes" or "no" > ').lower()
    counter = 0
    
    while ans == 'yes':
        print(df.iloc[counter:counter+5])
        counter += 5
        print()
        print('-'*40,'\n')
        ans = input('Would you like to see the next 5 rows of data? enter "yes" or "no" > ').lower()
        
        


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        
        view_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()