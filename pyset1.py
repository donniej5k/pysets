# Define the sets of flight destinations for both airlines
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# Destinations that both airlines fly to (intersection)
common_destinations = our_routes.intersection(competitor_routes)
print(f"Destinations both airlines fly to: {common_destinations}")

# Destinations unique to our airline (difference)
unique_to_our_airline = our_routes.difference(competitor_routes)
print(f"Destinations unique to our airline: {unique_to_our_airline}")

# Check if there are destinations neither airline shares
all_destinations = {"LAX", "JFK", "CDG", "DXB", "LHR", "BKK"}  # This should include all possible destinations
neither_shared = all_destinations.difference(our_routes.union(competitor_routes))
print(f"Destinations neither airline shares: {neither_shared}")
