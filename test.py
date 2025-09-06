import gradio as gr
import hidden
from openai import OpenAI

client = OpenAI(api_key=hidden.openai_api_key)


start_sequence = "\nAI:"
restart_sequence = "\nHuman: "


def gpt_output(prompt):
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    return response.choices[0].text.strip()

def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ''.join(s)
    output = gpt_output(inp)
    history.append((input, output))
    return history, history

block = gr.Blocks()

with block:
    gr.Markdown("""<h1><center>AGI AI Assistant</center></h1>""")
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder="Enter a question")
    state = gr.State()
    submit = gr.Button("Send")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug=True)
