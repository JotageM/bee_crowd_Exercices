vert_invert = input()
type = input()
food = input()

if vert_invert == "vertebrado" and type == "ave" and food == "carnivoro":
    animal = "aguia"
if vert_invert == "vertebrado" and type == "ave" and food == "onivoro":
    animal = "pomba"
if vert_invert == "vertebrado" and type == "mamifero" and food == "onivoro":
    animal = "homem"
if vert_invert == "vertebrado" and type == "mamifero" and food == "herbivoro":
    animal = "vaca"
if vert_invert == "invertebrado" and type == "inseto" and food == "hematofago":
    animal = "pulga"
if vert_invert == "invertebrado" and type == "inseto" and food == "herbivoro":
    animal = "lagarta"
if vert_invert == "invertebrado" and type == "anelideo" and food == "hematofago":
    animal = "sanguessuga"
if vert_invert == "invertebrado" and type == "inseto" and food == "onivoro":
    animal = "minhoca"

print(animal)



