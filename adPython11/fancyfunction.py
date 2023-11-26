def timezone_decorator(func):
    def wrapper(*args, **kwargs):
        print("I am a decorator")
        func(*args, **kwargs)

    return wrapper


@timezone_decorator
def show_location(country: str, city: str) -> None:
    print(f"I'm travelling in {city} of {country}")
