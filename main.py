def on_gesture_screen_up():
    basic.show_number(randint(1, 6))
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)
