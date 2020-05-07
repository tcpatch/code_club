import random
import logging
import datetime
import numpy as np


def set_up_logger():
    logger = logging.getLogger("temp.py")
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level=logging.DEBUG)

    return logger


def count_it(table, keys, i, j, total, count):
    if isinstance(table[keys[j]][i], float) or isinstance(table[keys[j]][i], int):
        try:
            total += table[keys[j]][i]
            count += 1.0
        except TypeError:
            pass

    return total, count


def mean_of_all_data(table, logger):
    keys = list(table.keys())
    total = 0.0
    count = 0.0
    for i in range(0, len(table[keys[0]])):
        for j in range(0, len(keys)):
            total, count = count_it(table, keys, i, j, total, count)

    logger.info('Mean of all data: {}'.format(float(total) / count))


def mean_of_each_row(table, logger):
    keys = list(table.keys())
    total = dict()
    count_dooku = dict()
    for k in keys:
        total[k] = 0.0
        count_dooku[k] = 0.0
    for i in range(0, len(table[keys[0]])):
        for j in range(0, len(keys)):
            t, c = count_it(table, keys, i, j, total[keys[j]], count_dooku[keys[j]])
            total[keys[j]] = t
            count_dooku[keys[j]] = c

    for i in range(0, len(keys)):
        logger.info("column {}'s mean: {}".format(keys[i], float(total[keys[i]]) / count_dooku[keys[i]]))


def native_python():
    logger = set_up_logger()
    logger.info('Running native_python() - implementation without any 3rd party libraries')
    logger.info('Populating 3 columns with 1,000,000 rows of random data (uniform distribution)')
    table = {'a': list(), 'b': list(), 'c': list()}
    for i in range(0, 10**6):
        table['a'].append(random.uniform(0, 100))
        table['b'].append(random.uniform(0, 100))
        table['c'].append(random.uniform(0, 100))
    logger.info('Starting to calculate mean of all data')
    start_time = datetime.datetime.now()
    mean_of_all_data(table, logger)
    end_time = datetime.datetime.now()
    total_time = end_time - start_time
    logger.info('Calculated mean of 3,000,000 floats in {}'.format(str(total_time)))
    logger.info('Native python implementation to get the mean for each column')
    start_time = datetime.datetime.now()
    mean_of_each_row(table, logger)
    end_time = datetime.datetime.now()
    total_time = end_time - start_time
    logger.info('Calculated mean of 1,000,000 floats three times in {}'.format(str(total_time)))
    return logger


def numpy_speed(logger):
    logger.info('*'*100)
    logger.info('Now running speedy numpy...')
    logger.info('Populating 3 columns with 1,000,000 rows of random data (uniform distribution)')

    # Step 1
    arr = np.random.choice(range(0, 100), size=(10**6, 3))

    logger.info('Starting to calculate mean of all data with numpy')
    start_time = datetime.datetime.now()

    # Step 3
    whole_mean = np.mean(arr)

    end_time = datetime.datetime.now()
    total_time = end_time - start_time
    logger.info('Mean of all data: {}'.format(whole_mean))
    logger.info('Calculated mean of 3,000,000 floats in {}'.format(str(total_time)))
    logger.info('Starting to calculate mean of each column with numpy')
    start_time = datetime.datetime.now()

    # Step 3
    column_a_mean, column_b_mean, column_c_mean = np.mean(arr, axis=0)

    end_time = datetime.datetime.now()
    total_time = end_time - start_time
    logger.info("Column a's mean: {}".format(column_a_mean))
    logger.info("Column b's mean: {}".format(column_b_mean))
    logger.info("Column c's mean: {}".format(column_c_mean))
    logger.info('Calculated mean of 1,000,000 floats three times in {}'.format(str(total_time)))


if __name__ == '__main__':
    logger = native_python()
    numpy_speed(logger)
