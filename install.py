from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.widgets import TextArea
from wtforms import SubmitField, StringField
from langchain_community.llms.mlx_pipeline import MLXPipeline

pipe = MLXPipeline.from_model_id(
    "mlx-community/Llama-3.1-SuperNova-Lite-4bit",
    pipeline_kwargs={"max_tokens": 10, "temp": 0.1},
)
    