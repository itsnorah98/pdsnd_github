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
        city = input("Select a city from {}, {} or {}:".format(*CITY_DATA.keys())).strip().lower()
        if city in CITY_DATA.keys():
            break
        
        
     

    # TO DO: get user input for month (all, january, february, ... , june)
    months=['all','january', 'february', 'march', 'april', 'may', 'june']
    
    while True:
        month = input('Enter A Month:').strip().lower()
        if month in months:
            break
        
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    week_days=['all','saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    
    while True:
      day = input('Enter A Week Day:').strip().lower()
      if day in week_days:
          break
      
            
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
    # load data file into a dataframe 
    df= pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month']= df['Start Time'].dt.month
    df['day_of_week']= df['Start Time'].dt.weekday_name
    
     # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month= months.index(month) + 1
        
     # filter by month to create the new dataframe
        df= df[df['month'] == month]
        
     # filter by day of week if applicable
    if day != 'all':
            # filter by day of week to create the new dataframe
            df= df[df['day_of_week'] == day.title()]
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_com_month = df['month'].mode()[0]
    print('the most common month: ',most_com_month)

    # TO DO: display the most common day of week
    most_com_day_of_week = df['day_of_week'].mode()[0]
    print('the most common day of week: ', most_com_day_of_week) 
          
    # TO DO: display the most common start hour
    df['hour']= df['Start Time'].dt.hour
    most_com_start_hour = df['hour'].mode()[0]
    print('the most common start hour: ', most_com_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_comm_strat_s = df['Start Station'].value_counts().idxmax()
    print('the most commonly used strat station: ' , most_comm_strat_s)

    # TO DO: display most commonly used end station
    most_comm_end_s = df['End Station'].value_counts().idxmax()
    print('the most commonly used end station: ', most_comm_end_s) 

    # TO DO: display most frequent combination of start station and end station trip
    df2= df.groupby(['Start Station', 'End Station'])
    most_freq_strat_end = df2['Trip Duration'].count().idxmax()
    print( 'the most frequent comination of start station and end staion:',  most_freq_strat_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('total travel time : ', total_travel_time)
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time : ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_usertype= df['User Type'].value_counts()
    print('counts of user types: ',count_usertype)
    
   # TO DO: Display counts of gender
    try:
        count_gender= df['Gender'].value_counts()
        print('counts of gender :', count_gender)
    except KeyError:
        print("There isn't a [Gender] column in this spreedsheet!")
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        most_earliest_year_of_birth= df['Birth Year'].min()
        print('earliest year of birth: ',most_earliest_year_of_birth)
    except KeyError:
        print("There isn't a [Birth year] column in this spreedsheet!")
    
    try:
        most_recent_year_of_birth= df['Birth Year'].max()
        print('most recent year of birth: ',most_recent_year_of_birth)
    except KeyError:
        print("There isn't a [Birth year] column in this spreedsheet!") 
    
    try:
        most_common_year_of_birth= df['Birth Year'].mode()[0]
        print('most common year of birth: ',most_common_year_of_birth)
    except KeyError:
        print("There isn't a [Birth year] column in this spreedsheet!") 
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):

    rows = 5
    start = 0
    end = rows - 1

    while True:
        data = input('do you want to see five lines of row data? yes or no ').lower()
        if data == 'yes':
            print(df.iloc[start : end + 1])
            start += rows
            end += rows
            ending= input ('do you want to see more row data? yes or no').lowe()
        if ending =='no':
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
