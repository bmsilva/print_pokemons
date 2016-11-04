import os
import argparse

from collections import UserDict

from pogo.trainer import Trainer
from pogo.api import PokeAuthSession
from pogo.pokedex import pokedex



class Types(UserDict):
    UNKNOWN = 0
    GRASS = 1
    POISON = 2
    FIRE = 3
    WATER = 4
    BUG = 5
    FLYING = 6
    NORMAL = 7
    ELECTRIC = 8
    GROUND = 9
    FAIRY = 10
    FIGHTING = 11
    PSYCHIC = 12
    STEEL = 13
    GHOST = 14
    ROCK = 15
    ICE = 16
    DRAGON = 17

    ALL_TYPES = {
        UNKNOWN: 'UNKNOWN',
        GRASS: 'GRASS',
        POISON: 'POISON',
        FIRE: 'FIRE',
        WATER: 'WATER',
        BUG: 'BUG',
        FLYING: 'FLYING',
        NORMAL: 'NORMAL',
        ELECTRIC: 'ELECTRIC',
        GROUND: 'GROUND',
        FAIRY: 'FAIRY',
        FIGHTING: 'FIGHTING',
        PSYCHIC: 'PSYCHIC',
        STEEL: 'STEEL',
        GHOST: 'GHOST',
        ROCK: 'ROCK',
        ICE: 'ICE',
        DRAGON: 'DRAGON',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data.update({
            pokedex.BULBASAUR: [Types.GRASS, Types.POISON],
            pokedex.IVYSAUR: [Types.GRASS, Types.POISON],
            pokedex.VENUSAUR: [Types.GRASS, Types.POISON],
            pokedex.CHARMANDER: [Types.FIRE],
            pokedex.CHARMELEON: [Types.FIRE],
            pokedex.CHARIZARD: [Types.FIRE],
            pokedex.SQUIRTLE: [Types.WATER],
            pokedex.WARTORTLE: [Types.WATER],
            pokedex.BLASTOISE: [Types.WATER],
            pokedex.CATERPIE: [Types.BUG],
            pokedex.METAPOD: [Types.BUG],
            pokedex.BUTTERFREE: [Types.BUG, Types.FLYING],
            pokedex.WEEDLE: [Types.BUG, Types.POISON],
            pokedex.KAKUNA: [Types.BUG, Types.POISON],
            pokedex.BEEDRILL: [Types.BUG, Types.POISON],
            pokedex.PIDGEY: [Types.NORMAL, Types.FLYING],
            pokedex.PIDGEOTTO: [Types.NORMAL, Types.FLYING],
            pokedex.PIDGEOT: [Types.NORMAL, Types.FLYING],
            pokedex.RATTATA: [Types.NORMAL],
            pokedex.RATICATE: [Types.NORMAL],
            pokedex.SPEAROW: [Types.NORMAL, Types.FLYING],
            pokedex.FEAROW: [Types.NORMAL, Types.FLYING],
            pokedex.EKANS: [Types.POISON],
            pokedex.ARBOK: [Types.POISON],
            pokedex.PIKACHU: [Types.ELECTRIC],
            pokedex.RAICHU: [Types.ELECTRIC],
            pokedex.SANDSHREW: [Types.GROUND],
            pokedex.SANDSLASH: [Types.GROUND],
            pokedex.NIDORAN_FEMALE: [Types.POISON],
            pokedex.NIDORINA: [Types.POISON],
            pokedex.NIDOQUEEN: [Types.POISON, Types.GROUND],
            pokedex.NIDORAN_MALE: [Types.POISON],
            pokedex.NIDORINO: [Types.POISON],
            pokedex.NIDOKING: [Types.POISON, Types.GROUND],
            pokedex.CLEFAIRY: [Types.FAIRY],
            pokedex.CLEFABLE: [Types.FAIRY],
            pokedex.VULPIX: [Types.FIRE],
            pokedex.NINETALES: [Types.FIRE],
            pokedex.JIGGLYPUFF: [Types.NORMAL, Types.FAIRY],
            pokedex.WIGGLYTUFF: [Types.NORMAL, Types.FAIRY],
            pokedex.ZUBAT: [Types.POISON, Types.FLYING],
            pokedex.GOLBAT: [Types.POISON, Types.FLYING],
            pokedex.ODDISH: [Types.GRASS, Types.POISON],
            pokedex.GLOOM: [Types.GRASS, Types.POISON],
            pokedex.VILEPLUME: [Types.GRASS, Types.POISON],
            pokedex.PARAS: [Types.BUG, Types.GRASS],
            pokedex.PARASECT: [Types.BUG, Types.GRASS],
            pokedex.VENONAT: [Types.BUG, Types.POISON],
            pokedex.VENOMOTH: [Types.BUG, Types.POISON],
            pokedex.DIGLETT: [Types.GROUND],
            pokedex.DUGTRIO: [Types.GROUND],
            pokedex.MEOWTH: [Types.NORMAL],
            pokedex.PERSIAN: [Types.NORMAL],
            pokedex.PSYDUCK: [Types.WATER],
            pokedex.GOLDUCK: [Types.WATER],
            pokedex.MANKEY: [Types.FIGHTING],
            pokedex.PRIMEAPE: [Types.FIGHTING],
            pokedex.GROWLITHE: [Types.FIRE],
            pokedex.ARCANINE: [Types.FIRE],
            pokedex.POLIWAG: [Types.WATER],
            pokedex.POLIWHIRL: [Types.WATER],
            pokedex.POLIWRATH: [Types.WATER, Types.FIGHTING],
            pokedex.ABRA: [Types.PSYCHIC],
            pokedex.KADABRA: [Types.PSYCHIC],
            pokedex.ALAKAZAM: [Types.PSYCHIC],
            pokedex.MACHOP: [Types.FIGHTING],
            pokedex.MACHOKE: [Types.FIGHTING],
            pokedex.MACHAMP: [Types.FIGHTING],
            pokedex.BELLSPROUT: [Types.GRASS, Types.POISON],
            pokedex.WEEPINBELL: [Types.GRASS, Types.POISON],
            pokedex.VICTREEBEL: [Types.GRASS, Types.POISON],
            pokedex.TENTACOOL: [Types.WATER, Types.POISON],
            pokedex.TENTACRUEL: [Types.WATER, Types.POISON],
            pokedex.GEODUDE: [Types.ROCK, Types.GROUND],
            pokedex.GRAVELER: [Types.ROCK, Types.GROUND],
            pokedex.GOLEM: [Types.ROCK, Types.GROUND],
            pokedex.PONYTA: [Types.FIRE],
            pokedex.RAPIDASH: [Types.FIRE],
            pokedex.SLOWPOKE: [Types.WATER, Types.PSYCHIC],
            pokedex.SLOWBRO: [Types.WATER, Types.PSYCHIC],
            pokedex.MAGNEMITE: [Types.ELECTRIC, Types.STEEL],
            pokedex.MAGNETON: [Types.ELECTRIC, Types.STEEL],
            pokedex.FARFETCHD: [Types.UNKNOWN],
            pokedex.DODUO: [Types.NORMAL, Types.FLYING],
            pokedex.DODRIO: [Types.NORMAL, Types.FLYING],
            pokedex.SEEL: [Types.WATER],
            pokedex.DEWGONG: [Types.WATER],
            pokedex.GRIMER: [Types.POISON],
            pokedex.MUK: [Types.POISON],
            pokedex.SHELLDER: [Types.WATER],
            pokedex.CLOYSTER: [Types.WATER],
            pokedex.GASTLY: [Types.GHOST, Types.POISON],
            pokedex.HAUNTER: [Types.GHOST, Types.POISON],
            pokedex.GENGAR: [Types.GHOST, Types.POISON],
            pokedex.ONIX: [Types.ROCK, Types.GROUND],
            pokedex.DROWZEE: [Types.PSYCHIC],
            pokedex.HYPNO: [Types.PSYCHIC],
            pokedex.KRABBY: [Types.WATER],
            pokedex.KINGLER: [Types.WATER],
            pokedex.VOLTORB: [Types.ELECTRIC],
            pokedex.ELECTRODE: [Types.ELECTRIC],
            pokedex.EXEGGCUTE: [Types.GRASS, Types.PSYCHIC],
            pokedex.EXEGGUTOR: [Types.GRASS, Types.PSYCHIC],
            pokedex.CUBONE: [Types.GROUND],
            pokedex.MAROWAK: [Types.GROUND],
            pokedex.HITMONLEE: [Types.FIGHTING],
            pokedex.HITMONCHAN: [Types.FIGHTING],
            pokedex.LICKITUNG: [Types.NORMAL],
            pokedex.KOFFING: [Types.POISON],
            pokedex.WEEZING: [Types.POISON],
            pokedex.RHYHORN: [Types.GROUND, Types.ROCK],
            pokedex.RHYDON: [Types.GROUND, Types.ROCK],
            pokedex.CHANSEY: [Types.UNKNOWN],
            pokedex.TANGELA: [Types.GRASS],
            pokedex.KANGASKHAN: [Types.UNKNOWN],
            pokedex.HORSEA: [Types.WATER],
            pokedex.SEADRA: [Types.WATER],
            pokedex.GOLDEEN: [Types.WATER],
            pokedex.SEAKING: [Types.WATER],
            pokedex.STARYU: [Types.WATER],
            pokedex.STARMIE: [Types.WATER, Types.PSYCHIC],
            pokedex.MR_MIME: [Types.PSYCHIC, Types.FAIRY],
            pokedex.SCYTHER: [Types.BUG, Types.FLYING],
            pokedex.JYNX: [Types.ICE, Types.PSYCHIC],
            pokedex.ELECTABUZZ: [Types.ELECTRIC],
            pokedex.MAGMAR: [Types.FIRE],
            pokedex.PINSIR: [Types.BUG],
            pokedex.TAUROS: [Types.UNKNOWN],
            pokedex.MAGIKARP: [Types.WATER],
            pokedex.GYARADOS: [Types.WATER, Types.FLYING],
            pokedex.LAPRAS: [Types.UNKNOWN],
            pokedex.DITTO: [Types.UNKNOWN],
            pokedex.EEVEE: [Types.NORMAL],
            pokedex.VAPOREON: [Types.WATER],
            pokedex.JOLTEON: [Types.ELECTRIC],
            pokedex.FLAREON: [Types.FIRE],
            pokedex.PORYGON: [Types.NORMAL],
            pokedex.OMANYTE: [Types.ROCK, Types.WATER],
            pokedex.OMASTAR: [Types.ROCK, Types.WATER],
            pokedex.KABUTO: [Types.ROCK, Types.WATER],
            pokedex.KABUTOPS: [Types.ROCK, Types.WATER],
            pokedex.AERODACTYL: [Types.ROCK, Types.FLYING],
            pokedex.SNORLAX: [Types.NORMAL],
            pokedex.ARTICUNO: [Types.UNKNOWN],
            pokedex.ZAPDOS: [Types.UNKNOWN],
            pokedex.MOLTRES: [Types.UNKNOWN],
            pokedex.DRATINI: [Types.DRAGON],
            pokedex.DRAGONAIR: [Types.DRAGON],
            pokedex.DRAGONITE: [Types.DRAGON],
            pokedex.MEWTWO: [Types.UNKNOWN],
            pokedex.MEW: [Types.UNKNOWN],
        })


def main():

    parser = argparse.ArgumentParser(description='Print your pokemon go list.')
    parser.add_argument('--keyfile', action='store', dest='keyfile',
                        default='keyfile')
    parser.add_argument('--family', action='append', dest='families',
                        default=[])
    parser.add_argument('--pokemon', action='append', dest='pokemons',
                        default=[])

    parser.add_argument('--action', action='store', dest='action', default='by_iv')

    args = parser.parse_args()

    families = [x.upper() for x in args.families]
    pokemons = [x.upper() for x in args.pokemons]

    if not args.action:
        requested_action = 'by_iv'
    else:
        requested_action = args.action

    if not os.path.isfile(args.keyfile):
        print("keyfile not found")
        return

    username, password, auth_type = get_credentials_from_keyfile(args.keyfile)

    trainer = get_trainer(username, password, auth_type)

    lst = get_pokemons(trainer)


    if requested_action == 'by_iv':
        print_pokemons_by_iv(lst, pokemons, families)
    else:
        print_pokemons_by_number(lst)


def print_pokemons_by_iv(lst, pokemons=[], families=[], segments=(90, 82, 0)):
    if pokemons:
        lst = [p for p in lst if p['name'] in pokemons]

    if families:
        lst = [p for p in lst if p['family'] in families]

    lst.sort(key=lambda x: (x['%'], x['cp']))
    lst.reverse()
    
    sep = '-'*(110)
    print('{:>3} | {:>15} | {:>4} | {:>4} | {:>8} | {:>8} | {:>8} | {:>7} | '
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
              '{defense:>8} | {stamina:>8} | {%:>7.2f} | {candies:>8} | '
              '{n_evolves:>8} | {family}'.format(**p))

    print('Sub total: {}'.format(counter))
    print('Pokemons Total: {}'.format(len(lst)))


def print_pokemons_by_number(lst):
    lst.sort(key=lambda x: (x['id'],x['%'], x['cp']))

    sep = '-'*(110)
    print('{:>3} | {:>15} | {:>4} | {:>4} | {:>8} | {:>8} | {:>8} | {:>8} | {:>8} | {:>8} | {}'.format(
        'id', 'name', 'cp', 'hp', 'attack', 'defense', 'stamina', '%', 'candies', 'n_evolves', 'family'))
    print(sep)

    curr_family = ''
    counter = 0

    for (i, p) in enumerate(lst, start=1):
        if not curr_family:
            curr_family=p['family']

        if p['family'] != curr_family:
            curr_family=p['family']
            print('')

        print('{id:>3} | {name:>15} | {cp:>4} | {hp:>4} | {attack:>8} | {defense:>8} | {stamina:>8} | {%:>8.3f} | {candies:>8} | {n_evolves:>8} | {family}'.format(**p))

    print('Sub total: {}'.format(counter))
    print('Pokemons Total: {}'.format(len(lst)))


def get_credentials_from_keyfile(keyfile):
    username = ''
    password = ''
    auth_type = 'google'
    with open(keyfile) as fh:
        line = fh.readline().strip()
        credentials = line.split('|')
        if len(credentials) == 2:
            username, password = credentials
        elif len(credentials) == 3:
            username, password, auth_type = credentials
        else:
            raise ValueError('Invalid keyfile')
    return (username, password, auth_type)


def get_trainer(username, password, auth_type='google'):
    auth_session = PokeAuthSession(username, password, auth_type,
                                   'libencrypt.so', geo_key=None)
    session = auth_session.authenticate()
    return Trainer(auth_session, session)


def get_pokemons(trainer):
    inventory = trainer.session.getInventory()

    lst = []

    for p in inventory.party:
        family = pokedex.families[p.pokemon_id]
        n_candies = inventory.candies.get(p.pokemon_id, 0)
        need = pokedex.evolves.get(p.pokemon_id, 0)
        iv_percent = ( 
            (p.individual_attack + 
             p.individual_defense + 
             p.individual_stamina) / 45 * 100)
        n_evolves = 0
        if need:
            n_evolves = int(n_candies / need)
        d = {
            'id': p.pokemon_id,
            'name': pokedex[p.pokemon_id],
            'cp': p.cp, 
            'hp': p.stamina, 
            'attack': p.individual_attack, 
            'defense': p.individual_defense, 
            'stamina': p.individual_stamina,
            '%': iv_percent,
            'family': pokedex[family],
            'candies': n_candies,
            'need': need,
            'n_evolves': n_evolves,
        }
        lst.append(d)

    return lst


if __name__ == '__main__':
    main()
