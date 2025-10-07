# Converts distance in miles to kilometers
def miles_converter(miles):
    kilometers = (miles) * 8.0 / 5.0
    print("Converting distance in miles to kilometers:")
    print("Distance in miles:     ", miles)
    print("Distance in kilometers:", kilometers)

if __name__ == "__main__":
    miles_converter(33)