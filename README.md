# ezKey

*ezkey* is a Python package that allows developers to easily manage locally stored API keys. It is designed to be used with the Command Line application [*ezKeyVault*](https://github.com/espressoAndCode/ezkeyvault)


## Getting Started

This project has two parts
  - ezKeyVault - a CLI based key manager where the user can add and view their API keys. This is for local use only on a developer's machine, and is installed only once.
  ezKeyVault creates a simple key/value store that writes a hidden text file in the user's home directory. ezKeyVault does not encrypt any content, it's sole purpose is to facilitate separation of the keys from the working code. Once a key is added to the ezKeyVault, it can be accessed from any project on the user's machine via the *ezKey* `pip` module.

  - ezKey - a `pip` module that the user can add to their projects to facilitate easy access to their API keys during development.

### Prerequisites

You will need Python 2 or 3 on your system to use this software. ezKeyVault and ezKey were built on OSX and should work on any *.nix machine.

Be sure to install ezkeyvault as described in the repo linked [here](https://github.com/espressoAndCode/ezkeyvault).

### Installation

Install ezkey by running:

```
pip install ezkey
```

### Documentation

Once ezKeyVault and ezKey are installed on your system, you can import ezkey into your project and use the `getkey` method to retrieve any API keys that are stored in the ezKeyVault. You must first run ezkeyvault and store one or more API Keys in order to use them with ezkey.

**ezKey and ezKeyVault are not designed for production use. Do not use these modules on a production server.** The ezKey and ezKeyVault modules are created solely for convenience to help beginning developers quickly and easily store their API keys in a path outside of their projects, and reduce the chance of accidentally uploading keys to a public repository. This project does not include any encryption, obfuscation, or security measures of any kind, and should only be used for local key management on a developer's machine.

```
from ezkey import getkey

  mykey = getkey('Google')
  print("Mykey: ", mykey)
  #Use mykey wherever you need the API Key
```

- Note - if you attempt to retrieve a key using an incorrect name, ezkey will return the string:

```
"Error - Key not found"
```

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details

