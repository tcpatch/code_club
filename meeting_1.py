"""
CodeClub Meeting #1

. Puppy and/or Kitten?
- You pick up two random animals from a box. If both animals are a kitten,
  return True. If both animals are a puppy return True. If one animal is a
  puppy and one animal is a kitten, return False.

2. Flip a Coin
- Flip a coin 100 times, return the percentage of total flips that the coin
  landed on heads, and the percentage of total flips the coin landed on tails.
ex. 10 heads -> 10% heads, 90% tails
"""

import argparse
from random import randrange


def get_animals():
    convert_dict = {0: 'puppy', 1: 'kitten'}
    animal_1 = convert_dict[randrange(2)]
    animal_2 = convert_dict[randrange(2)]
    return animal_1, animal_2


def puppy_or_kitten():
    print('Running Question 1: Puppy or Kitten')
    print('Picking two animals from a box...')
    animal_1, animal_2 = get_animals()
    print('Animals picked: {}, {}'.format(animal_1, animal_2))
    if len(set([animal_1, animal_2])) == 1:
        ret = True
    else:
        ret = False
    return ret


def coin_flip(n_times=100):
    print('Running Question 2: Coin flipping')
    coin_dict = {0: 'heads', 1: 'tails'}
    heads_count = 0
    tails_count = 0
    total = 0
    print('Flipping a coint {} times'.format(n_times))
    for i in range(0, n_times):
        flip = coin_dict[randrange(2)]
        if flip == 'heads':
            heads_count += 1
        else:
            tails_count += 1
        total += 1
    percent_heads = int(round(float(heads_count) / float(total) * 100, 0))
    percent_tails = int(round(float(tails_count) / float(total) * 100, 0))
    print(('Percent flips landing on heads: {}%\n'
           'Percent flips landing on tails: {}%').format(percent_heads,
                                                         percent_tails))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CodeClub #1')
    parser.add_argument('-a', '--a', action='store_true', help='Run #1 (puppy \
                        or kitten)', required=False)
    parser.add_argument('-b', '--b', action='store_true', help='Run #2 (coin)',
                        required=False)
    parser.add_argument('-n_flips', '--n_flips', type=int, default=100,
                        help='Number of flips to run')
    args = parser.parse_args()
    if args.a:
        val = puppy_or_kitten()
        print('Value returned: {}'.format(val))
    if args.a and args.b:
        print('-'*35)
    if args.b:
        coin_flip(args.n_flips)

