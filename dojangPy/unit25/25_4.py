#25.4 dictionary 안에 dictionary 사용하기 - 중첩nested dictionary -> 계층형 data를 저장하는 경우 고려해볼만한 자료구조 (keys -> nested keys -> values)


#dictionary는 value 위치에 다시 dictionary가 들어갈 수 있다
    # dictionary = {key1: {keyA: valA}, key2: {keyB: valB}, ...}

terrestrial_planet = {
    'Mercury': {
        'radius': 1,
        'mass': 2,
        'orbit': 3
    },
    'Venus': {
        'radius': 11,
        'mass': 12,
        'orbit': 13
    },
    'Earth': {
        'radius': 21,
        'mass': 22,
        'orbit': 23
    },
    'Mars': {
        'radius': 31,
        'mass': 32,
        'orbit': 33
    }
}
print(terrestrial_planet['Venus']['radius'])    #11
print(terrestrial_planet['Earth'])  #{'radius': 21, 'mass': 22, 'orbit': 23}
