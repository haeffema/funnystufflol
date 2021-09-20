attackstat = 479
defstat = 171
hp = 285
stab = 1.5
attackdmg = 120
effectiv = 2
damagemax = ((42 * attackdmg * attackstat/defstat)/50)*stab*effectiv
damagemin = damagemax*0.85
percent = round(damagemax/hp * 100, 2)
percentmin = round(damagemin/hp * 100, 2)
print("The Attack will do between " + str(percentmin)+ "% and " + str(percent) + "% damage")
