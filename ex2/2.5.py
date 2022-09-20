
leiviska = float(input("Anna leiviskät."))
naula = float(input("Anna naulat."))
luoti = float(input("Anna luodit."))

luoti2 = 13.3
naula2 = 32 * luoti2
leiviska2 = 20 * naula2
grammat = (leiviska * leiviska2) + (naula * naula2) + (luoti * luoti2)
kilot = grammat // 1000
grammat2 = "{:.2f}".format(grammat - (kilot * 1000))
kilot = int(kilot)
print(f"Massa nykymittojen mukaan:\n {kilot} kilogrammaa ja {grammat2} grammaa.")