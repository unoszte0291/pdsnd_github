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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please enter city name ")
        if city.lower() not in ('chicago', 'new york city', 'washington'):
            print("Please enter chicago or new york city or washington")
        else:
            break
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enter month | (e.g. january:")
        if month.lower() not in ('january','february','march','aplil','may','june'):
            print ("Please enter the correct month")
        else:
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter day of week:")
        if day.lower() not in ('monday','tuesday','wednesday','thursday','friday','saturday','sunday'):
            print ("Please enter the correct day of week")
        else:
            break
    print('-'*40)
    return city.lower(),month.lower(),day.lower()
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("the most common month:",common_month)

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day
    common_day_of_week = df['day'].mode()[0]
    print("the most common day of week:",common_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print("the most common start hour:",common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Time'].mode()[0]
    print("the most common start station:",start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Time'].mode()[0]
    print("the most common end station:",end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + "-" + df['End Station']
    df['Trip'].mode()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("total travel time:",total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("mean travel time:",mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

df = pd.read_csv(CITY_DATA[city])
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print("counts of user types:",count_user_type)

    # TO DO: Display counts of gender
    try:
        count_gender = df['Gender'].value_counts()
    except ValueError:
        print("Oops, there is no Gender data")
    else:
        print("counts of gender:",count_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year_of_birth = df['Birth Year'].min()
    print("earliest year of birth:",earliest_year_of_birth)

    most_recent_year_of_birth = df['Birth Year'].max()
    print("most recent year of birth:",most_recent_year_of_birth)

    most_common_year_of_birth = df['Birth Year'].mode()
    print("most common year of birth:",most_common_year_of_birth)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    user_stats = input('\nWould you like to see 5 line of raw data?\nPlease enter yes or no\n').lower()
　　　　　　if user_stats in ('yes', 'y'):
    　　　　　　　print(df.iloc[0:5])
        　　　　　user_stats = input('Would you like to see 5 line of raw data again? Please enter yes or no: ').lower()
        　　　　　if user_stats not in ('yes', 'y'):
            　　　break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
