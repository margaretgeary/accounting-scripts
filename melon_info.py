"""Print out all the melons in our inventory."""

from melons import melon_dict

def print_melon(melon_dict):
    """Print each melon name with corresponding attributes."""

    for name, attributes in melon_dict.items():
        print(name.upper())

        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')

        print("**************************")

print_melon(melon_dict)

# def print_melon(name, seedless, price):
#     """Print each melon with corresponding attribute information."""

#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
