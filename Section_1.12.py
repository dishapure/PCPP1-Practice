def show_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

def create_profile(**info):
    # Forward keyword arguments to show_profile
    show_profile(**info)

# Test it
create_profile(name="Disha", age=20, city="San Antonio")
