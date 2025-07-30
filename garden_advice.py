# Get season and plant type from user.
season = input("Please select the season (spring, summer, autum, winter): ")
plant_type = input("Please select the plant type (flower, vegetable, fruit: )")

# Variable to hold gardening advice
advice = ""

# Change the code
# Use git add .
# Use git commit -m "message"
# Push the new branch to GitHub (git push orign new_branch_name)
# On GitHub in the browser create the pull request
# Merge and close the pull request on GitHub including a keyword such as Fix... to automatically close the related issue
# Check the "Issues" tab and ensure the issue is closed


def get_gardening_advice(season, plant_type):
    advice = ""

    if season == "summer":
        advice += "Water plants regularly and provide shade.\n"
    elif season == "winter":
        advice += "Protect plants from frost with covers.\n"
    else:
        advice += "No seasonal advice.\n"

    if plant_type == "flower":
        advice += "Use fertiliser for blooms."
    elif plant_type == "vegetable":
        advice += "Watch out for pests!"
    else:
        advice += "No plant type advice."    
    return advice


print(get_gardening_advice("summer", "flower"))
print(get_gardening_advice("winter", "vegetable"))
print(get_gardening_advice("spring", "tree"))

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
