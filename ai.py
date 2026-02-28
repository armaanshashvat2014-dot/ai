// Initial greeting
game.splash("Hi, I am an AI that solves addition")

// Use a forever loop so the AI keeps asking for new numbers
forever(function () {
    // 1. Ask the user for the first number and store it
    let num_1 = game.askForNumber("Enter first number:")
    
    // 2. Ask for the second number and store it
    let num_2 = game.askForNumber("Enter second number:")
    
    // 3. Calculate the sum
    let sum = num_1 + num_2
    
    // 4. Show the final answer
    // We combine text and the sum variable using the '+' sign
    game.splash(num_1 + " + " + num_2 + " = " + sum)
})
