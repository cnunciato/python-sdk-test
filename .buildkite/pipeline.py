from buildkite_sdk import Pipeline

pipeline = Pipeline()
pipeline.add_step({
    'commands': [
        'cat /etc/os-release'
    ],
    # 'image': 'ubuntu:24.04'
})

print(pipeline.to_yaml())
