import pandas as pd


def calculate_demographic_data(print_data=True):
  # Read data from file
  df = pd.read_csv('adult.data.csv')
  total_rows = len(df)

  # How many of each race are represented in this dataset? This should be a Pandas series         with race names as the index labels.
  race_count = df['race'].value_counts()

  # What is the average age of men?
  males = df.loc[df['sex'] == 'Male']
  average_age_men = round((males['age'].mean()), 1)

  # What is the percentage of people who have a Bachelor's degree?
  total_bachelors_degree = len(df.loc[df['education'] == 'Bachelors'])
  percentage_bachelors = round(((total_bachelors_degree / total_rows) * 100),
                               1)

  # What percentage of people with advanced education (`Bachelors`, `Masters`, or       `          Doctorate`) make more than 50K?
  ls = ['Bachelors', 'Masters', 'Doctorate']
  df2 = df.query('education in @ls')

  # What percentage of people without advanced education make more than 50K?
  df3 = df.query('education not in @ls')

  # with and without `Bachelors`, `Masters`, or `Doctorate`
  higher_education = len(df2.loc[df2['salary'] == '>50K'])
  lower_education = len(df3.loc[df3['salary'] == '>50K'])

  # percentage with salary >50K
  higher_education_rich = round(((higher_education / len(df2)) * 100), 1)
  lower_education_rich = round(((lower_education / len(df3)) * 100), 1)

  # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = df['hours-per-week'].min()

  # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

  num_min_workers = len(df.loc[df['hours-per-week'] == 1])

  rich = len(df.loc[(df['hours-per-week'] == 1) & (df['salary'] == '>50K')])

  rich_percentage = (rich / num_min_workers) * 100

  # What country has the highest percentage of people that earn >50K?
  per_country = df.loc[df['salary'] == '>50K']
  per_country = per_country['native-country']
  per_country_above50k = per_country.value_counts()
  c_count = (df['native-country']).value_counts()
  t_list = [c_count, per_country_above50k]

  tester = pd.DataFrame(t_list)
  tester = tester.T
  tester.columns = ['total-count', 'rich-count']
  tester['percentage-rich'] = (tester['rich-count'] /
                               tester['total-count']) * 100
  maximum = (tester['percentage-rich']).max()

  highest_earning_country = (tester['percentage-rich']).idxmax()
  highest_earning_country_percentage = round(maximum, 1)

  # Identify the most popular occupation for those who earn >50K in India.
  ind = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
  ind_occupations = ind['occupation'].value_counts()
  pop_occc = ind_occupations.max()
  df5 = ind_occupations.loc[ind_occupations == pop_occc]
  top_IN_occupation = df5.idxmax()

  if print_data:
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(
        f"Percentage with higher education that earn >50K: {higher_education_rich}%"
    )
    print(
        f"Percentage without higher education that earn >50K: {lower_education_rich}%"
    )
    print(f"Min work time: {min_work_hours} hours/week")
    print(
        f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
    )
    print("Country with highest percentage of rich:", highest_earning_country)
    print(
        f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
    )
    print("Top occupations in India:", top_IN_occupation)

  return {
      'race_count': race_count,
      'average_age_men': average_age_men,
      'percentage_bachelors': percentage_bachelors,
      'higher_education_rich': higher_education_rich,
      'lower_education_rich': lower_education_rich,
      'min_work_hours': min_work_hours,
      'rich_percentage': rich_percentage,
      'highest_earning_country': highest_earning_country,
      'highest_earning_country_percentage': highest_earning_country_percentage,
      'top_IN_occupation': top_IN_occupation
  }
