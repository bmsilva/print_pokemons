import os
import argparse

from pogo.trainer import Trainer
from pogo.api import PokeAuthSession
from pogo.pokedex import pokedex


def main():

    parser = argparse.ArgumentParser(description='Print your pokemon go list.')
    parser.add_argument('--keyfile', action='store', dest='keyfile',
                        default='keyfile')
    parser.add_argument('--family', action='append', dest='families',
                        default=[])
    parser.add_argument('--pokemon', action='append', dest='pokemons',
                        default=[])

    args = parser.parse_args()

    families = [x.upper() for x in args.families]
    pokemons = [x.upper() for x in args.pokemons]

    if not os.path.isfile(args.keyfile):
        print("keyfile not found")
        return

    username, password = get_credentials_from_keyfile(args.keyfile)

    trainer = get_trainer(username, password)

    lst = get_pokemons(trainer)


    print_pokemons_by_iv(lst, pokemons, families)


def print_pokemons_by_iv(lst, pokemons=[], families=[], segments=(90, 82, 0)):
    if pokemons:
        lst = [p for p in lst if p['name'] in pokemons]

    if families:
        lst = [p for p in lst if p['family'] in families]

    lst.sort(key=lambda x: (x['%'], x['cp']))
    lst.reverse()
    
    sep = '-'*(110)
    print('{:>3} | {:>15} | {:>4} | {:>4} | {:>8} | {:>8} | {:>8} | {:>8} | '
          '{:>8} | {:>8} | {}'.format('id', 'name', 'cp', 'hp', 'attack',
                                      'defense', 'stamina', '%', 'candies',
                                      'n_evolves', 'family'))
    print(sep)
    
    curr_segment = 0
    counter = 0

    for (i, p) in enumerate(lst, start=1):
        if p['%'] > segments[curr_segment]:
            counter += 1
        else:
            print('Sub total: {}'.format(counter))
            print(sep)
            curr_segment += 1
            counter = 1
        print('{id:>3} | {name:>15} | {cp:>4} | {hp:>4} | {attack:>8} | '
              '{defense:>8} | {stamina:>8} | {%:>8.3f} | {candies:>8} | '
              '{n_evolves:>8} | {family}'.format(**p))

    print('Sub total: {}'.format(counter))
    print('Pokemons Total: {}'.format(len(lst)))


def get_credentials_from_keyfile(keyfile):
    with open(keyfile) as fh:
        line = fh.readline().strip()
        username, password = line.split('|')
    return (username, password)


def get_trainer(username, password):
    auth_session = PokeAuthSession(username, password, 'google',
                                   'libencrypt.so', geo_key=None)
    session = auth_session.authenticate()
    return Trainer(auth_session, session)


def get_pokemons(trainer):
    inventory = trainer.session.getInventory()

    lst = []

    for p in inventory.party:
        candies = inventory.candies.get(pokedex.families[p.pokemon_id], 0)
        evolves = pokedex.evolves[p.pokemon_id]
        n_evolves = 0
        iv_percent = ( 
            (p.individual_attack + 
             p.individual_defense + 
             p.individual_stamina) / 45 * 100)
        if evolves:
            n_evolves = int(candies / pokedex.evolves[p.pokemon_id])
        d = {
            'id': p.pokemon_id,
            'name': pokedex[p.pokemon_id],
            'cp': p.cp, 
            'hp': p.stamina, 
            'attack': p.individual_attack, 
            'defense': p.individual_defense, 
            'stamina': p.individual_stamina,
            '%': iv_percent,
            'family': pokedex[pokedex.families[p.pokemon_id]],
            'candies': candies,
            'evolves': evolves,
            'n_evolves': n_evolves,
        }
        lst.append(d)

    return lst


if __name__ == '__main__':
    main()
