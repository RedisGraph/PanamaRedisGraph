# Panama Papers in Redis Graph

## Running with Docker

### Prerequisites 
- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Running Dockerized Version

```
git clone https://github.com/RedisLabs/PanamaRedisGraph.git
cd PanamaRedisGraph
docker-compose up
```

### Navigate to RedisInsight
[Open This Link in Your Browser](http://localhost:8001)

[Example Queries Available](./InsightQueries.md)


## Documentation


![Relationships](./relationships.png "Relationships")


## Manually loading the data

### Data Download Location
https://offshoreleaks.icij.org/pages/database

Download the zip file from above into the data_download diretory and unzip

### Clean the data

```
./run_all.sh
```

### Install the bulk loader and Load the data

```
pip3 install git+https://github.com/RedisGraph/redisgraph-bulk-loader.git@master
~/bin/redisgraph-bulk-loader PANAMA -n data_download/Officer.csv\
 -n data_download/Entity.csv  -n data_download/Address.csv \
 -n data_download/Intermediary.csv  -r ./data_download/INTERMEDIARY_OF.csv \
 -r ./data_download/OFFICER_OF.csv -r ./data_download/REGISTERED_ADDRESS.csv
```

### Query Away!!

create some full text searching for some fun

```
GRAPH.QUERY PANAMA "CALL db.idx.fulltext.createNodeIndex('Address', 'address')"
GRAPH.QUERY PANAMA "CALL db.idx.fulltext.createNodeIndex('Entity', 'name')"
GRAPH.QUERY PANAMA "CALL db.idx.fulltext.createNodeIndex('Officer', 'name')"
```

