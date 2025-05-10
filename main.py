class Field():
    y_coords = {
        'А': 1,
        'Б': 2,
        'В': 3,
        'Г': 4,
        'Д': 5,
        'Е': 6,
        'Ж': 7,
        'З': 8,
        'И': 9,
        'К': 10,
    }

    player_field_body, ai_field_body = (
        [[0 for i in range(10)] for j in range(10)],
        [[0 for i in range(10)] for j in range(10)]
    )

    def __init__(self):
        ...

    def show_field(self):
        space = '        '
        print(f'{space}Player Field')
        for i in self.player_field_body:
            print('  '.join(str(item) for item in i))
        print()
        print(f'{space}AI Field')
        for i in self.ai_field_body:
            print('  '.join(str(item) for item in i))

a = Field()

a.show_field()