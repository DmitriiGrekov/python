heroes = {
        'Spider-man':80,
        'Batman':65,
        'Superman':85,
        'Wonder Woman':70,
        'Flash':70,
        'Iron Man':65,
        'Thor':90,
        'Aquaman':65,
        'Captain America':65,
        'Hulk':87,
        }



for i in sorted(heroes.items(),key=lambda para:(para[1],para[0])):
    print(i)
