# -*- coding: utf-8 -*-
import csv, os, uuid
from datetime import datetime
from . import helpers


def run(filepath):

    # Start time
    run_start = datetime.now()

    # Test and open filepath
    file = csv.reader(open(filepath, 'r'))
    filename = os.path.basename(filepath)

    # Generate unique run id
    run_id = str(uuid.uuid4())

    # Initialize variables
    count = 0
    error_count = 0

    # Initialize lists
    tfm_list = list()
    errors_list = list()

    # Iterate over rows in file
    for row in file:
        count += 1

        # Validate row is valid
        if helpers.check_if_valid(row):

            # Transformation 1 logic - append to list with transformed values
            tfm1 = [helpers.transform1(x) for x in row]
            tfm_list.append(
                {'run_id': run_id, 'tfm_type': 'tfm1', 'original': repr(row),
                'transformed': repr(tfm1)}
            )

            # Transformation 2 logic - append to list with transformed values
            tfm2 = [helpers.transform2(x) for x in row]
            tfm_list.append(
                {'run_id': run_id, 'tfm_type': 'tfm2', 'original': repr(tfm1),
                'transformed': repr(tfm2)}
            )

            # Transformation 3 logic - append to list with transformed values
            tfm3 = helpers.transform3(tfm2)
            tfm_list.append(
                {'run_id': run_id, 'tfm_type': 'tfm3', 'original': repr(tfm2),
                'transformed': repr(tfm3)}
            )
            
        # Add to errors count and append to list if not valid
        else:
            error_count += 1
            errors_list.append(
                {'run_id': run_id, 'invalid_row': count, 'error': helpers.get_error_code(row)}
            )

    # End Time
    run_end = datetime.now()

    # Open fizzbuzz table, insert fizzbuzz report, and commit changes 
    fizzbuzz_table = helpers.open_fizzbuzz_table().open()
    fizzbuzz_table.insert(
        run_id=run_id,
        file_name=filename,
        file_path=filepath,
        total_rows=count,
        valid_rows=count - error_count,
        invalid_rows=error_count,
        run_start=run_start,
        run_end=run_end,
        run_time_in_seconds=(run_end - run_start).total_seconds()
    )
    fizzbuzz_table.commit()

    # Open errors table, insert errors list, and commit changes
    fizzbuzz_errors_table = helpers.open_fizzbuzz_errors_table().open()
    fizzbuzz_errors_table.insert(errors_list)
    fizzbuzz_errors_table.commit()

    # Open transformations table, insert transformations list, and commit changes
    fizzbuzz_tfm_table = helpers.open_fizzbuzz_tfms_table().open()
    fizzbuzz_tfm_table.insert(tfm_list)
    fizzbuzz_tfm_table.commit()
