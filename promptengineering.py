import tkinter as tk
import openai
from tkinter import font

# Replace 'your_api_key' with your actual API key
openai.api_key = ""
variations = []


def generate_text(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Create and extend 4 diffrent variation of a question based on this question: {prompt} Your answers will be split with one new line"}
        ]
    )
    return completion.choices[0].message.content.split('\n')


def gen_questions():
    prompt = entry.get()
    variations = generate_text(prompt)
    print(variations)
    variations = list(filter(lambda x: x != '', variations))
    for i, label in enumerate(labels):
        label.config(text=variations[i])


def gen_a():
    label_texts = [label.cget("text") for label in labels]

    print(label_texts)
    for i, response_label in enumerate(response_labels):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                    "content": f"Anwser me this: {label_texts[i]}"}
            ]
        )

        response_label.config(text=completion.choices[0].message.content)


def on_key(event):
    if event.keysym == 'enter':
        gen_questions()


app = tk.Tk()
app.title("Simple GUI App")

entry = tk.Entry(app, width=50)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entry.bind("<Key>", on_key)

button = tk.Button(app, text="Generate Questions", command=gen_questions)
button.grid(row=1, column=0, columnspan=3)

buttonAnswer = tk.Button(
    app, text="Generate Anwser to the Generated Questions", command=gen_a)
buttonAnswer.grid(row=1, column=1, columnspan=3)
custom_font = font.Font(size=12)
labels = []
response_labels = []

for i in range(4):
    label = tk.Label(app, text="", width=40, height=10,
                     relief="groove", wraplength=250, font=custom_font, justify='center')
    label.grid(row=2, column=i, padx=10, pady=5)
    labels.append(label)
    response_label = tk.Label(app, text="", width=None, height=None, relief="groove",
                              wraplength=150, font=custom_font, justify='center')
    response_label.grid(row=3, column=i, padx=5, pady=5)
    response_labels.append(response_label)
app.mainloop()
