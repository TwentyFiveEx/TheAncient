These are alternative build scripts, if for some reason you don't have make.
It's pretty simple and doesn't do much in the way of error checking.. 

* Login to docker.com
* Build the docker image
* Push the docker image to docker.com

Just run: ./manual-build/release.sh  

Or individually run:
* ./manual-build/docker-login.sh
* ./manual-build/build.sh
* ./manual-build/docker-push.sh
Additionally:
* ./manual-build/github-push-tag.sh

github-push-tag.sh: will grab the current hash (which we use as the  
same tag for the Docker image) and push that as a tag back to github.  
This allows you to associate what code is inside a container image  
with a specific atomic commit in the codebase.
