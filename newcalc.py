import pokemon
import moves

def damage_calc(move, attacker, defender):
    a = 2 * attacker.level
    b = a / 5
    c = b + 2
    if move.damagetyp == 'Special':
        d = c * move.damage * attacker.stats.spezattack / defender.stats.spezdef
    else:
        d = c * move.damage * attacker.stats.physattack / defender.stats.physdef
    e = d / 50 + 2
    TYPE = defender.calculateEffecticityForPokemon(move.type)
    STAB = 1
    if attacker.firstType == move.type or attacker.secondType == move.type:
        STAB = 1.5
    damagelow = round(e * STAB * TYPE * 0.85)
    damagemax = round(e * STAB * TYPE)
    print(f'Min Damage: {round(damagelow/defender.stats.hp * 100, 1)}%, {damagelow} hp')
    print(f'Max Damage: {round(damagemax/defender.stats.hp * 100, 1)}%, {damagemax} hp')

damage_calc(moves.ShadowBall, pokemon.Gengar, pokemon.Dragoran)