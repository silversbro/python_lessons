from sub_transport import PassengerBoat, PassengerPlane, PassengerCar
from transport import Trasporters, Сrossover
from exceptions import exceptions_transport as Ex


def main():
    product_1 = Сrossover('Toyota Prado', 5, 'Robot', 3)
    product_2 = PassengerBoat('Doral Prestancia', 10, '1.04 m')
    product_3 = PassengerPlane('Boeing 777X', 350)
    product_4 = Сrossover('Creta', 0, 'Robot', 3)

    product_1.close_dors()
    product_1.fasten_belts()
    product_1.start_engine()
    product_1.start_moving()
    print(product_1.caclc_power_reserve(20, 30))
    print(product_1)

    print(product_2)

    trasropter = Trasporters()
    trasropter += product_1
    trasropter += product_2

    print(trasropter.items)
    print(product_3.calculate_bagage_weith(20, 150))
    print(trasropter.total_capacity())

    print(product_4.carrying_capacity)


if __name__  == '__main__':
    try:
        main()
    except Ex.SeatsValueException as e:
        print(f'Error contruct class: {e.args}')
    except Ex.MovingException as e:
        print(e)
    except Exception as e:
        print(e)

