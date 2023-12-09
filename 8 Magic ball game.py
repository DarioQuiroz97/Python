import random

# Solicitar al usuario que ingrese su nombre y pregunta
name = input("Enter your name: ")
question = input("Ask the Magic 8-Ball a Yes or No question: ")

answer = ""  # Variable para almacenar la respuesta de la bola 8

# Generar un número aleatorio
random_number = random.randint(1, 9)

# Asignar respuestas basadas en el número aleatorio
if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
else:
    answer = "Error"

# Mostrar el resultado
if name != "":
    print(f"{name} asks: {question}")
else:
    print(f"Question: {question}")

if question != "":
    print(f"Magic 8-Ball's answer: {answer}")
else:
    print("Please provide a question for the Magic 8-Ball.")
