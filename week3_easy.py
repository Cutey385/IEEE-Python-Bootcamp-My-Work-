def string_combiner(*args) :
    sonuc = ""
    noktalama = [".", ",", "!", "?"]

    for word in args :
         if not isinstance(word , str):
             print("String dışında bir parametre girdiniz!")
             return None

         for a in noktalama :
             word = word.replace(a , "")

         sonuc = sonuc + word + " "

    sonuc += "."
    return sonuc

print(string_combiner("I.","E","!E","E"))
print(string_combiner("Mer?haba","Dünya!"))
