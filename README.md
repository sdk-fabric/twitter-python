
# Twitter SDK

This SDK is managed by the [SDK Fabric](https://sdk-fabric.org/) project.
Our goal is to build a global infrastructure to automatically generate
an SDK for every API, please take a look at our website for more information.

## Contribution

Please do not create a pull requests at this repository since the code is
automatically generated. If an operation or type is missing at the client SDK
please register at the [TypeHub](https://typehub.cloud/) platform and create
a pull request at the [Twitter](https://app.typehub.cloud/d/sdkfabric/twitter)
specification. The system will then automatically create a GIT commit and update
the code.

## Usage

The following example shows how you initialize the client:

```python
from sdk.client import Client

client = Client.build("[access_token]")

// @TODO use the client
```

You can find all available operations and types at:
https://app.typehub.cloud/d/sdkfabric/twitter
