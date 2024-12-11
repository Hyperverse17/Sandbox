
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
        0:{
            "title":"Capítulo 0",
            "page":14,
            "abstract":"Saul y Maxi..."
        },
        1:{
            "title":"Vuelta al ruedo",
            "page":23,
            "abstract":"Isaac Zarco..."
        },
        2:{
            "title":"La promesa",
            "page":87,
            "abstract":""
        },
        3:{
            "title":"Mentes abiertas",
            "page":119,
            "abstract":""
        },
        4:{
            "title":"Interludio",
            "page":143,
            "abstract":""
        },
        5:{
            "title":"Esa noche",
            "page":153,
            "abstract":""
        },
        6:{
            "title":"La probable irresponsabilidad de un padre",
            "page":196,
            "abstract":""
        },
        7:{
            "title":"Esa noche",
            "page":153,
            "abstract":""
        },
        8:{
            "title":"Esa noche",
            "page":153,
            "abstract":""
        },
        9:{
            "title":"Esa noche",
            "page":153,
            "abstract":""
        },
        10:{
            "title":"Esa noche",
            "page":153,
            "abstract":""
        },
        11:{
            "title":"Esa noche",
            "page":153,
            "abstract":""
        },
        12:{
            "title":"Esa noche",
            "page":153,
            "abstract":""
        },
        13:{
            "title":"Esa noche",
            "page":153,
            "abstract":""
        },
        14:{
            "title":"Esa noche",
            "page":153,
            "abstract":""
        },
        15:{
            "title":"Esa noche",
            "page":153,
            "abstract":""
        },
        16:{
            "title":"Esa noche",
            "page":153,
            "abstract":""
        },
        17:{
            "title":"Esa noche",
            "page":153,
            "abstract":""
        },
        18:{
            "title":"Esa noche",
            "page":153,
            "abstract":""
        },
        19:{
            "title":"Esa noche",
            "page":153,
            "abstract":""
        },
        20:{
            "title":"Esa noche",
            "page":153,
            "abstract":""
        },
        21:{
            "title":"Esa noche",
            "page":153,
            "abstract":""
        },
        22:{
            "title":"Esa noche",
            "page":153,
            "abstract":""
        },
        23:{
            "title":"Esa noche",
            "page":153,
            "abstract":""
        },
        24:{
            "title":"Esa noche",
            "page":153,
            "abstract":""
        },
        25:{
            "title":"Esa noche",
            "page":153,
            "abstract":""
        },
        26:{
            "title":"Esa noche",
            "page":153,
            "abstract":""
        }
    }
}

def getChapter(chapter,dataString):
    chapterN = book1.get("chapters")[chapter]
    chapterValue = chapterN[dataString]
    return chapterValue

def getChapterLenght(chapterA,chapterB):
    pageA = book1.get("chapters")[chapterA]["page"]
    pageB = book1.get("chapters")[chapterB]["page"]
    difference = abs(pageB-pageA)

    return difference


try:
    bookValue = getChapter(6,"page")
    print(bookValue)
    
    diff = getChapterLenght(5,3)
    print(diff)

except(KeyError):
    print("Capitulo inexistente")


    