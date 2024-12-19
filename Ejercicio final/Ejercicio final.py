
import requests
import random

def main():
    nombre = input("Introduce tu nombre: ")
    print(f"¡Bienvenido, {nombre}! Vamos a comenzar el juego.\n")
    response = requests.get("https://opentdb.com/api.php?amount=15&category=23&difficulty=easy&type=multiple")
    preguntas = response.json()['results']

    puntos = 0
    for trivia in preguntas:
        pregunta = trivia['question']
        correcta = trivia['correct_answer']
        incorrectas = trivia['incorrect_answers']

        print(f"Pregunta: {pregunta}")
        opciones = incorrectas + [correcta]
        random.shuffle(opciones)

        for i, opcion in enumerate(opciones):
            print(f"{i + 1}. {opcion}")
        respuesta_usuario = int(input("Elige la opción correcta del 1 al 4: "))
        if opciones[respuesta_usuario - 1] == correcta:
            puntos += 1
            print(f"CORRECTA. Puntuación actual: {puntos} puntos.")
        else:
            print(f"INCORRECTA. La respuesta correcta era {correcta}")
            puntos = 0
            break



    print(f"Juego terminado. Tu puntuación final es: {puntos} puntos.")

if __name__ == "__main__":
    main()
