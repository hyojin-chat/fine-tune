import openai
import streamlit as st

model_name = "davinci:ft-personal-2023-02-08-03-42-24"

def generate_response(prompt):
    completion = openai.Completion.create(model=model_name, prompt=prompt)
    text = completion.choices[0]["text"]
    return text

st.title("Fine-tuned ChatGPT")

prompt = st.text_input("Enter your prompt:")

if prompt:
    response = generate_response(prompt)
    st.write("Response:", response)

    # Make the completion request
    completion = openai.Completion.create(model=model_name, prompt=prompt)

    # Clear the input field
    input_field.delete(0, "end")

    # Get the completion text from the first choice in the choices list
    text = completion.choices[0]["text"]

    # Display the completion in the result text area
    result_text.config(state="normal")
    result_text.delete("1.0", "end")
    result_text.insert("end", text)
    result_text.config(state="disabled")

# Create the main window
window = tk.Tk()
window.title("Fine-tuned ChatGPT")

# Create the input field and submit button
input_field = tk.Entry(window)
submit_button = tk.Button(window, text="Submit", command=on_submit)

# Create the result text area
result_text = tk.Text(window, state="disabled", width=80, height=20)

# Add the input field, submit button, and result text area to the window
input_field.pack()
submit_button.pack()
result_text.pack()

# Run the main loop
window.mainloop()
