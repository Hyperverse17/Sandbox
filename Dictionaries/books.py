
book1 = {
    "title":"La Chica Gris",
    "author":"Antonio Runa",
    "year":"2022",
    "publisher":"Minotauro",
    "country":"Spain",
    "languaje":"Spanish",
    "ISBN":{
        "phisical":"9788445014752",
        "digital":"[???]"
    },
    "chapters":{
        1:"Capítulo 0",
        2:"Vuelta al ruedo",
        3:"La promesa",
        4:"Mentes abiertas",
        5:"Interludio",
        6:"Esa noche"
    }
}

currentBook = book1.get("title")
print(currentBook)

ISBN = book1["ISBN"]["phisical"]
print(ISBN)

currentChapter = book1["chapters"][6]
print(currentChapter)

currentChapter = book1.get("chapters")[3]
print(currentChapter)
