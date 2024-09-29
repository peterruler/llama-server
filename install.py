from langchain_community.llms.mlx_pipeline import MLXPipeline

pipe = MLXPipeline.from_model_id(
    "mlx-community/Llama-3.1-SuperNova-Lite-4bit",
    pipeline_kwargs={"max_tokens": 10, "temp": 0.1},
)
    