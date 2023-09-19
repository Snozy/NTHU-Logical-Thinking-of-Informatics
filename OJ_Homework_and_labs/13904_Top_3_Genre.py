"""
Dead Poets Society,comedy|drama,8.1
Inception,action|thriller,8.8
Eternal Sunshine of the Spotless Mind,sci-fi|drama,8.3
The Shining,horror|thriller,8.4


action,8.80
thriller,8.60
horror,8.40
number = 7.9775609756097534 

truncated_number = int(number * 100) / 100

truncated_number = "{:.2f}".format(truncated_number)

print(truncated_number) // truncated_number will be 7.97
"""
genre_ratings = {}

while True:
    try:
        inputs = input().split(",")
        name, genre_str, rating = inputs[0], inputs[1], float(inputs[2])
        genres = genre_str.split("|")
        for genre in genres:
            if genre not in genre_ratings:
                genre_ratings[genre] = []
            genre_ratings[genre].append(rating)
    except:
        break

sorted_genres = sorted(genre_ratings.items(), key=lambda x: (-sum(x[1]) / len(x[1]), x[0]), reverse=False)
#print(sorted_genres)

for i, (genre, ratings) in enumerate(sorted_genres[:3]):
    average_rating = sum(ratings) / len(ratings)
    average_rating = int(average_rating * 100)/100
    average_rating = "{:.2f}".format(average_rating)
    sorted_genres[i] = (genre, (average_rating,))

#print(sorted_genres)

for item in sorted_genres[:3]:
    print(f"{item[0]},{item[1][0]}")
