import pokemon
import stats
import moves
import type

for x in type.types:
    print(x.name + ": " + str(pokemon.Dragoran.calculateEffecticityForPokemon(x)))
