from collections import Counter
from app.models.random_users import RandomUserResponse
from app.models.names_occurrences import NamesOccurrencesResponse, NameOccurrence
from pydantic import ValidationError

def process_random_user_response(data):
    """
    Process the data returned by the Random User API and return names with their occurrences sorted.
    """
    # Validate the response using the Pydantic model
    try:
        validated_data = RandomUserResponse(**data)
    except ValidationError as e:
        raise ValueError({"error": "Invalid API response", "details": e.errors()})

    # Extract names
    names = [user.name.first for user in validated_data.results]

    # Count occurrences
    name_counts = Counter(names)

    # Sort by occurrences in descending order
    sorted_name_counts = sorted(name_counts.items(), key=lambda x: x[1], reverse=True)

    # Format as a list of NameOccurrence dictionaries
    name_occurrences = [NameOccurrence(name=name, count=count) for name, count in sorted_name_counts]

    # Validate with NamesOccurrencesResponse model
    response_model = NamesOccurrencesResponse(names=name_occurrences)

    return response_model
