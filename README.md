# PFE SEARCH ENGINE

A search engine for final year internships.

## Components

- __Frontend:__ Implemented with ReactJS. It consists of a search bar and a search filter. Once you execute the search, a list of the offers that correspond to your search will be returned. It queries the result from the Data Reader.
- __Data Reader:__ A Flask API that exposes an endpoint to do filtered searches.
- __Scrapper:__ Implemented with Go - used to be in Python - and Selenium APIs. It is used to scrap job offers to load them to the database using the Data Loader.
- __RabbitMQ:__ Used to transfer asynchronously the scrapped data to the Data Loader.
-__Data Loader:__ This consumes the scrapped data and loads them in the Database.
- __Database:__ We use Neo4J for our database. Having a Graph Database enables us to define perfectly the relations between the data.

## Workflow

The current workflow is the following;

![workflow](assets/whatwehavenow_archi.png)

## Node-Relationship model

The following _Node-Relationship_ model is defined as the following;

![node-rel-model](assets/NodeDiagram.png)

Thus, the database looks like the following;

![graph](assets/graph.png)

## Next Steps

- [x] Convert the scapping scripts to go and dockerize it.
- [x] Use RabbitMQ between the scrapper and the loader.
- [x] Seperate the backend to two different containers, one for the reader and one for the loader.
- [x] Add scripts for the Makefile.
- [x] Send messages in queue in Protocol Buffers - Google's data interchange format.
- [x] Add a prelimenary GitHub actions pipeline to push new docker images on every push.
- [ ] Add a pre-commit hook.
- [ ] Add logging in different components.
- [ ] Add application metrics using Prometheus API.
- [ ] Use K8S for deployment.
- [ ] Use Helm or Kustomize to package the different entities.
- [ ] Use ArgoCD for GitOps.
- [ ] Add application metrics and visualize them using Prometheus and Grafana.
- [ ] Add retention policy for logs both for dev and prod.
- [ ] Make an ingress with a domain name.
- [ ] Improve the front's UI.
- [ ] Add UTs.
- [ ] Add a CI/CD pipeline.
- [ ] Learn and apply security best practices.
