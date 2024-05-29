# Define the list of artist names
artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]

# Initialize an empty set to store unique artist names
unique_artists = set()

# Initialize a variable to track if duplicates are found
duplicates_found = False

# Loop through the list of artist names
for artist in artist_names:
    # Check if the artist is already in the unique_artists set
    if artist in unique_artists:
        duplicates_found = True
    # Add the artist to the unique_artists set
    unique_artists.add(artist)

# Display the unique artist names
print(f"Unique artist lineup: {unique_artists}")

# Confirm whether there were duplicate playlists
print(f"Duplicate playlists found: {duplicates_found}")
