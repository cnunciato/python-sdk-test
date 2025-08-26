from buildkite_sdk import Pipeline

pipeline = Pipeline()
pipeline.add_step({
    'commands': [
        'uv run main.py'
    ]
})

print(pipeline.to_json())
