CI steps
--------

1. find list of dockerfiles to build.
    1. look at list of changed files in git since last push (can contain multiple commits).
    1. if `FORCE_REBUILD_GLOB` environ variable is set, search the project
       repo with this pattern. The glob pattern supports the same matching rules
       used in Unix shell. Example: `dl/tensorflow/1.0.1/Dockerfile-py[2-3]`.
1. build image from dockefile (uses `floykder build` command).
1. test new image if there is any test defined (uses `floydker test` command).
1. push image to dockerhub (TODO).


See [floydker's documentation](https://github.com/floydhub/dockerfiles/blob/master/floydker/README.md)
on how to generate dockerfiles with templates using `floydker render` command
and define tests for dockerfiles in `matrix.yml`.
