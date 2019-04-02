from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.structure.graph import Graph

graph = Graph()
g = graph.traversal().withRemote(DriverRemoteConnection('ws://localhost:8182/gremlin', 'g'))

print(g.E().hasLabel('route').count().next())

hkVertexId = g.V().has('airport', 'code', 'HKG').id().next()

sydneyVertexId = g.V().hasLabel('airport').has('code', 'SYD').id().next()

r = g.V(sydneyVertexId).outE('route').inV().values('desc')
x1 = g.V(sydneyVertexId).outE('route').inV().count().next()
for d in range(2):
    print(r.next())

print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
print(g.V(sydneyVertexId).outE('route').outV().values('desc').next())
