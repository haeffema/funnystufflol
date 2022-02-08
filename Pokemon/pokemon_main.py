import pokemon
import type
import stats
import moves

if __name__ == '__main__':
    Gengar = pokemon.Pokemon("Gengar", type.Ghost, type.Poison, stats.Stats(45, 95, 50, 40, 50, 75), 100)
    Dragoran = pokemon.Pokemon("Dragoran", type.Dragon, type.Flying, stats.Stats(45, 95, 50, 40, 50, 75), 100)
    Gengar.calculate_damage(moves.ShadowBall, Dragoran)
    #print(pokemon.get_pokemon_from_txt('test.txt'))
