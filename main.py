import meteor_data_class

# makes empty lists to hold filtered values
mass_list = []
year_list = []
print('Welcome to the Meteorite Sorting Program!\n'
      'This program prints out user specified tables based on the categories and parameters passed into it.')
print('Written by Charlie Dakai in October 2023\n')
while True:
    file_input = input('Enter a valid file name (ex. "file_name.txt") with its file extension if applicable |or| \n'
                       'Enter "<q" or "<Q" to quit the program: ')
    if file_input.upper() == '<Q':
        print('Exiting the program. Goodbye!')
        break
    else:
        print()
        print('Target File: ', file_input)
        print()
    mode_input = input('Please enter a mode to open the file in.\n'
                       "'r':" ' open for reading (default)\n'
                       "'w':" ' open for writing, truncating the file first\n'
                       "'x':" ' open for exclusive creation, failing if the file already exists\n'
                       "'a':" ' open for writing, appending to the end of file if it exists\n'
                       "'b':" ' binary mode\n'
                       "'t':" ' text mode (default)\n'
                       "'+':" ' open for updating (reading and writing)\n'
                       'Enter <q or <Q to quit the program: ')
    if mode_input.upper() == '<Q':
        print('Exiting the program. Goodbye!')
        break
    else:
        print()
        print('File Mode: ', mode_input)
        print()
        
    category_input = input('What attribute would u like to filter the data on?\n'
                           '1. meteor MASS (g)\n'
                           '2. The YEAR the meteor fell\n'
                           '3. QUIT\n'
                           '>>')
    if category_input == '1':
        lower_limit_input = input('Enter the LOWER limit (inclusive) for the meteors mass(g) ("Q" to quit): ')
        if lower_limit_input == 'Q':
            print('Exiting the program. Goodbye!')
            break
        upper_limit_input = input('Enter the UPPER limit (inclusive) for the meteors mass(g) ("Q" to quit): ')
        if upper_limit_input == 'Q':
            print('Exiting the program. Goodbye!')
            break
        file = open(file_input, mode_input)
        with file as text_file:
            file.readline()
            for line in file:
                split_list = line.strip('\n').split('\t')
                for i in range(12):
                    if len(split_list) < 12:
                        split_list.append('')
                    else:
                        pass
                meteor_object = meteor_data_class.MeteorDataEntry(split_list[0], split_list[1], split_list[2],
                                                                  split_list[3],
                                                                  split_list[4], split_list[5], split_list[6],
                                                                  split_list[7],
                                                                  split_list[8], split_list[9], split_list[10],
                                                                  split_list[11])
    # mass filter
                if meteor_object.mass == '':
                    continue
                elif float(lower_limit_input) < float(meteor_object.mass) < float(upper_limit_input):
                    mass_list.append(meteor_object.name + ', ' + meteor_object.mass)
        print('=' * 40)
        print(' ' * 2, 'Name', ' ' * 21, 'Mass (g)', ' ' * 16)
        print('=' * 40)
        count = 1
        for i in range(len(mass_list)):
            splitMass = mass_list[i].split(',')
            print(f'{count:2} {splitMass[0]:25} {splitMass[1]:10}')
            count = count + 1
        break
    elif category_input == '2':
        low_year_input = input('Enter the LOWER limit for the meteors YEAR (inclusive) (Q to quit): ')
        if low_year_input == 'Q':
            print('Exiting the program. Goodbye!')
            break
        high_year_input = input('Enter the UPPER limit for the meteors YEAR (inclusive) (Q to quit): ')
        if high_year_input == 'Q':
            print('Exiting the program. Goodbye!')
            break
        file = open(file_input, mode_input)
        with file as text_file:
            file.readline()
            for line in file:
                split_list = line.strip('\n').split('\t')
                for i in range(12):
                    if len(split_list) < 12:
                        split_list.append('')
                    else:
                        pass
                meteor_object = meteor_data_class.MeteorDataEntry(split_list[0], split_list[1], split_list[2],
                                                                  split_list[3],
                                                                  split_list[4], split_list[5], split_list[6],
                                                                  split_list[7],
                                                                  split_list[8], split_list[9], split_list[10],
                                                                  split_list[11])
        # year filter
                if meteor_object.year == '':
                    continue
                elif int(high_year_input) > int(meteor_object.year) >= int(low_year_input):
                    year_list.append(meteor_object.name + ',' + meteor_object.year)
        # year table
        year_count = 1
        print('=' * 40)
        print(' ' * 2, 'Name', ' ' * 20, 'Year', ' ' * 16)
        print('=' * 40)
        for i in range(len(year_list)):
            splitYear = year_list[i].split(',')
            print(f'{year_count:2} {splitYear[0]:25} {splitYear[1]:5}')
            year_count = year_count + 1
        break
    elif category_input == '3':
        print('Exiting the program. Goodbye!')
        break








