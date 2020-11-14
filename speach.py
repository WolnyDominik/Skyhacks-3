import io
import os

from pydub import AudioSegment
outputs = []
columns2 = ['park rozrywki', 'zwierzęta', 'ławka', 'budynek', 'zamek',
       'jaskinia', 'kościół', 'miasto', 'krzyż', 'instytucja kultury', 'jedzenie',
       'Ścieżka', 'Las', 'Meble', 'Trawa', 'Cmentarz', 'Jezioro',
       'krajobraz', 'kopalnia', 'Pomnik', 'Pojazd mechaniczny', 'Góry', 'Muzeum',
       'Skansen', 'Park', 'Człowiek', 'Rośliny', 'Zbiornik', 'Rzeka',
       'Droga', 'Skały', 'Śnieg', 'Sport', 'Obiekt sportowy', 'Schody', 'Drzewa',
       'Statek', 'Okna']
columns = [['lunapark','wesołe miasteczko', "park rozrywki"],
        ['ryb','wąż','sarna','ptaki','pies','kot', 'przyro'],
        ['siedzi','ławka','zydel'],
        ["apartamentowiec", "biurowiec", "bliźniak", "blok", "blokhauz", "bungalow", "ceglak", "czynszówka", "dacza", "dom", "domek", "domostwo", "drapacz chmur", "dworzyszcze", "gmach", "kamienica", "murowaniec", "nieruchomość", "piętrowiec", "segment", "szeregowiec", "wieżowiec", "apartament", "budowla", "chata", "mieszkanie", "pałac", "rezydencja", "willa", "zamek", "bloczysko"],
        ['zamek', 'dworek', 'cytadela', 'baszta', 'flanki', 'mur', 'blanki', 'łucznicy'],
        ["czeluść", "głębia", "grota", "jama", "jamka", "lej", "leże", "loch", "nora", "norka", "otwór", "pieczara", "rozpadlina", "szczelina", "wgłębienie", "wgłębienie skalne", "wykrot", "wyrwa", "zagłębienie", "załamanie"],
        ["archikatedra", "bazylika", "modlitwy", "pański",  "boży", "wiara", "świątynia", "chrześcijanie", "wierni", "wspólnota"],
        ["aglomeracja", "betonowa dżungla", "metropolia", "miasteczko", "miejscowość", "mieścina", "osada", "osiedle", "wioska", "cywilizacja", "konurbacja", "urbanizacja", "katowice", "częstochowa", "sosnowiec", "gliwice"],
        ["krzyż"],
        ["kino", "muzeum", "biblioteka", "opera", "operetka", "filharmonia", "teatr", "orkiestra", "kultury", "artystyczne", "galeria", "sztuki"],
        ["jedzenie", "zjeść", "pożywienie"],
        ["ścieżka", "chodnik", "deptak"],
        ["bór", "las","dżungla", 'przyro', "gaj","knieja","laseczek","lasek","łęg","młodnik","puszcza","regiel","selwa","tajga","zagaj","zagajnik","zalesienie"],
        ["mebelki", "sprzęty", "umeblowanie", "wyposażenie", "wystrój", "zabudowa", "stół", "krzeslo", "łóżk", "szafk"],
        ["kwietnik","murawa","trawnik","darnina", "natur", "sielsk"],
        ["grób", "groby", "cmentarz", "polegl"],
        ["woda", "akwen", "bagno", "bajoro", "glinianka", "jeziorko", "mulisko", "oczko wodne", "sadzawka", "staw", "zarośnięte jezioro", "zarośnięty staw", "obszar wodny", "zalew", "zalewisko", "zbiornik wody", "jeziorzysko", "szot", "szott"],
        ["obraz", "panorama", "scena", "widok", "wizja", "okolica", "pejzaż", "perspektywa", "sceneria", "plener", "widoczek", "otwarta przestrzeń", "przestrzeń", "środowisko", "pejzażyk"],
        [ "kwk", "wegięl", "kamienny", "wieliczka", "źródło", "hawiernia", "sztolnia", "zakład górniczy"],
        ["cenotaf", "dolmen", "figura", "kamień nagrobny", "monument", "nagrobek", "obelisk", "pamiątka", "pomniczek", "posąg", "rzeźba", "statua", "bałwan", "figurka", "figurynka", "monolit", "popiersie", "statuetka", "totem", "epitafium", "inskrypcja nagrobna"],
        ["auto", "automobil", "bryczka", "bryka", "czterokołowiec", "dwuślad", "dwuśladowiec", "fura", "gablota", "limuzyna", "maszyna", "osobówka", "pojazd", "samochodzik", "samochód", "środek transportu", "wóz", "wózek", "środek lokomocji", "motor"],
        ["czub", "czubek", "góra", "górotwór", "grań", "grzbiet", "kalenica", "koniec góry", "masyw", "masyw górski", "pagórek", "pasmo", "szczyt", "szpic", "turnia", "wierch", "wierzchołek", "wzgórze", "wzniesienie"],
        ["galeria", "kolekcja", "kolekcja dzieł", "pinakoteka", "salon wystawowy", "wernisaż", "wystawa", "zbiór", "zbiór dzieł sztuki", "gliptoteka", "panoptikum", "park etnograficzny"],
        ["anachronizm", "archaizm", "przeżytek", "relikt", "relikt przeszłości", "skansen", "staroć", "staroświecczyzna", "zabytek"],
        
        ]
def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    from google.cloud import speech

    client = speech.SpeechClient()

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=44100,
        language_code="pl-PL",
        audio_channel_count = 2,
        enable_word_time_offsets=True,
    )

    response = client.recognize(config=config, audio=audio)


    for result in response.results:
            alternative = result.alternatives[0]
            print("Transcript: {}".format(alternative.transcript))
          #  print("Confidence: {}".format(alternative.confidence))

            for word_info in alternative.words:
                word = word_info.word
                start_time = word_info.start_time
                end_time = word_info.end_time
                outputs.append([word.lower(), start_time.total_seconds(), end_time.total_seconds()])
src = "test.mp3"
dst = "test.flac"
startSec = 0
endSec = 30
startTime = startSec*1000
endTime = endSec*1000
song = AudioSegment.from_mp3( src )
extract = song[startTime:endTime]
extract.export(dst, format="flac")
transcribe_file("test.flac")
for key, j in enumerate(outputs):
    for i in range(14):
        for element in columns[i]:
            try:
              if((j[0].find(element))!=-1):
                 print(outputs[key][1])
                 print(outputs[key][2])
                # print(columns[i])
            except:
                pass
            

