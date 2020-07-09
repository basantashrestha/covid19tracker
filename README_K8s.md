#### Before following these steps you will need to create the local registery of the container image. See here to create local registry 
https://gitlab.com/libresoftitsolutions/corona-patient-tracker/-/wikis/Creating%20&%20Working%20with%20Local%20Registry%20for%20Kubernetes
kubectl apply -f covid19nepal.yml
###But this looks very unstable. The image from local registry disappears. It is better to put it on dockerhub


##Expose the Service
#kubectl expose deployment.apps/covid19nepal-deployment --type=NodePort --port=8501
##No need for above line. Becaseu a service.yml file is created which exposes on 31200
kubectl apply -f service.yml


##Plot will be Available at IP:port
## If you are running on the virtual machine and trying to access from hostmachine. It is not working. 
