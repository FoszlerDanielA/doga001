import ember_o

Ember = ember_o.Ember(int(input("Adja meg az életkort")), int(input("Adja meg a magasságot")), int(input("Adja meg a tudásszintet")),
                      input("Adja meg a nemet"), input("Adja meg a családnevet"),input("Adja meg a keresztnevet"),
                      int(input("Adja meg a testsúlyt")))

print(Ember.Kiir())

