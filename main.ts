input.onButtonPressed(Button.A, function () {
    if (input.temperature() >= 27) {
        basic.showString("Bad")
    } else {
        basic.showString("Good")
    }
})
input.onButtonPressed(Button.B, function () {
    if (input.lightLevel() < 100) {
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showIcon(IconNames.Asleep)
    }
})
input.onGesture(Gesture.Shake, function () {
    basic.clearScreen()
})
