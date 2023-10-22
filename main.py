import random

sentence_starter = ["Once upon a time", "In the middle of the village", "In the beginning", "About 100 years ago"]

character = [" there was a knight. ", " there was a man. ", " there was a farmer. "]

time = ["One day ", "In the afternoon "]

story_plot = [" he was walking ", " he was thinking "]

place = [" in the city, ", " in the mountains, "]

another_character = [" when he saw a man ", " when he saw a woman "]

age = [" who seemed very young ", " who seemed very old "]

work = [" and drawing something.", " and building a house."]

story = random.choice(sentence_starter) + random.choice(character) + random.choice(time) + random.choice(story_plot) + random.choice(place) + random.choice(another_character) + random.choice(age) + random.choice(work)

print(story)