import gradio as gr
import hidden
from openai import OpenAI

client = OpenAI(api_key=hidden.openai_api_key)


start_sequence = "\nAI:"
restart_sequence = "\nHuman: "


def gpt_output(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6
    )
    return response.choices[0].message.content.strip()

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
