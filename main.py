from motogp import bike


def main():
    # Print Riders's bike info
    print_riders_bike_info()


def print_riders_bike_info():
    mm93 = bike.honda('RC213V')
    ad04 = bike.ducati('GP20')
    ar42 = bike.suzuki()
    mv12 = bike.yamaha('A Spec')
    pe44 = bike.ktm()
    ae41 = bike.aprilia()

    print(f'Marc Marquez : {mm93.show_bike_detail()}')
    print(f'Andrea Dovizioso : {ad04.show_bike_detail()}')
    print(f'Alex Rins : {ar42.show_bike_detail()}')
    print(f'Maverick Vinales : {mv12.show_bike_detail()}')
    print(f'Pol Espagaro : {pe44.show_bike_detail()}')
    print(f'Aliex Espagaro : {ae41.show_bike_detail()}')


if __name__ == "__main__":
    main()
