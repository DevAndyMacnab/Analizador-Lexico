import graphviz

d = graphviz.Digraph(filename='rank_same.gv')

with d.subgraph() as s:
    s.attr(rank='same')
    s.attr("node",shape="circle",style="filled")
    s.node('A')
    s.node('X')
    s.node('B')
    s.node('D')
    s.node('Y')
    s.node("C")



d.edges(['AB', 'AC', 'CD', 'XY'])

d.view()