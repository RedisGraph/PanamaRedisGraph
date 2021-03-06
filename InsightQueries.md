## Exploring the Graph

Display all of the Labels

```
CALL db.labels()
```

Display all of the relationships

```
CALL db.relationshipTypes
```

Show me an example of an Office - click on Table view

```
MATCH (o:Officer) RETURN o LIMIT 1
MATCH (e:Entity) RETURN e LIMIT 1
MATCH (e:Address) RETURN e LIMIT 1
MATCH (e:Intermediary) RETURN e LIMIT 1
```

Show me some relationships

```
MATCH (a)-[g:INTERMEDIARY_OF]->(b) RETURN a,g,b LIMIT 1
MATCH (a)-[g:OFFICER_OF]->(b) RETURN a,g,b LIMIT 1
MATCH (a)-[g:REGISTERED_ADDRESS]->(b) RETURN a,g,b LIMIT 1
```

## Querying Nodes

Find me Entities in Hong Kong

```
MATCH (e:Entity{country_codes: 'HKG'}) RETURN e.name, e.countries LIMIT 10
```

Aggregate by Juristiction

```
MATCH (e:Entity) RETURN e.jurisdiction_description, count(e.jurisdiction_description) as count ORDER BY count DESC LIMIT 10
```

## Querying Relationships

Someone hiding deep

```
MATCH (a:Officer)-[:OFFICER_OF]->(b:Officer)-[:OFFICER_OF]->(j) RETURN a, b, j
```

## Variable Length Path Queries

Find all other officers 1-3 hops deep from U2's manager

```
MATCH path=(a:Officer{name:'PAUL ARTHUR MCGUINNESS'})-[*..3]-(x:Officer) RETURN DISTINCT(path)

```

List top 10 Countries for all connections 1-4 hops deep from Zylann

```
MATCH (a:Officer{name: 'ZYLANN PROPERTIES LIMITED'})-[*..4]-(x:Entity) RETURN count(x.countries) as count, a.name
MATCH (a:Officer{name: 'ZYLANN PROPERTIES LIMITED'})-[*..4]-(x:Entity) RETURN count(x.countries) as count, x.countries  ORDER BY count DESC LIMIT 10
```


## Using Search with queries

Finding all the Alpines

```
CALL db.idx.fulltext.queryNodes('Entity', 'Alpine') YIELD node RETURN node.name, node.countries
```

Companies with slightly different addresses

```
CALL db.idx.fulltext.queryNodes('Address', '25 Mason Complex') YIELD node WITH collect(node.id) as masons MATCH (e:Entity)-[:REGISTERED_ADDRESS]->(a:Address) WHERE a.id  in masons RETURN e.name
```


