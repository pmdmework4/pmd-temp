def on_button_pressed_a():
    if input.temperature() >= 27:
        basic.show_string("Bad")
    else:
        basic.show_string("Good")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if input.light_level() < 100:
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.ASLEEP)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
