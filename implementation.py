import pokemon
import stats
import moves
import type

GengarBase = stats.Stats(60, 65, 60, 130, 75, 110)
Gengar = pokemon.Pokemon("Gengar", type.Ghost, type.Poison, GengarBase)