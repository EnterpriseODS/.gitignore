print('Personal_data:')

first_name: str = 'Dima'
last_name: str = 'Great'
year_of_birth: int = 1987
date_of_birth: str = '25.07.1987'
age: int = 2022 - year_of_birth  # calculates age when entering a year (relevant for 2022)
gender: str = 'male'
place_of_residence: str = 'Odessa'
IT_experience: str = 'not'
start_date: str = '17.10.2022'  # start date of training
lessons_learned: int = 2
full_name: str = last_name + ' ' + first_name  # for easy and fast printing

print('full_name' ':', full_name,  '\n', 'age', ':', age, "(" 'date_of_birth', date_of_birth, ")")
print('gender', ':', gender, '\n' 'place_of_residence', ':', place_of_residence)
print('IT_experience',':', IT_experience, '\n' 'start_date', ':', start_date, ',lessons_learned', ':', lessons_learned)
