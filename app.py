from taipy import Gui
def operate(state):
    v1 = float(state.value1)
    v2 = float(state.value2)
    op = state.value
    result = 0
    if op == "Subtract(-)":
        result = v1 - v2
    elif op == "Multiply(x)":
        result = v1 * v2
    elif op == "Add(+)":
        result = v1 + v2
    elif op == "Divide(/)":
        result = v1 / v2 if v2 != 0 else "Error (Divide by zero)"
    state.result = f"The answer is: {result}"
def clear(state):
    state.value1 = 1
    state.value2 = 1
    state.value = "Subtract(-)"
    state.result = ""
value1 = 1
value2 = 1
value = "Subtract(-)"
result = ""
page = '''
<|text-center|
# Welcome to our simple calculator

Enter your first number  
<|{value1}|number|>

Enter your second number  
<|{value2}|number|>

Choose operation  
<|{value}|selector|lov=Subtract(-);Multiply(x);Add(+);Divide(/)|>

<|Calculate|button|on_action=operate|>
<|Reset|button|on_action=clear|>
<|{result}|>

Note: This website is made by Rishabh, a 10 year old child and I've setted a world record that is the youngest person to make a website
>
'''
if __name__ == "__main__":
    Gui(page).run(title="Simple Calculator by Rishabh Birthalia", port=1000, use_reloader=True)