# -*- coding: utf-8 -*-
from pydblite.sqlite import Database, Table


db = Database((":memory:"))

def open_fizzbuzz_table():
    """
    Create main fizzbuzz table. Open if table already exists.
    """
    table = Table('fct_fizzbuzz', db)
    table.create(
        ('id', 'INTEGER PRIMARY KEY'),
        ('run_id', 'TEXT'),
        ('file_name', 'TEXT'),
        ('file_path', 'TEXT'),
        ('total_rows', 'INTEGER'),
        ('valid_rows', 'INTEGER'),
        ('invalid_rows', 'INTEGER'),
        ('run_start', 'INTEGER'),
        ('run_end', 'INTEGER'),
        ('run_time_in_seconds', 'INTEGER'),
        mode="open"
    )

    # Transform run_start and run_end into datetime columns
    table.is_datetime('run_start')
    table.is_datetime('run_end')
    
    table.commit()

    return table


def open_fizzbuzz_errors_table():
    """
    Create fizzbuzz errors table. Open if table already exists.
    """
    table = Table('fct_fizzbuzz_errors', db)
    table.create(
        ('id', 'INTEGER PRIMARY KEY'),
        ('run_id', 'TEXT'),
        ('invalid_row', 'INTEGER'),
        ('error', 'TEXT'),
        mode="open"
    )
    table.commit()

    return table


def open_fizzbuzz_tfms_table():
    """
    Create fizzbuzz transformations table. Open if table already exists.
    """
    table = Table('fct_fizzbuzz_transformations', db)
    table.create(
        ('id', 'INTEGER PRIMARY KEY'),
        ('run_id', 'TEXT'),
        ('tfm_type', 'TEXT'),
        ('original', 'BLOB'),
        ('transformed', 'BLOB'),
        mode="open"
    )
    db.commit()

    return table


def check_if_valid(row):
    """
    Check that all requirements on row are met
    Return true if all requirements are met
    """
    if not all(str(x).isdigit() for x in row) or len(row) != 20:
        return False
    else:
        return True


def get_error_code(row):
    """
    Given error, return error code
    """
    if not all(str(x).isdigit() for x in row):
        return 'non_integer'
    
    if len(row) != 20:
        return 'column_error'


def transform1(x):
    """
    Given an input value, transforms data with transformation logic 1
    Returns a new list of transformed values
    """
    x = int(x)

    # Transform into 'fizz' for multiples of 3
    if x % 15 == 0:
        return 'fizzbuzz'

    # Transform into 'buzz' for multiples of 5
    elif x % 5 == 0:
        return 'buzz'

    # Transform into 'fizzbuzz' for multiples for 15
    elif x % 3 == 0:
        return 'fizz'

    # If no criteria is met, then return original value
    else:
        return x


def transform2(x):
    """
    Given an input value, transforms data with transformation logic 2
    Returns the transformed value
    """
    # If number contains 3, transform into 'lucky'
    if '3' in str(x):
        return 'lucky'
    
    # If no criteria is met, then return value based on transformation logic 1
    else:
        return transform1(x)


def transform3(row):
    """
    Given an input row, transforms data with transformation logic 1
    Returns a new list of transformed values
    """
    # Initialize variables
    fizz = 0
    buzz = 0
    fizzbuzz = 0
    lucky = 0
    integer = 0

    # Iterate over elements in row and count each keyword
    for i in row:
        if i == 'fizz':
            fizz += 1

        elif i == 'buzz':
            buzz += 1

        elif i == 'fizzbuzz':
            fizzbuzz += 1
        
        elif i == 'lucky':
            lucky +=1

        else:
            integer += 1

    # Contruct report
    report = {
        'fizz': fizz,
        'buzz': buzz,
        'fizzbuzz': fizzbuzz,
        'lucky': lucky,
        'integer': integer
    }

    # Return report
    return report
