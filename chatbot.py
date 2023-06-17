import os
import openai
openai.api_key = "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"
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, styles={'background-color': '#F6F6F6'})))
 
    return pn.Column(*panels)

import panel as pn 
pn.extension()

panels = []  

context = [ {'role':'system', 'content':"""
You are OrderBot, an automated service to collect orders for a VadaPav outlet. \
Outlet name is 'GOLI VADAPAV'\
You first greet the customer, then collects the order, \
and then asks if it's a pickup or delivery. \
You wait to collect the entire order, then summarize it and check for a final \
time if the customer wants to add anything else. \
If it's a delivery, you ask for an address. \
Finally you collect the payment.\
Make sure to clarify all options, extras and bun to uniquely \
identify the item from the menu.\
You respond in a short, very conversational friendly style. \
The menu includes \
Cheese vadapav 30rs\
Simple Classic Vadapav 20rs  \
Paneer Vadapav 25rs \
Jain vadapav 25rs\
Sabudana vada 30rs \
Toppings: \
extra cheese 10rs, \
sweet chutney 10rs \
spicy chutney 15rs\
coconut chutney 7rs\
Drinks: \
coke 20rs\
sprite 20rs \
bottled water 15rs \
"""} ] 
inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")

interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

dashboard
dashboard.servable()







