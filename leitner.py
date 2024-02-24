import pandas as pd


def add_new_words(df):
    n_rows = len(df)
    b = True
    while b is True:
        b_user_continuing = (
            bool(
                int(
                    input("Enter 1 if you would like to add a " +
                          "new word. Otherwise, enter 0: "))))
        if b_user_continuing:
            french_english = input("Enter the French or English expression: ")
            german = input("Enter the German expression: ")
            df.loc[n_rows] = [french_english, german, 1, '1']
            n_rows += 1
        else:
            b = False


def main():
    df = pd.DataFrame(columns=['French/English', 'German', 'Current_Level',
                               'Level_Log'])
    add_new_words(df)
    print(df)
    add_new_words(df)
    print(df)


if __name__ == '__main__':
    main()

# %% Next steps
'''
1) Save & import df

2) make calendar three columns with
    1st column: day
    2nd column: level
    3rd column: completed

3) def revise(calendar, df)
        searches first 'False' in calendar -> 'Level_to_train'
        makes sub data frame of df only keeping rows with
        'Current_Level' == 'Level_to_train'
        if correct, adds one to current level, else sets it to 1
        adds new level to Level_Log

4) Could add column to df counting number of times a mistake was made for that
   word. (would be nice but is not a priority)
'''

# def add_new_word(french_english: str, german: str, df):
#     df.loc[-1] = [french_english, german, 1, '1']
#     df.index = df.index + 1

# add_new_word('je', 'ich', df)
# add_new_word('tu', 'du', df)
# df = df.sort_index()
