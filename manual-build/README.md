These are alternative build scripts, if for some reason you don't have make.
It's pretty simple and doesn't do much in the way of error checking.. 

* Login to docker.com
* Build the docker image
* Push the docker image to docker.com

Just run: ./manual-build/release.sh  

Or individually run:
* ./manual-build/docker-login.sh
* ./manual-build/build.sh
* ./manual-build/push.sh
