notasW = {
    "A": [{"info":{"oitava":3,"freq":220}},{"info":{"oitava":4,"freq":440}},{"info":{"oitava":5,"freq":880}}],
    "B": [{"info":{"oitava":3,"freq":246.9417}},{"info":{"oitava":4,"freq":493.8833}},{"info":{"oitava":5,"freq":987.7666}}],
    "C": [{"info":{"oitava":4,"freq":130.8128}},{"info":{"oitava":5,"freq":523.2511}},{"info":{"oitava":6,"freq":1108.73}}],
    "D": [{"info":{"oitava":4,"freq":146.8324}},{"info":{"oitava":5,"freq":587.3295}},{"info":{"oitava":6,"freq":587.3295}}],
    "E": [{"info":{"oitava":4,"freq":164.8138}},{"info":{"oitava":5,"freq":587.3295}},{"info":{"oitava":6,"freq":659.2551}}],
    "F": [{"info":{"oitava":4,"freq":174.6141}},{"info":{"oitava":5,"freq":587.3295}},{"info":{"oitava":6,"freq":698.4565}}],
    "G": [{"info":{"oitava":4,"freq":195.9977}},{"info":{"oitava":5,"freq":587.3295}},{"info":{"oitava":6,"freq":783.9909}}]
    }
print(notasW)
print(notasW["A"])
print(notasW["A"][0])
print(notasW["A"][0]["info"]["freq"])

print("\nutilizando range():\n")
for x in range(0, 7):
    print("Estamos na iteração %d" % (x))
print("\nPercorrendo uma lista:\n")
colecao = ['oi', 5, 'último da lista']
for x in colecao:
    print(x)
s="fritzkliewer"
print("\nPercorrendo a string %s\n" %(s))
for x in s:
  print(x)

