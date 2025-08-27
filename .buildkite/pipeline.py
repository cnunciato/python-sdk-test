from buildkite_sdk import Pipeline

pipeline = Pipeline()
pipeline.add_step({
    'commands': [
        'curl -LsSf https://astral.sh/uv/install.sh | sh',
        'source $$HOME/.local/bin/env',
        'uv python install',
        'uv run main.py'
    ],
    'image': 'ubuntu:24.04'
})

print(pipeline.to_yaml())
