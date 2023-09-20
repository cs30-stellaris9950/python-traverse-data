# survey result count function
def survey_result_count():

    with open("survey-results.txt", "r") as survey_results_output:
        survey_results = survey_results_output.readlines()

    yes_count = 0
    no_count = 0
    maybe_count = 0

    for item in survey_results:
        # count yes
        if item == 'Yes\n' or item == 'Yes':
            yes_count += 1
        # count no
        elif item == 'No\n' or item == 'No':
            no_count += 1
        # count maybe
        elif item == 'Maybe\n' or item == 'Maybe':
            maybe_count += 1

    print(f"Survey Results: Yes({yes_count}), No({no_count}), Maybe({maybe_count})")


# survey result count function
def age_data_count():

    with open("age-data.txt", "r") as age_data_output:
        age_data = age_data_output.readlines()

    under_18 = 0
    from_18_to_35 = 0
    from_36_to_65 = 0
    above_65 = 0
    for item in age_data:
        item = int(item)
        # count under 18
        if item < 18:
            under_18 += 1
        # count 18 to 35
        elif 18 <= item <= 35:
            from_18_to_35 += 1
        # count 36 to 65
        elif 36 <= item <= 65:
            from_36_to_65 += 1
        # count above 65
        else:
            above_65 += 1

    print(f"Age Results: under 18({under_18}), 18-35({from_18_to_35}), 36-65({from_36_to_65}), above 65({above_65})")


# survey result count function
def number_data_count():

    with open("number-data.txt", "r") as number_data_output:
        number_data = number_data_output.readlines()

    odd_count = 0
    even_count = 0

    for item in number_data:
        item = int(item)
        # count even
        if (item % 2) == 0:
            even_count += 1
        # count odd
        else:
            odd_count += 1

    print(f"Number Results: Even({even_count}), Odd({odd_count})")


# run function
survey_result_count()
age_data_count()
number_data_count()


