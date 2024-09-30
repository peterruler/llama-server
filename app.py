from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.widgets import TextArea
from wtforms import SubmitField, StringField
from langchain_community.llms.mlx_pipeline import MLXPipeline
from mlx_lm import load
from langchain_core.prompts import PromptTemplate

def return_prediction(sample_json):
    
    req1 = sample_json['req1']

    model, tokenizer = load("mlx-community/Llama-3.1-SuperNova-Lite-4bit")
    pipe = MLXPipeline(model=model, tokenizer=tokenizer)

    template = """Question: {question}

    Answer: Let's think step by step."""
    prompt = PromptTemplate.from_template(template)

    chain = prompt | pipe

    predict = chain.invoke({"question":req1}).lstrip()
    
    return predict

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class LlmForm(FlaskForm):
    req1 = StringField('Input Text:', widget=TextArea())
    submit = SubmitField('Run Llama')

@app.route('/', methods=['GET', 'POST'])
def index():

    form = LlmForm()
    if form.validate_on_submit():

        session['req1'] = form.req1.data

        return redirect(url_for("prediction"))

    return render_template('home.html', form=form)


@app.route('/prediction')
def prediction():
    content = {}

    content['req1'] = session['req1']
    result = return_prediction(sample_json=content)
    return render_template('prediction.html',results=result)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5001) 