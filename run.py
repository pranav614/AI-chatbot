from flask import Flask, render_template, request
app = Flask(__name__)

import textwrap

import google.generativeai as genai

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key="AIzaSyCs-HIBoYQaBMH4OXkmpIdXFVEOxtADNZI")

## Function to load OpenAI model and get respones

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response=get_gemini_response(userText)
    return response

if __name__ == "__main__":
    app.run()
