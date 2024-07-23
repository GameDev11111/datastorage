def on_button_pressed_a():
    with open('story.txt') as my_file:
        content = my_file.read()
    print(content)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    pass
basic.forever(on_forever)
