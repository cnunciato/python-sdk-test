from buildkite_sdk import Pipeline

pipeline = Pipeline()
pipeline.add_step({
    'commands': [
        'lsb_release -ds'
    ],
    'image': 'ubuntu:24.04'
})

print(pipeline.to_yaml())
