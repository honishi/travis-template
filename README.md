travis template
==
[![Build Status](https://travis-ci.org/honishi/travis-template.png?branch=master)](https://travis-ci.org/honishi/travis-template)

snippet
--
create secure env variables.
````
travis encrypt MY_SECURE_ENV_VAR='THIS-IS-SECURE-VAR'
travis encrypt MY_SECURE_ENV_VAR='THIS-IS-SECURE-VAR' --add
````
change submodule url.
````
# change content .gitmodules inside
#   - git@github.com:tweepy/tweepy.git
#   - https://github.com/tweepy/tweepy.git
vi .gitmodules
git submodule sync
````
