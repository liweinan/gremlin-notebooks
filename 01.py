from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.structure.graph import Graph

graph = Graph()
g = graph.traversal().withRemote(DriverRemoteConnection('ws://localhost:8182/gremlin', 'g'))

hkVertexId = g.V().has('airport', 'code', 'HKG').id().next()

sydneyVertexId = g.V().hasLabel('airport').has('code', 'SYD').id().next()

r = g.V().hasLabel('airport').has('code', 'SYD').next()
x1 = r.id
print(g.V(x1).valueMap(True).next())
