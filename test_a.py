from AdManager import AdRotator

ar = AdRotator(5)

ar.add_ad("Just do it")
ar.add_ad("Think Different")
ar.add_ad("Taste the feeling")
ar.add_ad("The Happiest Place on Earth")
ar.add_ad("Let's GO Places")
print("~"* 50)
ar.display_list()
print("="*50)
ar.rotate(8)
ar.rotate(3)
print("*"*50)
ar.add_ad("Melts in your mouth, not in  your hands") #resizes
ar.display_list()
print("#"*50)
ar.rotate(3)
ar.rotate(3)
