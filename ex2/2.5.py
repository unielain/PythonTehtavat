# a simple program to convert old units to grams and kilograms

talent = float(input("Give talents: "))
pound = float(input("Give pounds: "))
plumb = float(input("Give plumbs: "))

plumb_in_grams = 13.3
pound_in_grams = 32 * plumb_in_grams
talent_in_grams = 20 * pound_in_grams
grams = (talent * talent_in_grams) + (pound * pound_in_grams) + (plumb * plumb_in_grams)

kgs = grams // 1000
grams_formatted = "{:.2f}".format(grams - (kgs * 1000))
kgs_formatted = int(kgs)
print(f"Mass in modern units:"
      f"\n{kgs_formatted} kg and {grams_formatted} g.")