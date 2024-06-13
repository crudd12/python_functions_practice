def hello():
    print('Hello Courtney!')

hello()

def pack(movie, color, animal):
    return[movie, color, animal]

print(pack('Selena', 'red', 'husky'))

def eat_lunch(food):
    if not food:
        print('My lunchbox is empty!')
    else:
        print(f'First I eat {food[0]}')
        for item in food[1:]:
            print(f'Next I eat {item}')

eat_lunch(['burger', 'fries', 'donut'])

eat_lunch([])

