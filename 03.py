from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.structure.graph import Graph

graph = Graph()
g = graph.traversal().withRemote(DriverRemoteConnection('ws://localhost:8182/gremlin', 'g'))

hkVertexId = g.V().has('airport', 'code', 'HKG').id().next()

sydneyVertexId = g.V().hasLabel('airport').has('code', 'SYD').id().next()

x1 = g.V(hkVertexId).out().out().out().has('code', 'SYD').count().next()
print(x1)

print(g.V(hkVertexId).out().out().out().has('code', 'SYD').path().by('desc').fold().next())
