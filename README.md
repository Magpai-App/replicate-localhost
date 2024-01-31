# Replicate Localhost

[Replicate.com](https://replicate.com) is great! Their creation of [cog](https://github.com/replicate/cog) is great!

However sometimes, users want to run AI locally.

Sure they can crank open the command line, download docker, download cog, run cog, but thats a lotta effort.

Why cant there be a one-click tool that spins up, checks everything is installed and setup, and then listen for replicate predictions or any model?

I think there probably can be!

This is just a test. But we need something to solve this for [magpai.app](https://magpai.app), so we're playing around with this...

## Running Server

`flask --app server run`

## Problems

### Prediction API endpoint doesnt include model and user name needed for cog/docker

The replicate prediction endpoint is `https://api.replicate.com/v1/predictions`, where the model version is a POST body object `"version"`. 

However, running a model locally via cog or docker, you need to know the user name, and the model name to run the image. 
e.g. `r8.im/magpai-app/cog-ffmpeg@sha256:efd0b79b577bcd58ae7d035bce9de5c4659a59e09faafac4d426d61c04249251`.

Maybe I'm missing something, but I can't find a way to find that url without running a prediction on replicate....

### How do we know which inputs are files

File inputs via CLI require an @ prefix, it's not clear how we find this out... But also, this hasnt been tested with any files. So that's a bridge for another day.

Magpai deals mostly with base64 encoded data, so hopefully we can just send that...

## TODO:
 - Install Cog if not installed
 - Install Docker if not installed
 - Install WSL on windows if not installed
 - Better response when model is being downloaded...
 - Create a bundlable executable
 - Webhooks
 - https://github.com/replicate/cog/issues/1459 (Australia is very far from r8.im...)
 - Lots of other stuff...